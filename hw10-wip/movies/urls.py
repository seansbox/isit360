from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

app_name = 'movies'
urlpatterns = [
    path('', login_required()(views.MovieListView.as_view()), name='index'),
    path('add/', permission_required('movies.create_movie')(views.MovieCreateView.as_view()), name='create'),
    path('<int:pk>/', permission_required('movies.view_movie')(views.MovieDetailView.as_view()), name='detail'),
    path('<int:pk>/update', permission_required('movies.change_movie')(views.MovieUpdateView.as_view()), name='update'),
    path('<int:pk>/delete', permission_required('movies.delete_movie')(views.MovieDeleteView.as_view()), name='delete'),
]