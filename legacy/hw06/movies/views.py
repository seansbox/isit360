from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'movies/index.html', context)

def celebs(request):
    context = {}
    return render(request, 'movies/celebs.html', context)