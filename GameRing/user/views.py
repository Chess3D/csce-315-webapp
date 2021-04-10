from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login(request):
    return render(request, 'user/login.html')

def home(request):
    return render(request, 'user/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message.success(request, f'Account created for user {username}')
            return redirect('user/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'user/SignUp.html', {'form': form})


