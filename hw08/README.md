# HW08 Models and Admin

_Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion._

## Objectives

- Understand Django models and their role in database schema definition.
- Utilize Django’s admin site to manage application data.
- Modify our custom home page for our Django application.
- Implement generic views to simplify common web development tasks.

## Introduction to Django Models

[Django Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models) are a powerful way to define the structure of your database. Remember SQLAlchemy? Well Django has an ORM builtin as well, and honestly, I think it's a little easier to use than SQLAlchemy was, but very similar. Each Python model/class maps to a single database table and allows us to define the fields and behaviors of the data we store. Models are defined as Python classes and use Django’s ORM to automatically create the database schema for us!

Key Concepts:

- **Defining Models**: Create classes that inherit from `models.Model`.
- **Model Fields**: Define fields like `CharField`, `DateField`, `ForeignKey`, etc.
- **Meta Class**: Customize model behavior using the `Meta` class.
- **Model Methods**: Add custom methods to models for specific behaviors.

## Introduction to Django Admin Site

[Django Admin Site](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site) is a powerful built-in Django tool that provides an interface for managing our application data. Remember sqlite_web? Or using SQLite's command-line interface? Well, once again Django has us covered, and it's wonderful. The automatic admin site allows us to create, read, update, and delete records in our database through a web interface without having to write any additional code!

Key Concepts:

- **Registering Models**: Make models available in the admin site using `admin.site.register()`.
- **Customizing Admin Interface**: Modify how models are displayed and interacted with in the admin interface.
- **Admin Classes**: Create admin classes to specify configurations like list display, search fields, and filtering options.

## Introduction to Django Home Page

[Django Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page) allow us to create custom pages for our web application. This involves defining a view, creating a URL route, and rendering an HTML template. We did this last module, and now we're going to do it a couple more times, but this time, we'll connect these pages to our data!

Key Concepts:

- **Defining Views**: Use Django’s `views.py` to create functions or classes that handle requests.
- **URL Configuration**: Map URLs to views in `urls.py`.
- **Templates**: Create HTML templates to define the layout and design of your home page.

## Introduction to Django Generic Views

[Django Generic Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views) are predefined views that handle common patterns like displaying a list of objects, handling forms, and displaying object details. Sometimes we find ourselves especially in larger sites writing the same boilerplate code again and again. Generic Views help reduce the amount of code we need to write for standard tasks.

Key Concepts:

- **ListView**: Display a list of objects.
- **DetailView**: Display details of a single object.
- **CreateView, UpdateView, DeleteView**: Handle forms for creating, updating, and deleting objects.
- **Customizing Generic Views**: Override methods and attributes to customize behavior.

## Updating Our Project

1. **Define Models**: Add models to your application.
2. **Register Models with Admin Site**: Make your models accessible in the admin interface.
3. **Create Pages**: Define a view, URL, and template for your home page.
4. **Use Generic Views**: Implement generic views for common patterns.

### Example Steps

1. **Create Models**: _(example of models.py in our Django application)_

   ```python
   from django.db import models

   class Author(models.Model):
       name = models.CharField(max_length=200)
       birth_date = models.DateField()

       def __str__(self):
           return self.name

   class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.ForeignKey(Author, on_delete=models.CASCADE)
       publish_date = models.DateField()

       def __str__(self):
           return self.title
   ```

2. **Register Models**: _(example of admin.py in our Django application)_

   ```python
   from django.contrib import admin
   from .models import Author, Book

   admin.site.register(Author)
   admin.site.register(Book)
   ```

3. **Create Home Page View**: _(example of views.py in our Django application)_

   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')
   ```

4. **URL Configuration**: _(example of a urls.py in our Django project)_

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
   ```

5. **Home Page Template**: _(example of a templates/(appname)/home.html in our Django application)_

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Home Page</title>
     </head>
     <body>
       <h1>Welcome to My Django Site</h1>
     </body>
   </html>
   ```

6. **Using Generic Views**: _(updated/expanded example of views.py and urls.py in our Django application)_

   ```python
   from django.views.generic import ListView, DetailView
   from .models import Book

   class BookListView(ListView):
       model = Book
       template_name = 'book_list.html'

   class BookDetailView(DetailView):
       model = Book
       template_name = 'book_detail.html'
   ```

   ```python
   from django.urls import path
   from .views import BookListView, BookDetailView

   urlpatterns = [
       path('books/', BookListView.as_view(), name='book-list'),
       path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
   ]
   ```

## Completing the Homework

Updates your PythonAnywhere project to contain the following:

- Meets the technical requirements outlined below:

  - Defines at least two models with relationships.
  - Registers models with the admin site.
  - Creates a custom home page which includes visibility to the data.
  - Implements at least one generic view.

- Leverages pipenv (and a Pipfile) to manage its dependencies.
- Includes a screenshot.jpg of the website successfully running. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)
- Does not directly copy examples from the book or class.

Be sure that your site's URL is visible in the screenshot and accessible from the Internet.

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.
