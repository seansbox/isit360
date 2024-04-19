import sqlite3

con = sqlite3.connect("hw03.sqlite3")
cur = con.cursor()

sql = """
    SELECT movies.name, movies.release, celebs.name, celebs.birthday
      FROM movies
    LEFT OUTER JOIN map_movie_celeb
      ON map_movie_celeb.movie_id = movies.id
    LEFT OUTER JOIN celebs
      ON map_movie_celeb.celeb_id = celebs.id
    WHERE movies.id = '/m/the_wizard_of_oz_1939'
    ORDER BY celebs.birthday
"""

print("Celebrities and Birthdays from the Wizard of Oz...")
for row in cur.execute(sql):
    print(f"{row[2]} {row[3]}")
