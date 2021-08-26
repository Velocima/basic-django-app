from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Movie


# Create your views here.
def index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', context={"movies": movies})

def show(request, id):
  movie = get_object_or_404(Movie, pk=id)
  return render(request, 'movies/movie.html', context={"movie": movie})

def about(request):
  return render(request, 'movies/about.html')