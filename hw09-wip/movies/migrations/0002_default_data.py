import csv
import os

from django.db import migrations

def rotten_data(apps, schema_editor):
    Celeb = apps.get_model('movies', 'Celeb')
    Genre = apps.get_model('movies', 'Genre')
    Movie = apps.get_model('movies', 'Movie')
    celebs_by_id = {}
    genres_by_id = {}
    movies_by_id = {}
    with open(os.path.join('movies', 'default_data', 'celebs.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            old_id = row['id']
            del row['id']
            if not row['birthday']: del row['birthday']
            if row['birthplace'] == 'Not Available': del row['birthplace']
            c = Celeb(**row)
            c.save()
            celebs_by_id[old_id] = c
    with open(os.path.join('movies', 'default_data', 'genres.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            old_id = row['id']
            del row['id']
            g = Genre(**row)
            g.save()
            genres_by_id[old_id] = g
    with open(os.path.join('movies', 'default_data', 'movies.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            old_id = row['id']
            del row['id']
            m = Movie(**row)
            m.save()
            movies_by_id[old_id] = m
    with open(os.path.join('movies', 'default_data', 'map_movie_genre.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m = movies_by_id[row['movie_id']]
            g = genres_by_id[row['genre_id']]
            m.genres.add(g)
    with open(os.path.join('movies', 'default_data', 'map_movie_celeb.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m = movies_by_id[row['movie_id']]
            c = celebs_by_id[row['celeb_id']]
            m.celebs.add(c)

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(rotten_data),
    ]
