# HW08 Deploying Our Project to the Internet

## New things to do...

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

- Make django actually workable in Heroku

    pipenv install waitress whitenoise dj-database-url psycopg2-binary
    code yummytomatoes\settings.py (for WHITENOISE as a static file server)
        Remove this from INSTALLED_APPS:
            'django.contrib.staticfiles',
        Add this to INSTALLED_APPS:
            'whitenoise.runserver_nostatic',
        Add this to MIDDLEWARE:
            'whitenoise.middleware.WhiteNoiseMiddleware',
        Add this to END:
            STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    code yummytomatoes\settings.py (for POSTGRES database server when available)
        Add this to below DATABASES:
            import dj_database_url
            db_from_env = dj_database_url.config(conn_max_age=500)
            DATABASES['default'].update(db_from_env)
    code yummytomatoes\settings.py (for the Internet to actually get to HEROKU pages)
        Replace the default ALLOWED_HOSTS with this:
            ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']
            CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com']
    code Procfile (so Heroku knows how to RUN our Django app / Heroku Dyno)
        release: python manage.py migrate
        web: waitress-serve --port $PORT --threads $WEB_CONCURRENCY yummytomatoes.wsgi:application    
    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set DISABLE_COLLECTSTATIC=1

- Run the rest of the Heroku commands

    git add .
    git commit -am "Initial Heroku attempt"
    git push heroku master