from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('', views.front, name='front'),
    path('help/', views.help, name='help'),
]