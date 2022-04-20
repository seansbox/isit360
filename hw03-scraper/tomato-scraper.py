import csv
import datetime
import json
import re
import os
import sqlite3
from scraper import *
from sqlitedict import SqliteDict
from slugify import slugify

schema = {
    'movies': {
        'id': 'TEXT PRIMARY KEY',
        'name': 'TEXT',
        'release': 'TEXT',
        'meter': 'INTEGER',
        'score': 'INTEGER',
        'thumb': 'TEXT',
        'summary': 'TEXT'
    },
    'celebs': {
        'id': 'TEXT PRIMARY KEY',
        'name': 'TEXT',
        'birthday': 'TEXT',
        'birthplace': 'TEXT',
        'thumb': 'TEXT',
        'summary': 'TEXT'
    },
    'genres': {
        'id': 'TEXT PRIMARY KEY',
        'name': 'TEXT'
    },
    'map_movie_celeb': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'movie_id': 'TEXT',
        'celeb_id': 'TEXT'
    },
    'map_movie_genre': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'movie_id': 'TEXT',
        'genre_id': 'TEXT'
    }
}

class TomatoScraper(Scraper):
    def __init__(self):
        self.cache = {}
        super().__init__()

    # Make our scraper save some time by caching page-parses that it has already completed
    def set_cache_db(self, file):
        self.cache = SqliteDict(file,
            encode = json.dumps,
            decode = json.loads,
            tablename = "scraper",
            autocommit = True)

    # Download the top 100 movies list from RottenTomatoes.com
    def get_top_100(self):
        self.get_page('https://www.rottentomatoes.com/top/bestofrt/')
        movies = []
        for movie_el in self.find_fast_elements("//a[@class='unstyled articleLink']"):
            if movie_el.get('href', '').startswith('/m/'):
                movies.append({
                    'id': movie_el.get('href').strip(),
                    'name': (movie_el.text or '').strip()
                })
        return movies
    
    # Returns the text of the first matched xpath element, or '' if empty/non-existant
    def find_first_text(self, xpath, dom=None):
        el = self.find_fast_elements(xpath, dom)
        if not el: return ''
        return (el[0].text or '').strip()

    # Returns the date value of the text of the first matched xpath element, or '' if empty/non-existant
    def find_first_date(self, xpath):
        el = self.find_fast_elements(xpath)
        if not el: return ''
        text = (el[0].text or '').strip()
        text = re.sub(r'^[A-Za-z]+:', '', text).strip() # better than text.replace('Birthday:')?
        try:
            return datetime.datetime.strptime(text, '%b %d, %Y').date().isoformat()
        except ValueError:
            return ''

    # Downloads a movie page and parses the relevant data
    def get_movie_data(self, href):
        data = self.cache.get(href, None)
        if data: return data
        self.get_page(f"https://www.rottentomatoes.com{href}")
        data = {}
        data['id'] = href
        data['name'] = self.find_first_text("//h1[@data-qa='score-panel-movie-title']")
        data['summary'] = self.find_first_text("//div[@data-qa='movie-info-synopsis']")
        data['genre'] = [g.strip() for g in self.find_first_text("//div[@class='meta-value genre']").split(',')]
        data['release'] = self.find_first_date("//div[@data-qa='movie-info-item-value']/time")
        data['thumb'] = self.find_fast_elements("//img[contains(@class, 'posterImage')]")[0].get('src', '')
        tomo = self.find_fast_elements("//score-board")
        data['meter'] = tomo[0].get('tomatometerscore', '') # self.find_first_text("//span[@data-qa='tomatometer']", tomo[0])
        data['score'] = tomo[0].get('audiencescore', '') # self.find_first_text("//span[@data-qa='audience-score']", tomo[0])
        celebs = []
        celebs_els = self.find_fast_elements("//a[@data-qa='cast-crew-item-link']")
        for celebs_el in celebs_els:
            celeb_name = celebs_el.xpath('span')[0].text.strip()
            celeb_id = celebs_el.get('href').strip()
            celebs.append({ 'id': celeb_id, 'name': celeb_name })
        data['celebs'] = celebs
        self.cache[href] = data
        return data

    # Downloads a celebrity page and parses the relevant data
    def get_celeb_data(self, href):
        data = self.cache.get(href, None)
        if data: return data
        self.get_page(f"https://www.rottentomatoes.com{href}")
        data = {}
        data['id'] = href
        data['name'] = self.find_first_text("//h1[@data-qa='celebrity-bio-header']")
        data['birthday'] = self.find_first_date("//p[@data-qa='celebrity-bio-bday']")
        birthplace = self.find_first_text("//p[@data-qa='celebrity-bio-birthplace']")
        data['birthplace'] = re.sub(r'^[A-Za-z]+:', '', birthplace).strip() # Strip off 'Birthplace:' or whatever
        data['summary'] = self.find_first_text("//p[@data-qa='celebrity-bio-summary']")
        data['thumb'] = self.find_fast_elements("//img[contains(@class, 'celebrity-bio__hero-img')]")[0].get('src', '')
        self.cache[href] = data
        return data

if __name__ == '__main__':
    # Shortcut function to save a list (of dicts) to a CSV document (with the included dict field names)
    def save_list_as_csv(filename, obj, fieldnames):
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(obj)

    def save_list_to_sql(cursor, table, l, fieldnames):
        for d in l:
            columns = ', '.join(fieldnames)
            placeholders = ':' + ', :'.join(fieldnames)
            query = 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns, placeholders)
            cursor.execute(query, d)

    rt = TomatoScraper()
    rt.set_cache_db(os.path.join('working', 'cache.db'))

    # We're going to store our data in this variable and then export it to .csv and .db
    data = {
        'movies': {},
        'celebs': {},
        'genres': {},
        'map_movie_celeb': {},
        'map_movie_genre': {},
    }

    top_movies = rt.get_top_100() # Get the list of top movies

    # Loop through the movie list
    for movie in top_movies:
        # Get each movie detail
        print(f"{str(len(data['movies'])+1).zfill(3)}/ {movie['name']} @ {movie['id']}...")
        data['movies'][movie['id']] = rt.get_movie_data(movie['id'])
        # Convert the format of the genres from text to href/text
        genres = []
        for genre in data['movies'][movie['id']]['genre']:
            genres.append({ 'id': slugify(genre), 'name': genre })
        data['movies'][movie['id']]['genre'] = genres
        # Extract the genre and genre-to-movie mapping data
        for genre in data['movies'][movie['id']]['genre']:
            data['genres'][genre['id']] = genre
            data['map_movie_genre'][len(data['map_movie_genre'])+1] = { 'id': len(data['map_movie_genre'])+1, 'movie_id': movie['id'], 'genre_id': genre['id'] }
        # Loop through the celebrities in the movie and get their details too!
        for celeb in data['movies'][movie['id']]['celebs']:
            print(f"     {celeb['name']} @ {celeb['id']}...")
            if not celeb['id'] in data['celebs']: # We don't need to download this celeb if we already have
                data['celebs'][celeb['id']] = rt.get_celeb_data(celeb['id'])
            # Extract the celeb to movie mapping data
            data['map_movie_celeb'][len(data['map_movie_celeb'])+1] = { 'id': len(data['map_movie_celeb'])+1, 'movie_id': movie['id'], 'celeb_id': celeb['id'] }

    # Finally, save all that data to .csv files!
    for table, scheme in schema.items():
        save_list_as_csv(os.path.join('working', f"{table}.csv"), data[table].values(), schema[table].keys())

    # And save it all to SQL too!
    con = sqlite3.connect(os.path.join('working', 'tomatoes.db'))
    cur = con.cursor()
    for table, scheme in schema.items():
        columns = ','.join([f"{k} {v}" for k, v in scheme.items()])
        cur.execute(f"DROP TABLE IF EXISTS {table}")
        cur.execute(f"CREATE TABLE {table} ({columns})")
        save_list_to_sql(cur, table, data[table].values(), scheme.keys())
        con.commit()