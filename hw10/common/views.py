from django.shortcuts import render

def front(request):
    context = {}
    return render(request, 'common/front.html', context)

def help(request):
    context = {}
    return render(request, 'common/help.html', context)
