from django.shortcuts import render

from .models import Movie

def index(request):
    context = {}
    context['movies'] = Movie.objects.order_by('name')
    return render(request, 'movies/index.html', context)

def detail(request, id):
    context = {}
    context['movie'] = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', context)

def celebs(request):
    context = {}
    return render(request, 'movies/celebs.html', context)