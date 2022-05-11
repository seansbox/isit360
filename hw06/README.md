# HW06
Setting up a Web-based App

## How to run this project

    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver
    heroku local -f Profile.windows

## How I originally built the project

    mkdir hw06
    cd hw06
    code .
    pipenv isntall django waitress dj-database-url whitenoise psycopg2-binary
    pipenv shell
    django-admin startproject yummytomatoes .
    python manage.py showmigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    explorer http://127.0.0.1:8000/admin/

## How I setup an initial app/model

    python manage.py startapp movies
    code movies/models.py
    code yummytomatoes/settings.py
        INSTALLED_APPS
    python manage.py makemigrations
    python manage.py showmigrations
    python manage.py sqlmigrate movies 0001
    python manage.py migrate

    python manage.py makemigrations --empty movies
    code movies/migrations/0002_default_data.py
    python manage.py migrate
    python manage.py runserver

## How I setup an initial admin portal

    code movies/admin.py

## How I setup an initial home page

    code yummytomatoes/urls.py
        'DIRS': [os.path.join(BASE_DIR, 'yummytomatoes', 'templates')]
    code movies/urls.py
    code yummytomatoes/urls.py
        path('', include('movies.urls')),
    code movies/templates/movies/index.html

## How I deployed my app to Heroku

Install Heroku's command-line tool...

    -- sign-up for free at https://signup.heroku.com/
    Windows PowerShell as Administrator:
        choco install heroku-cli
    macOS Terminal:
        brew tap heroku/brew && brew install heroku

Create some new fancy Heroku files...

    echo web: waitress-serve --listen "*:$PORT" --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-for x-forwarded-proto x-forwarded-port' --log-untrusted-proxy-headers --clear-untrusted-proxy-headers --threads ${WEB_CONCURRENCY:-4} yummytomatoes.wsgi:application > Procfile
    echo web: waitress-serve --port %PORT% yummytomatoes.wsgi:application > Procfile.windows
    echo SECRET_KEY=vd;ohvhvhsvhsklfvhlekjhvli3n > .env

Make some changes in app/settings.py...

    add 'import os' to the TOP
    replace SECRET_KEY with: SECRET_KEY=os.environ['SECRET_KEY']
    add 'whitenoise.runserver_nostatic' to INSTALLED_APPS
    add ['localhost', '127.0.0.1', '.herokuapp.com'] to ALLOWED_HOSTS
    add CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com'] just below ALLOWED_HOSTS
    add 'whitenoise.middleware.WhiteNoiseMiddleware' right after 'SecurityMiddleware' to MIDDLEWARE
    add after DATABASES:
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
    add to the bottom:
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

Create our Heroku project and test it

    heroku login
    heroku create yummytomatoes
        or
    heroku git:remote -a yummytomatoes
    heroku local -f Procfile.windows

    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set DJANGO_SUPERUSER_USERNAME=admin
    heroku config:set DJANGO_SUPERUSER_PASSWORD=PASSWORD
    heroku config:set DJANGO_SUPERUSER_EMAIL=seansbox@gmail.com
    heroku config:set SECRET_KEY=django-sfgljheroghoh3h8*y9889y

    Just for me, due to using subfolders:
        heroku buildpacks:clear
        heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
        heroku buildpacks:add heroku/python
        heroku config:set PROJECT_PATH=hw06

    git add .
    git commit -m "Adds Heroku"
    git push heroku
    heroku run:detached python manage.py migrate
    heroku run:detached python manage.py createsuperuser --noinput
    heroku open

## Handy references

- Django Models: https://docs.djangoproject.com/en/4.0/topics/db/models/
- Model Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/
- Heroku/Django Guide: https://realpython.com/django-hosting-on-heroku/
- Heroku/Django Guide: https://medium.com/geekculture/how-to-deploy-a-django-app-on-heroku-4d696b458272
- Heroku/Waitress Guide: https://docs.pylonsproject.org/projects/waitress/en/stable/usage.html
- Waitress Web Server: https://docs.pylonsproject.org/projects/waitress/en/latest/
- WhiteNoise Static File Server: http://whitenoise.evans.io/en/stable/
- Bootstrap Introduction: https://getbootstrap.com/docs/5.1/getting-started/introduction/
- Bootstrap Examples: https://getbootstrap.com/docs/5.1/examples/
- Bootswatch Themes: https://bootswatch.com/

## Handy reading

- https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- https://docs.djangoproject.com/en/4.0/intro/tutorial02/
- https://docs.djangoproject.com/en/4.0/intro/tutorial03/
