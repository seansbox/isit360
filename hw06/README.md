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
    poetry add django gunicorn dj-database-url whitenoise psycopg2-binary
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

Install Heroku's command-line tool...

    -- sign-up for free at https://signup.heroku.com/
    choco install heroku-cli (Windows PowerShell as Administrator)
    brew tap heroku/brew && brew install heroku (macOS Terminal)

Create some new fancy Heroku files...

    poetry export --format requirements.txt --without-hashes --output requirements.txt
    --- then cleanup requirements.txt (remove any extras)
    echo python-3.9.6 > runtime.txt
    echo web: python manage.py runserver 0.0.0.0:$PORT > Procfile
    echo web: gunicorn clean-tomatoes.wsgi > Procfile

Make some changes in app/settings.py...

    replace SECRET_KEY with: SECRET_KEY=os.environ['SECRET_KEY']
    add 'whitenoise.runserver_nostatic' to INSTALLED_APPS
    add ['localhost', '127.0.0.1', '.herokuapp.com'] to ALLOWED_HOSTS
    add 'whitenoise.middleware.WhiteNoiseMiddleware' right after 'SecurityMiddleware' to MIDDLEWARE
    add 'import os' to the TOP
    add to the bottom:
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    add after DATABASES
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
    python manage.py runserver 0.0.0.0
    waitress-serve freshtomatoes.wsgi:application

Create our Heroku project and test it

    heroku login
    heroku create clean-tomatoes
        or
    heroku git:remote -a clean-tomatoes
    heroku local --port 5001

    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set DJANGO_SUPERUSER_USERNAME=admin
    heroku config:set DJANGO_SUPERUSER_PASSWORD=PASSWORD
    heroku config:set DJANGO_SUPERUSER_EMAIL=seansbox@gmail.com
    heroku config:set SECRET_KEY=django-sfgljheroghoh3h8*y9889y
    heroku run:detached python manage.py migrate
    heroku run:detached python manage.py createsuperuser --noinput
    heroku open

## Handy references

- Heroku/Django Setup Guide: https://realpython.com/django-hosting-on-heroku/
- Django Models: https://docs.djangoproject.com/en/4.0/topics/db/models/
- Model Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/
- Heroku/Django Guide: https://medium.com/geekculture/how-to-deploy-a-django-app-on-heroku-4d696b458272
- Heroku/Waitress Guide: https://docs.pylonsproject.org/projects/waitress/en/stable/usage.html