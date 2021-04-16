from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def login(request):
    return render(request, 'user/login.html')


def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'user/SignUp.html', {'form': form})
