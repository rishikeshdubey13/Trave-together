from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your views here.

def home(request):
    return render(request,'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password =password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
        
    else:
        return render(request , 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request,'register.html', {'form' : form})