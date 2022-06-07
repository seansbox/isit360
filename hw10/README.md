# HW10 Authentication and Authorization

*This folder accompanies a live session recording available on Canvas for this course.*

We've covered just about every primary topic in building a database application using Django! But last module we left a website running on the Internet that allows anonymous users to make changes to our data! NOOOO! Let's fix that this module by adding user ***authentication and authorization*** to our app! Luckily, as usual Django does most of the hard work for us. We just need to do some plumbing to connect the pipes...

## Important topics...

- Adding ***authentication***: building login and logout views and templates
- Adding ***authorization***: defining which users are allowed to do what

## Select reading...

- https://docs.djangoproject.com/en/4.0/ <-- START HERE
- https://docs.djangoproject.com/en/4.0/topics/auth/
- https://docs.djangoproject.com/en/4.0/topics/auth/default/
- https://docs.djangoproject.com/en/4.0/topics/auth/passwords/

## Running this project...

    pipenv install
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser
    pipenv run python manage.py runserver

## How I built the project...

See HW09 for baseline, then...

Adding ***authentication***

- Building login and logout views
- Building login and logout templates

    code yummytomatoes\settings.py
        LOGIN_URL = "/login/"
        LOGIN_REDIRECT_URL = "/"
        LOGOUT_REDIRECT_URL = "/"
    code common\templates\common\login.html
    code yummytomatoes\urls.py

Adding ***authorization***

- Creating groups and assigning permissions
- Adding permissions to our views
- Adding logic to our templates

    code movies\views.py
    code movies\urls.py
