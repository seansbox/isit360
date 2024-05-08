# HW06 Welcome to Django and PythonAnywhere

_Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion._

# Objectives

- Understand the components and architecture of Django.
- Set up an Internet-facing development environment.
- Create a basic Django project.
- Understand the structure of a Django project.

# Introduction to Django

[Django](https://www.djangoproject.com/) is a high-level, open-source web framework written in Python that enables rapid development of secure and maintainable websites. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's great for small projects and scales well to large; for example, it's what powers Instagram and Pinterest! It’s free and open source and has an exceptional ORM (Object-Relational Mapping) system that allows you to interact with your database using Python objects. We've explored ORMs previously using SQLAlchemy, and Django's ORM is similar (and simpler) in many ways.

Here’s a quick overview of Django:

- Full-Featured Framework: Django follows the "batteries-included" philosophy and provides almost everything developers might want to do "out of the box". This means it includes a lot of built-in features, such as an admin panel, user authentication, and an ORM (Object-Relational Mapping) that facilitates database queries.
- Rapid Development: Django was designed to help developers take applications from concept to completion as quickly as possible. It encourages rapid development with a clean and pragmatic design.
- Secure: Security is a key aspect of Django. It has built-in protection against many security threats like SQL injection, cross-site scripting, cross-site request forgery, and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords.
- Scalable: Django uses a component-based "shared-nothing" architecture (each part of the architecture is independent of the others, and each can be replaced or changed independently). This architecture makes it easy to scale an application to handle high levels of traffic.
- Versatile: Django has been used to build all sorts of things—from content management systems to social networks to scientific computing platforms. Its flexibility and versatility make it suitable for almost any project, no matter how big or small.
- Community and Documentation: Django has a vibrant community that provides excellent documentation, which is very helpful for beginners and experts alike. This community also contributes to a large collection of modules and apps available for use in your projects.

More information on Django:

- https://www.djangoproject.com/start/overview/
- https://docs.djangoproject.com/en/4.2/

# Introduction to PythonAnywhere

For the back half of this course, we're going to start connecting all of the database pieces we've been learning to the web. While we've been running code on our local PCs up to this point in the course, to better share our new web-enabled homework and projects, we need to run our code on a server that is accessible from the Internet. One way to do this is to use a cloud-based service like [PythonAnywhere](https://www.pythonanywhere.com/).

[PythonAnywhere](https://www.pythonanywhere.com/) is an online platform that allows you to run Python code in the cloud. It provides an environment where you can write, run, and host Python applications without needing to install Python on your local machine. PythonAnywhere is a great tool for beginners who want to learn Python and Django, as it allows you to focus on writing code without worrying about setting up a development environment. It also can scale up to public-facing websites, so you can use it to host your Django projects. It's also free to use for small projects, so it's a great way to get started with Django.

More information on PythonAnywhere:

- https://help.pythonanywhere.com/
- https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/
- https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

# The Rest of the Course

For the remainder of the course, we'll be building a Django project that will be hosted on PythonAnywhere. We'll be building a database web application based on something that interests you or would be valuable to your current or future employer. We'll be using Django's built-in admin panel to manage the database, and we'll be using Django's ORM to interact with the database. We'll also be using Django's templating system to create the web pages that users will see. We'll be using PythonAnywhere to host the project, so it will be accessible from the Internet. If you have a great idea in mind of a data-backed web application you'd like to build, now is the time to start thinking about it!

# Setting Up PythonAnywhere

- Visit [PythonAnywhere](https://www.pythonanywhere.com/) and create an account.
- Verify your email address to fully activate your account.
- Once you've created an account, you'll be taken to the dashboard.
- Click the "$ Bash" button to fire up a new console. Instead of using the console in VSCode as we have been, you'll use this console to run commands on the PythonAnywhere server.
- I like to run this command (one time) to make the 'ls' command a bit more user-friendly:

```bash
echo "alias ls='ls --color=auto'" >> ~/.bashrc
```

Django has so much built in, that we don't really have many dependencies to install when running it on PythonAnywhere. But we do want to continue using pipenv, so let's install that here similar to how we did on our local machines:

```bash
pip install pipenv
```

# Creating a Django Project

Now that we have PythonAnywhere set up, let's create a Django project. We'll create a new Django project. For this tutorial, we'll create a project called `yummytomatoes`. Your own project should use a different name based on what the project is. To create a new Django project, run the following command:

```bash
mkdir yummytomatoes
cd yummytomatoes
pipenv install django==4.2
pipenv shell
```

The `pipenv install django==4.2` command installs Django 4.2. You can install a different version of Django by changing the version number. The `pipenv shell` command activates the virtual environment. You should see the prompt change to show that you are in the virtual environment, and you should see the **path to the virtual environment** in the prompt. Copy it down, as you'll need it later.

Now, let's create a new Django project called `yummytomatoes`:

```bash
django-admin startproject yummytomatoes .
python manage.py migrate
python manage.py createsuperuser
```

The `django-admin startproject yummytomatoes .` command creates a new Django project called `yummytomatoes`. The `.` at the end of the command tells Django to create the project in the current directory. The `python manage.py migrate` command creates the database tables for the Django project. The `python manage.py createsuperuser` command creates a superuser account that you can use to log in to the Django admin panel. (More to come on that later.)

For the super user account, use `admin` as the username and `adminadmin` as the password. These credentials will be used for checking your homework!

Django projects are created with a directory structure that looks like this:

```bash
yummytomatoes/
    manage.py
    yummytomatoes/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

So much free stuff! Let's see what all of these files do, by joining the official Django tutorial, already in progress, at https://docs.djangoproject.com/en/4.2/intro/tutorial01/.

Well, the next step according to the tutorial is to run **'python manage.py runserver'**, but we can't do that on PythonAnywhere. Instead, we'll need to set up an always-on web app on PythonAnywhere to run our Django project. We'll do that in the next section.

# Adjusting Our Django Settings for PythonAnywhere

Before we set up the web app on PythonAnywhere, we need to make a few changes to our Django project to make it work correctly. Let's use PythonAnywhere's built-in editor to make these changes to the `settings.py` file.

- Find `ALLOWED_HOSTS = []` in the `settings.py` file and update it to include your PythonAnywhere domain. For example, if your PythonAnywhere domain is `seansbox.pythonanywhere.com`, you would update the `ALLOWED_HOSTS` setting like this:

```python
ALLOWED_HOSTS = ['seansbox.pythonanywhere.com']
```

- Next, find your TIME_ZONE setting and update it to your local timezone. For example, if you are in the Pacific time zone, you would update the `TIME_ZONE` setting like this:

```python
TIME_ZONE = 'America/Los_Angeles'
```

- Finally, let Django know where to find the static files and media files. We won't be using these this module, but future us will thank us for having this already setup. Add the following lines to the bottom of the `settings.py` file:

```python
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Alright, not so bad. Django is ready to go on PythonAnywhere. Let's set up the PythonAnywhere web app now.

# Setting Up a Web App on PythonAnywhere

PythonAnywhere allows you to run web apps using a variety of web frameworks, including Django. To set up our Django web app on PythonAnywhere, follow these steps:

- Go to the PythonAnywhere dashboard and click on the "Web" tab.
- Click the "Add a new web app" button.
- Select the "Manual configuration" option and click the "Next" button.
- Select the "Python 3.10" option and click the "Next" button.

Great, so we have a new web app, but it isn't actually connected to our Django project that we built yet. Let's do that now.

- Set the 'code' directory to the path of your Django project. Mine is /home/seansbox/yummytomatoes. Replace your username and folder name as needed.
- Update the 'WSGI configuration file' with the following code, which I stole from [here](https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/). Make sure to change 'mysite' to the name of your Django project. (Mine is 'yummytomatoes'.)

```python
import os
import sys

path = os.path.expanduser('~/mysite')
if path not in sys.path:
sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```

- Set the 'Virtualenv' to the path that you copied down earlier when you activated the virtual environment. It should look something like `/home/seansbox/.virtualenvs/yummytomatoes-uAKj25yN`. Now our Web App knows where our source code is, knows how to serve up our web page with WSGI, and knows where our virtual environment is.

- Add Static files paths for /static/ and /media/. This will allow Django to serve up static files like CSS and images. Click on the 'Static files' section and add your version of the following paths (changing 'seansbox' to your username and 'yummytomatoes' to your project name):

```
URL: /static/   Directory: /home/seansbox/yummytomatoes/static/
URL: /media/    Directory: /home/seansbox/yummytomatoes/media/
```

- Okay, one last step! Enable 'Force HTTPS'. We don't want to be serving up our admin password in plain text.

- Click the 'Reload' button at the top of the page to restart the web app.

- Click the link at the top of the web app to your site. Mine is https://seansbox.pythonanywhere.com/. You should see the Django welcome page with a rocket ship. If you don't see the rocket ship, you may need to check the error logs in the 'Error log' section of the web app.

# Completing the Homework

Now that we have Django running on PythonAnywhere, let's complete the homework.

Create a `hw06` project/folder that contains the following:

- Meets the technical requirements outlined below:
  - Successfully creates a Django project.
  - Successfully adjusts Django settings for PythonAnywhere.
  - Successfully sets up a web app on PythonAnywhere.
  - Successfully runs a web app on PythonAnywhere.
  - Successfully allows access to the Django admin panel using `admin/adminadmin` credentials.
- Leverages pipenv (and a Pipfile) to manage its dependencies.
- Includes a screenshot.jpg of the app successfully running. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)
- Does not directly copy examples from the book or class.

As most of this homework is setting up the environment, the code you write will be minimal. But the setup is important, as we'll be building on this environment for the rest of the course. This bundle will likely only include `screenshot.jpg`. Be sure that your site's URL is visible in the screenshot and accessible from the Internet.

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.
