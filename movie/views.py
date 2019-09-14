from django.shortcuts import render

from .models import Movie


def index(request):
    template = 'movie/index.html'
    context={'index_page':'active'}
    return render(request, template, context)



from django.views.generic import ListView, DetailView

class MovieList(ListView):
    model = Movie
    paginate_by = 6

    

class MovieDetail(DetailView):
    model = Movie
    
