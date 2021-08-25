from django.shortcuts import render
from django.http import HttpResponse

movies = [
  {
    "id": 1,
    "title": "The Dark Knight",
    "year_of_release": 2008,
    "genre": "Action"
  },
  {
    "id": 2,
    "title": "The Notebook",
    "year_of_release": 2004,
    "genre": "Romance"
  },
  {
    "id": 3,
    "title": "Pulp Fiction",
    "year_of_release": 1994,
    "genre": "Crime"
  },
]

# Create your views here.
def index(request):
  return render(request, 'movies/index.html')

def show(request, id):
  return HttpResponse('<h1>Hello Movies!</h1>')

def about(request):
  return HttpResponse('<h1>About Movies!</h1>')