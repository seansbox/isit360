# HW07 Views and Templates

# Objectives

- Understand the components and architecture of Django.
- Create a basic Django application.
- Create some static web pages.
- Make it look nice.

# Introduction

Read through https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction. This will give you another good overview of what Django is and how it works. Perhaps the most important thing I'd like you to understand at this time, is the basic flow of the Django request and response approach:

![](basic-django.png)

When a user requests a page from our site, Django will look at the URL and match it to a pattern in _urls.py_. This will then call a _view_ function, which will return a _response_ to the user. This response can be a simple string, or it can be a _template_ that is rendered by Django. Many times, the view will also need to interact with a _model_ to get data to display in the template and return to the user. This is the fundamental flow of a Django application.

Read through https://docs.djangoproject.com/en/4.2/intro/tutorial03/ and https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website. Try to understand the gist of Django's _application_ architecture and how it works with _views_ to provide _templates_ to the user. Then, follow the steps below on your current project.

# Creating a Django Application

Let's get back to our PythonAnywhere console. We're going to create a new Django _application_ for our existing django _project_. It should look something like this:

```bash
cd yummytomatoes
pipenv shell
python manage.py startapp movies
```

Remember, _my_ project is called _yummytomatoes_, and I'm going to create a new application for it called _movies_, since that is the main focus of my project: a movies website that shows my top movie recommendations: the Yummy Tomatoes! Your project should have a different name, and your application should too.

The _startapp_ command above will create a new directory called _movies_ in our project. This is where we will put all of our _views_ and _models_ for our movies application. We will also need to add this new application to our _INSTALLED_APPS_ in _settings.py_. We can use PythonAnywhere's "Files" editor to do this. Open the file _yummytomatoes/settings.py_ and add _movies_ to the _INSTALLED_APPS_ list. Again, your project and application names will be different, but the process is the same.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our new application
    'movies',
```

Go the Web function of PythonAnywhere and reload your web app. Then refresh your web browser pointed at _your_ version of https://seansbox.pythonanywhere.com/ and make sure that rocket page still shows up! We've built and installed a new application in our project, but we haven't actually made it do anything yet.

# Creating Our First Page

So we want to make a web page, right? Well here is what we need to do:

1. Create a _view_ function in our _movies_ application.
2. Create a _URL pattern_ in our _movies_ application that will call this _view_ function.
3. Create a _template_ in our _movies_ application that will be rendered by the _view_ function.
4. Create a _URL pattern_ in our project's _urls.py_ file that will call the _URL pattern_ in our _movies_ application.

WHAT IS ALL THAT?! Let's break it down.

## 1. Create a _view_ function in our _movies_ application.

As we read in the Django documentation, a _view_ is a Python function that takes a web request and returns a web response. We need to create a view for our new _movies_ application. We can do this by editing the _views.py_ in the _movies_ directory. This file will contain all of our view functions for our movies application.

### movies/views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'movies/index.html', context)
```

What is this?! We're using the _render_ function from Django's _shortcuts_ module to return a _template_ called _index.html_! We haven't created this html template yet, but we will in a moment. This is the basic structure of a Django view function. It takes a _request_ object and returns a _response_ object. In this case, the response is from a template called _index.html_.

## 2. Create a _URL pattern_ in our _movies_ application

We need to create a _URL pattern_ in our _movies_ application that will call this _index_ view function. We can do this by editing the _urls.py_ file in the _movies_ directory. Oddly enough, Django doesn't automatically make this file for us so we have to create it. This file will contain all of our URL patterns for our movies application.

### movies/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    # Empty (root) path goes to the index view
    path('', views.index, name='index'),
]
```

Okay, so what's going on here? We're importing the _path_ function from Django's _urls_ module, and we're importing that _index_ function from our _views.py_ file. We're then creating a _URL pattern_ that will call our _index_ view function when the user requests the root URL of our movies application. This is the basic structure of a Django URL pattern. There is quite a bit of boilerplate code here, but it's all necessary to make Django work. And it won't change much from application to application. We'll do this over and over again.

## 3. Create a _template_ in our _movies_ application.

We need to create an html _template_ in our _movies_ application that will be rendered by that _index_ view function of ours. We can do this by creating a new directory called _templates_ in the _movies_ directory. This is where we will put all of our _html_ templates for our movies application. We will also need to add this new directory to our _TEMPLATES_ in _settings.py_. We can use PythonAnywhere's "Files" editor to do this. Open the file _yummytomatoes/settings.py_ and add _movies_ to the _DIRS_ list in the _TEMPLATES_ dictionary. Again, your project and application names will be different, but the process is the same.

````python

### movies/templates/movies/index.html

```html
Hello, world!
````

Ugh, what an ugly template! But it's a start. We'll make it look better in a moment. For now, let's just make sure it works.

## 4. Create a _URL pattern_ in our project's _urls.py_ file

One last plumbing bit. We need to create a _URL pattern_ in our project's _urls.py_ file that will call the _URL pattern_ in our _movies_ application. We can do this by editing the _urls.py_ file in the _yummytomatoes_ (project) directory. This file will contain all of our URL patterns for our project. No matter how many applications we have in our project, we will always have this main _urls.py_ file in our project directory.

### yummytomatoes/urls.py

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("movies.urls")),
    path("admin/", admin.site.urls),
]
```

What is this _include_ function? It's a way to include another _urls.py_ file in our main _urls.py_ file. This is how we can have multiple applications in our project. We can have a _urls.py_ file for each application, and then include them all in our main _urls.py_ file. This is the basic structure of a Django _urls.py_ file. We will do this over and over again.

So we're telling our project/website that the empty/root URL should go to the _index_ view function in our _movies_ application. We're also telling our project/website that the _admin/_ URL should go to the Django admin interface. This is the basic structure of a Django project _urls.py_ file. We will do this over and over again.

## Test it out!

Go to the Web function of PythonAnywhere and reload your web app. Then refresh your web browser pointed at _your_ version of https://seansbox.pythonanywhere.com/ and you should see the text "Hello, world!" on the page. You've just created your first Django web page! It's not much, but it's a start. We'll make it look better in a moment.

# Making It Look Nice

Django doesn't have an opinion about the style of our web pages. It's up to us to make them look nice. You're welcome to use any CSS framework you like, or you can write your own CSS. But I'm going to show you _fully lazy_ mode by leveraging another library: _Bootstrap_.

```bash
pipenv install django-bootstrap5
```

We're going to use this [django-bootstrap5](https://github.com/zostera/django-bootstrap5) module to make our site look nice. We'll also need to add it to the end of our _INSTALLED_APPS_ in _settings.py_.

```python
INSTALLED_APPS = (
    ...
    "movies",
    "django-bootstrap5",
)
```

We need to reload the web app in PythonAnywhere and refresh the page in our web browser. Did we break anything? No? Good. Now our html templates have new super powers. Let's update our _index.html_ template to look nice now!

### movies/templates/movies/index.html

```django-html
{% extends 'movies/base.html' %}
{% block title %}Hello, world!{% endblock %}
{% block content %}This site is coming soon!{% endblock %}
```

Wait, what? We're using _extends_ and _block_? What is this magic? This is Django's template inheritance that we read about. We're extending a _base.html_ template (which we'll make in a second) and we're overriding the _title_ and _content_ blocks. Let's create the base template now.

### movies/templates/movies/base.html

```django-html
{% extends 'django_bootstrap5/bootstrap5.html' %}
{% load django_bootstrap5 %}
{% block bootstrap5_content %}

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/darkly/bootstrap.min.css" />

<nav class="navbar navbar-expand-lg fixed-top bg-primary" data-bs-theme="dark">
  <div class="container">
    <a class="navbar-brand" href="/">Yummy Tomatoes</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarResponsive"
      aria-controls="navbarResponsive"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<br /><br /><br /><br />
<div class="container">
  <h1>{% block bootstrap5_title %}{% block title %}(no title){% endblock %}{% endblock %}</h1>

  {% autoescape off %}{% bootstrap_messages %}{% endautoescape %}

  {% block content %}(no content){% endblock %}
</div>

{% endblock %}
```

What is all this? We're extending the _bootstrap5.html_ template from _django-bootstrap5_ and we're overriding the _bootstrap5_content_ block. We're then adding a _navbar_ and a _container_ to our _base.html_ template. This is how we can create a consistent look and feel across all of our web pages. We can have a _base.html_ template that contains all of our common elements, and then we can extend that template in our other templates. This is the basic structure of a Django template. Bootstrap is a CSS framework that makes it easy to create nice looking web pages. We can use it to make our site look nice with very little effort, other than a little bit of copy and paste.

Refresh our web app, refresh our browser, and our new hello world page should be looking lovely!

Oh, I snuck in an extra line in the base.html: that link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/darkly/bootstrap.min.css" bit. This is a link to a _bootswatch_ theme called _darkly_. It's a dark theme that makes our site look a little more interesting. You can change this to any other bootswatch theme you like. Check out https://bootswatch.com/ for more themes. Change this line to any other theme you like, and refresh your web app and browser to see the changes.

# Completing the Homework

Now that we have Django running on PythonAnywhere, let's complete the homework.

Create a `hw07` project/folder that contains the following:

- Meets the technical requirements outlined below:
  - Successfully leverages a Django application and Boostrap library to display a stylish web page.
- Leverages pipenv (and a Pipfile) to manage its dependencies.
- Includes a screenshot.jpg of the website successfully running. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)
- Does not directly copy examples from the book or class.

This bundle will likely only include `screenshot.jpg`. Be sure that your site's URL is visible in the screenshot and accessible from the Internet.

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.
