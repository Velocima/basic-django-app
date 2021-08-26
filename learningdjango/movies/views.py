from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddGenreForm, AddMovieForm
from .models import Movie

def is_member(user):
    return user.groups.filter(name='Manager').exists()

# Create your views here.
def index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', context={"movies": movies, 'is_manager': is_member(request.user)})

def show(request, id):
  movie = get_object_or_404(Movie, pk=id)
  return render(request, 'movies/movie.html', context={"movie": movie})

def about(request):
  return render(request, 'movies/about.html')

def create(request):
  if not is_member(request.user):
    return HttpResponseForbidden()
  if request.method == 'POST':
    new_movie_data = AddMovieForm(request.POST)
    if new_movie_data.is_valid():
      new_movie = new_movie_data.save()
      return redirect('movies-show', id=new_movie.id)
  else:
    form = AddMovieForm()
    return render(request, 'movies/create.html', context={'form': form})