from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = "movies"

urlpatterns = [
    # Empty (root) path goes to the index view
    path("about", views.about, name="about"),
    path("", views.MovieListView.as_view(), name="home"),
    path("add", permission_required("movies.add_movie")(views.MovieCreateView.as_view()), name="create"),
    path("<int:pk>", views.MovieDetailView.as_view(), name="detail"),
    path("<int:pk>/update", permission_required("movies.change_movie")(views.MovieUpdateView.as_view()), name="update"),
    path("<int:pk>/delete", permission_required("movies.delete_movie")(views.MovieDeleteView.as_view()), name="delete"),
]
