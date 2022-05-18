from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('celebs/', views.celebs, name='celebs'),
    path('<int:id>/', views.detail, name='detail'),
]