from django.urls import path

from . import views

urlpatterns = [
    # Empty (root) path goes to the index view
    path("", views.index, name="index"),
]
