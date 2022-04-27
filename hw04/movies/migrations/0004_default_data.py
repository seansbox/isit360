import csv, os

from django.db import migrations

def rotten_data(apps, schema_editor):
    # We can't import the Movie model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Movie = apps.get_model('movies', 'Movie')
    with open(os.path.join('movies', 'rawdata', 'movies.csv'), 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m = Movie(
                name=row['name'],
                release=row['release'],
                thumb=row['thumb'],
                summary=row['summary'],
                meter=row['meter'],
                score=row['score'],
            )
            m.save()

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_celeb_movies'),
    ]

    operations = [
        migrations.RunPython(rotten_data),
    ]
