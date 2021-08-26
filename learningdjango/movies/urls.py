from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='movies-index'),
  path('<int:id>/', views.show, name='movies-show'),
  path('about/', views.about, name='movies-about'),
  path('new/', views.create, name='movies-new')
]