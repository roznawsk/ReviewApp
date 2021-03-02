from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from . import models


def index(request):
    return HttpResponse("Hello, world. You're at the ReviewApp")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'courses/signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # redirect('login')
            pass
    return render(request, 'courses/login.html')


def home(request):
    current_user = request.user
    sections = models.Section.objects.filter(user=current_user)
    # if type(sections) != list:
    #     sections = [sections]
    sections = [str(s) for s in sections]
    print(sections)
    return render(request, 'courses/home.html', {'sections': sections})
