# HW09 Data Forms and Permissions

*This folder accompanies a live session recording available on Canvas for this course.*

Our database app is up and running and even deployed to Heroku! NOW... let's add the ability for ***users*** of our web app to make changes. Presently we have our website, and we have our admin site. Let's make it so we can allow anonymous users (terrible idea) to make changes to the website! We'll add user authentication next module!

## Important topics...

- Intro to HTML ***forms***, GET and POST actions ([link](https://docs.djangoproject.com/en/4.0/topics/forms/))
- Cheating with ***class-based generic views*** ([link](https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/))
- Adding views and templates for ***create***, ***update***, and ***delete*** actions.

## Stuff to study...

- https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/
- https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
- https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/

## How to make it happen...

- Refactor/rename the template files...
- Change our views.py (and urls.py) to use class-based generic views...
- Add create, update, and delete views and templates...
- Use crispy_forms_tags to make create/update forms use Bootstrap styling...
