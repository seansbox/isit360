from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Movie

# def index(request):
#    context = {}
#    context['movies'] = Movie.objects.order_by('-meter', 'name')[:20]
#    return render(request, 'movies/index.html', context)


class MovieCreateView(CreateView):
    model = Movie
    fields = ["name", "release", "thumb", "summary", "meter", "score"]


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["name", "release", "thumb", "summary", "meter", "score"]


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = "/"


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie


def about(request):
    context = {}
    return render(request, "movies/about.html", context)


# GENERIC: project/urls.py >>> app/urls.py >>> app/views.py >>> app/templates/app/index.html
# ME: yummytomatoes/urls.py >>> movies/urls.py >>> movies/views.py >>> movies/templates/movies/index.html
