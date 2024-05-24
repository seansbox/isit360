# HW09 Users and Forms

_Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion._

## Objectives

- Understand and implement Django sessions to track user state.
- Utilize Django’s authentication system to manage user accounts and permissions.
- Create and handle forms in Django for user input.

## Introduction to Django Sessions

[Django Sessions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions) allow you to store and retrieve arbitrary data on a per-site-visitor basis. They help you track the state of a user's interaction with your site across multiple requests. This is complex code to write ourselves, so once again having this functionality built into Django in a flexible way is a huge time-saver.

Key Concepts:

- **Session Middleware**: Middleware that enables session support in Django.
- **Session Data**: Store and access session data using the `request.session` dictionary.
- **Session Expiry**: Manage the duration for which session data is stored.

## Introduction to Django Authentication

[Django Authentication](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) provides a comprehensive framework for managing user accounts, groups, permissions, and cookie-based user sessions.

Key Concepts:

- **User Model**: Django’s built-in `User` model for managing user data.
- **Authentication Views**: Predefined views for login, logout, and password management.
- **Permissions**: Use permissions to control user access to different parts of your application.

## Introduction to Django Forms

[Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms) provide a powerful way to handle user input. They abstract the process of rendering HTML forms and validating user input. It's great to build a website that can view our data, but far greater is a website where users have permission to alter the data!

Key Concepts:

- **Form Classes**: Create forms using Django's `forms` module.
- **Form Handling**: Process form data and perform validation.
- **Model Forms**: Create forms directly from Django models to automate form creation.

## Updating Our Project

1. **Implement Sessions**: Enable and use session middleware to track user state.
2. **Set Up Authentication**: Integrate Django’s authentication system to manage user accounts.
3. **Create and Handle Forms**: Use Django forms to collect and validate user input.

### Example Steps

1. **Enable Sessions**: _(example of settings.py in our Django application)_

   ```python
   MIDDLEWARE = [
       ...
       'django.contrib.sessions.middleware.SessionMiddleware',
       ...
   ]

   INSTALLED_APPS = [
       ...
       'django.contrib.sessions',
       ...
   ]
   ```

2. **Using Sessions**: _(example of views.py in our Django application)_

   ```python
   from django.shortcuts import render

   def my_view(request):
       num_visits = request.session.get('num_visits', 0)
       request.session['num_visits'] = num_visits + 1
       return render(request, 'my_template.html', {'num_visits': num_visits})
   ```

3. **Set Up Authentication**: _(example of settings.py and urls.py in our Django application)_

   ```python
   INSTALLED_APPS = [
       ...
       'django.contrib.auth',
       'django.contrib.contenttypes',
       ...
   ]

   AUTHENTICATION_BACKENDS = (
       'django.contrib.auth.backends.ModelBackend',
   )
   ```

   ```python
   from django.urls import path
   from django.contrib.auth import views as auth_views

   urlpatterns = [
       ...
       path('login/', auth_views.LoginView.as_view(), name='login'),
       path('logout/', auth_views.LogoutView.as_view(), name='logout'),
       ...
   ]
   ```

4. **Creating Forms**: _(example of forms.py in our Django application)_

   ```python
   from django import forms

   class MyForm(forms.Form):
       name = forms.CharField(label='Your name', max_length=100)
       email = forms.EmailField(label='Your email')
   ```

5. **Handling Forms**: _(example of views.py and template in our Django application)_

   ```python
   from django.shortcuts import render
   from .forms import MyForm

   def my_form_view(request):
       if request.method == 'POST':
           form = MyForm(request.POST)
           if form.is_valid():
               # Process the data in form.cleaned_data
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               # Redirect or render a success page
       else:
           form = MyForm()

       return render(request, 'my_form_template.html', {'form': form})
   ```

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Form Page</title>
     </head>
     <body>
       <h1>Submit Your Info</h1>
       <form method="post">
         {% csrf_token %} {{ form.as_p }}
         <button type="submit">Submit</button>
       </form>
     </body>
   </html>
   ```

## Completing the Homework

Updates your PythonAnywhere project to contain the following:

- Meets the technical requirements outlined below:

  - Implements Django sessions to track user state.
  - Integrates Django’s authentication system to manage user accounts.
  - Creates and handles at least one form to collect user input and update your data.

- Leverages pipenv (and a Pipfile) to manage its dependencies.
- Includes a screenshot.jpg of the website successfully running. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)
- Does not directly copy examples from the book or class.

Be sure that your site's URL is visible in the screenshot and accessible from the Internet.

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.
