# Generated by Django 4.0.4 on 2022-04-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_celeb'),
    ]

    operations = [
        migrations.AddField(
            model_name='celeb',
            name='movies',
            field=models.ManyToManyField(to='movies.movie'),
        ),
    ]