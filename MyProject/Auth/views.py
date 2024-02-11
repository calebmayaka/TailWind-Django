from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
    return render(request, 'Auth/landing.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signout(request):
    pass

def homepage(request):
    return render(request, 'homepage.html')

