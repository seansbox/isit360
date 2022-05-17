# HW07 Making Templates and Displaying Data

## Important topics...

- More on ***template*** files
- Adding in ***static*** files
- Exposing a ***model*** to a ***controller***
- Using ***scripts*** in Pipfiles

## Select reading...

- https://docs.djangoproject.com/en/4.0/intro/tutorial03/
- https://docs.djangoproject.com/en/4.0/intro/tutorial06/

## Running this project...

    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver

## How I built this project...

- See HW06 for baseline, then...

    pipenv run python manage.py startapp common
    code yummytomatoes\settings.py to restore 'DIRS': [], and add 'common' app
    mkdir common\templates
    mkdir common\templates\common
    mkdir common\static
    mkdir common\static\common
    move yummytomatoes\templates to common\templates\common
    code movies\templates\movies\base.html to extend common/base.html
    code common\urls.py
    code common\views.py
    breakout front and help pages/views/urls
    add app_name = 'x' to urls.py
    update all of the template files...
        fix new template paths
        move to {% url 'x:y' %} style links

## Useful references...

- https://django-book.readthedocs.io/en/latest/index.html