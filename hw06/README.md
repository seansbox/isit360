# HW06
Setting up a Web-based App

## How to run this project

    poetry install
    poetry run python manage.py migrate
    poetry run python manage.py runserver

## How I originally built the project

    poetry config virtualenvs.in-project true
    mkdir hw06
    cd hw06
    poetry init -n
    code .
    poetry shell
    poetry add django
    django-admin startproject freshtomatoes .
    python manage.py showmigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    explorer http://127.0.0.1:8000/admin/

## How I setup an initial app/model

    python manage.py startapp movies
    --- edit movies/models.py
    --- edit freshtomatoes/settings.py (INSTALLED_APPS)
    python manage.py makemigrations
    python manage.py showmigrations
    python manage.py sqlmigrate movies 0001
    python manage.py migrate

    python manage.py makemigrations --empty movies
    --- edit movies/migrations/0002_default_data.py
    python manage.py migrate
    python manage.py runserver

## How I setup an initial admin portal

    --- edit movies/admin.py

## How I deployed my app to Heroku

    -- sign-up for free at https://signup.heroku.com/
    choco install heroku-cli (Windows PowerShell as Administrator)
    brew tap heroku/brew && brew install heroku (macOS Terminal)

    heroku login
    poetry export -f requirements.txt --output requirements.txt
    --- then cleanup requirements.txt
    echo python-3.9.6 > runtime.txt
    echo "web: python manage.py runserver 0.0.0.0:\$PORT" > Procfile
    heroku create clean-tomatoes
    heroku local --port 5001

## Handy references

- Heroku/Django Setup Guide: https://realpython.com/django-hosting-on-heroku/
- Django Models: https://docs.djangoproject.com/en/4.0/topics/db/models/
- Model Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/