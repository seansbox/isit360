from django.urls import path

from . import views

urlpatterns = [
    # Empty (root) path goes to the index view
    path("", views.MovieListView.as_view(), name="home"),
    path("about", views.about, name="about"),
]