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

- Building login and logout views and a login template

        code common\views.py
        code common\urls.py
        code common\templates\common\login.html (for the form)
        code yummytomatoes\settings.py
            LOGIN_URL = "/login/"

- Making the base template show 'messages' and use bootstrap styling

        code common\templates\common\base.html
        code yummytomatoes\settings.py
            from django.contrib.messages import constants as messages
            MESSAGE_TAGS = {
                messages.DEBUG: 'alert-secondary',
                messages.INFO: 'alert-info',
                messages.SUCCESS: 'alert-success',
                messages.WARNING: 'alert-warning',
                messages.ERROR: 'alert-danger',
            }

- Adding login-awareness to our base template

        code common\templates\common\base.html

Adding ***authorization***

- Creating groups and assigning permissions
- Creating users and assigning groups
- Adding permissions to our views

        code movies\urls.py

        create: myapp.add_mymodel
        read:   myapp.view_mymodel
        update: myapp.change_mymodel
        delete: myapp.delete_mymodel

- Adding awareness to our templates

        code movies\templates\movies\movie_list.py
        code movies\templates\movies\movie_detail.py
        code movies\templates\movies\movie_form.py

        create: perms.myapp.add_mymodel
        read:   perms.myapp.view_mymodel
        update: perms.myapp.change_mymodel
        delete: perms.myapp.delete_mymodel
