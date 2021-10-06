from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def nav(request):
    return render(request, 'nav.html')

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def heart(request):
    return render(request, 'heart/heart.html')

def diabetes(request):
    return render(request, 'diabetes/diabetes.html')

def parkinson(request):
    return render(request, 'parkinson/parkinson.html')