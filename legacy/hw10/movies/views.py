from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Movie

class MovieListView(ListView):
    model = Movie

class MovieDetailView(DetailView):
    model = Movie

class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'release', 'thumb', 'summary', 'meter', 'score']

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['name', 'release', 'thumb', 'summary', 'meter', 'score']

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies:index')