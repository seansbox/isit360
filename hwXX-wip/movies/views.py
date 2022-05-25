from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Movie

class MovieListView(ListView):
    queryset = Movie.objects.order_by('name')
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie

class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'release', 'thumb', 'summary', 'meter', 'score']
    success_url = reverse_lazy('movies:index')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['name', 'release', 'thumb', 'summary', 'meter', 'score']
    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'pk': self.object.pk})

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies:index')

@login_required
def detail(request, id):
    context = {}
    context['movie'] = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = MovieForm()

    return render(request, 'name.html', {'form': form})


    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    context = {}
    context['movie'] = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', context)

def celebs(request):
    context = {}
    return render(request, 'movies/celebs.html', context)