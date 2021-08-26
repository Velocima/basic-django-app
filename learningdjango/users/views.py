from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
# Create your views here.

def signup(request):
  if request.method == "POST":
    new_user = UserRegistrationForm(request.POST)
    if new_user.is_valid():
      new_user.save()
      return redirect('movies-index')
  else:
    form = UserRegistrationForm()
    return render(request, 'users/signup.html', context={'form': form})