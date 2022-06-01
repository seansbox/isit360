from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),
    path('add/', views.MovieCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.MovieUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.MovieDeleteView.as_view(), name='delete'),
]