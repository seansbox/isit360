from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages

class FrontView(TemplateView):
    template_name = "common/front.html"

class HelpView(TemplateView):
    template_name = "common/help.html"

class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'common/login.html'
    next_page = '/'
    success_message = "You have been successfully logged in!"

class LogoutView(LogoutView):
    next_page = '/'

def show_message(sender, user, request, **kwargs):
    messages.success(request, 'You have been successfully logged out!')

user_logged_out.connect(show_message)