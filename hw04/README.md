# HW04 Mapping Objects and Speaking Excel

## How I Built This

    poetry config virtualenvs.in-project true
    mkdir hw04
    cd hw04
    poetry init -n
    code .
    poetry add django
    django-admin startproject hw04 .
    python manage.py showmigrations
    python manage.py migrate
    sqlite_web db.sqlite3

## How I Added A Movie App To It

    python manage.py startapp movies
    --- edit movies/models.py
    --- edit hw04/settings.py (INSTALLED_APPS)
    python manage.py makemigrations
    python manage.py showmigrations
    python manage.py sqlmigrate movies 0001
    python manage.py migrate
    sqlite_web db.sqlite3

## How I Added Movie Data To It

    python manage.py makemigrations --empty movies
    --- edit hw04/migrations/00***.py

## How To Run This

    poetry install
    poetry run manage.py migrate
    poetry run manage.py runserver

## Handy References

- Django Models: https://docs.djangoproject.com/en/4.0/topics/db/models/
- Model Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/