from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.expressions import F

# Create your models here.
class Genre(models.Model):
  genre = models.CharField(primary_key=True, max_length=50)

  def __str__(self):
      return self.genre

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year_of_release = models.PositiveIntegerField(validators=[MinValueValidator(1880), MaxValueValidator(2121)])
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  def __str__(self):
      return f'{self.title} - {self.genre}'
  