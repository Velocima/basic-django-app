from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
# Create your views here.

def signup(request):
  if request.method == "POST":
    form_data = UserRegistrationForm(request.POST)
    if form_data.is_valid():
      form_data.save()
      new_user = authenticate(username=form_data.cleaned_data['username'],
                              password=form_data.cleaned_data['password1'],
                              )
      login(request, new_user)
      return redirect('movies-index')
  else:
    form = UserRegistrationForm()
    return render(request, 'users/signup.html', context={'form': form})