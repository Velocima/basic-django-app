from .models import Genre, Movie
from django import forms

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year_of_release', 'genre']