# Generated by Django 4.0.4 on 2022-06-08 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_default_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celeb',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['name']},
        ),
    ]
