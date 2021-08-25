from django.shortcuts import render
from django.http import HttpResponse

movies = []

# Create your views here.
def index(request):
  return render(request, 'movies/index.html')

def show(request, id):
  return HttpResponse('<h1>Hello Movies!</h1>')

def about(request):
  return HttpResponse('<h1>About Movies!</h1>')