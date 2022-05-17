from django.http import Http404
from django.shortcuts import render

from .models import Movie

def index(request):
    context = {}
    context['movies'] = Movie.objects.order_by('name')
    return render(request, 'movies/index.html', context)

def detail(request, id):
    context = {}
    try:
        context['movie'] = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/detail.html', context)

def celebs(request):
    context = {}
    return render(request, 'movies/celebs.html', context)