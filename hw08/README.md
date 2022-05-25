# HW08 Deploying a Database Application

*This folder accompanies a live session recording available on Canvas for this course.*

We're going to move our database web application to the Internet. To do that we need to make some "tweaks" to how Django serves up our website. ***python manage.py runserver*** will still work locally, but it is not recommended to use in production. We're going to use ***waitress*** and ***whitenoise***, two ultra-fast python projects, to make our application able to scale to Instragram-level success! Because we can. We'll also need to migrate from ***Sqlite*** to ***Postgres*** for Internet production so we have a true, persistent data store for our data to live in.

## Stuff to study...

- https://docs.pylonsproject.org/projects/waitress/en/stable/usage.html
- http://whitenoise.evans.io/en/stable/
- https://realpython.com/django-hosting-on-heroku/
- https://medium.com/geekculture/how-to-deploy-a-django-app-on-heroku-4d696b458272

## How to make it happen...

- Sign-up for an account at Heroku! (https://signup.heroku.com/)
- Install the Heroku command-line tool (run PowerShell as Administrator)

        choco install heroku-cli

- Create a new Heroku project at https://dashboard.heroku.com/apps
- Make sure git knows who you are:

        git config --global user.name "FIRST_NAME LAST_NAME"
        git config --global user.email "MY_NAME@example.com"

- Follow along with the Heroku app steps:

        heroku login
        cd yummytomatoes/
        git init
        heroku git:remote -a yummytomatoes

- Make django production-ready in Heroku!

        pipenv install waitress whitenoise dj-database-url psycopg2-binary
        heroku addons:create heroku-postgresql:hobby-dev
        heroku config:set DISABLE_COLLECTSTATIC=1

    - Edit ***yummytomatoes\settings.py*** (for ***WHITENOISE*** as our static file server)

            Remove this from INSTALLED_APPS:
                'django.contrib.staticfiles',
            Add this to INSTALLED_APPS:
                'whitenoise.runserver_nostatic',
            Add this to MIDDLEWARE:
                'whitenoise.middleware.WhiteNoiseMiddleware',
            Add this to END:
                STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    - Edit ***yummytomatoes\settings.py*** (for ***POSTGRES*** as our database server when available)

            Add this to below DATABASES:
                import dj_database_url
                db_from_env = dj_database_url.config(conn_max_age=500)
                DATABASES['default'].update(db_from_env)

    - Edit ***yummytomatoes\settings.py*** (to tell Django to trust ***HEROKU***)

            Replace the default ALLOWED_HOSTS with this:
                ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']
                CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com']

    - Edit ***Procfile*** (so Heroku knows how to ***RUN*** our Django app / Heroku Dyno)

            release: python manage.py migrate
            web: waitress-serve --port $PORT --threads $WEB_CONCURRENCY yummytomatoes.wsgi:application    

- Run the rest of the Heroku app commands (to deploy our app to Heroku!)

        git add .
        git commit -am "Initial Heroku attempt"
        git push heroku master

- Visit your new website!