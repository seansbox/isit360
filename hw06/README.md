# HW06
Setting up a Web-based App

## How to run this project...

    python -m pip install pipenv --force (PowerShell as Administrator)
    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver

## How I built this project...

    python -m pip install pipenv (PowerShell as Administrator)
    mkdir hw06-live
    cd hw06-live
    code .
    pipenv install django waitress dj-database-url whitenoise psycopg2-binary
    pipenv shell
    django-admin startproject yummytomatoes .
    python manage.py showmigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

## How I added a model...

    python manage.py startapp movies
    code movies\models.py
    code yummytomatoes\settings.py
    python manage.py makemigrations
    python manage.py showmigrations
    python manage.py sqlmigrate movies 0001
    python manage.py migrate

## How I added default data...

    python manage.py makemigrations --empty movies
    ren movies\migrations\0002_whatever_it_is.py 0002_default_data.py
    code movies\migrations\0002_default_data.py
    python manage.py migrate

## How I built an admin site...

    python manage.py runserver
    explorer http://127.0.0.1:8000/admin/
    code movies\admin.py
    python manage.py runserver

## How I made the front page...

    code yummytomatoes\settings.py
        @ TOP:
            import os
        @ TEMPLATES:
            'DIRS': [os.path.join(BASE_DIR, 'yummytomatoes', 'templates')],
    
    mkdir yummytomatoes\templates
    mkdir movies\templates
    mkdir movies\templates\movies

    code yummytomatoes\templates\base.html
    code movies\templates\movies\base.html
    code movies\templates\movies\index.html
    code movies\templates\movies\celebs.html

    code yummytomatoes\urls.py
    code movies\urls.py

    BASE    >    BASE    >    INDEX
    ^ PROJECT    ^ APP        ^ APP

## Handy references

- Bootstrap Introduction: https://getbootstrap.com/docs/5.1/getting-started/introduction/
- Bootstrap Examples: https://getbootstrap.com/docs/5.1/examples/
- Bootswatch Themes: https://bootswatch.com/
- Django Templates: https://docs.djangoproject.com/en/4.0/topics/templates/
- Django Models: https://docs.djangoproject.com/en/4.0/topics/db/models/
- Model Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/

## Handy reading

- https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- https://docs.djangoproject.com/en/4.0/intro/tutorial02/
- https://docs.djangoproject.com/en/4.0/intro/tutorial03/
