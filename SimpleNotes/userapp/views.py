from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            user = authenticate(request, email = cleaned['email'], password = cleaned['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('base'))
            else:
                return render(request, 'userapp/login.html', {'form' : LoginForm})
    else:
        return render(request, 'userapp/login.html', {'form' : LoginForm})
                
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'core/index.html', {'just_registered': 1})
        else:
            return render(request, 'userapp/register.html', {'form': RegisterForm})
    else:
        return render(request, 'userapp/register.html', {'form': RegisterForm})
