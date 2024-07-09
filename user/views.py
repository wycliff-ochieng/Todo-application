from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from .import forms
from . forms import UserCreationForm, LoginForm

def homepage(request):
    return render(request, 'user/home.html')


def loginPage(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    context = {'form':form}

    return render(request, 'user/login.html', context)


def register(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form':form}

    return render(request, 'user/register.html', context)


def dashboard(request):
    return render(request, 'user/dashboard.html')
