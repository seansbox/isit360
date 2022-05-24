# HW08 Data Forms and Permissions

## Important topics...

- Adding ***related*** data to a view (from HW07)
- Adding forms to our ***template*** files (in SE08)
- Adding login, logout, and ***authentication*** (in SE08)
- Customing the ***admin*** site using ***inline*** forms (for QZ08)

## Select reading...

- https://docs.djangoproject.com/en/4.0/ <-- START HERE
- https://docs.djangoproject.com/en/4.0/intro/tutorial04/
- https://docs.djangoproject.com/en/4.0/intro/tutorial07/
- https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
- https://docs.djangoproject.com/en/4.0/topics/auth/default/

## Running this project...

    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser
    pipenv run python manage.py runserver

## How I built the project...

See HW07 for baseline, then...

Add related data to a view... 

    code movies\templates\movies\details.html

Add login, logout, and ***authentication***...

    code yummytomatoes\settings.py
        LOGIN_URL = "/login/"
        LOGIN_REDIRECT_URL = "/"
        LOGOUT_REDIRECT_URL = "/"
    code common\templates\common\login.html
    code yummytomatoes\urls.py

Add an edit form template and view...

    pipenv install django-crispy-forms
    code yummytomatoes\settings.py
        INSTALLED_APPS = (
            ...
            'crispy_forms',
        )
        CRISPY_TEMPLATE_PACK = 'bootstrap4'
    code movies\views.py
    code movies\urls.py
    code movies\templates\movies\movie_list.html
    code movies\templates\movies\movie_detail.html
    code movies\templates\movies\movie_form.html
    code movies\templates\movies\movie_confirm_detail.html
