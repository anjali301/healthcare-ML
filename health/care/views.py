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

def faq(request):
    return render(request, 'faq.html')

def Hpredict(request):
    return render(request, 'heart/Hpredict.html')

def Habout(request):
    return render(request, 'heart/Habout.html')

def Hexercise(request):
    return render(request, 'heart/Hexercise.html')

def Ppredict(request):
    return render(request, 'parkinson/Ppredict.html')

def Pabout(request):
    return render(request, 'parkinson/Pabout.html')

def Pexercise(request):
    return render(request, 'parkinson/Pexercise.html')

def Dpredict(request):
    return render(request, 'diabetes/Dpredict.html')

def Dabout(request):
    return render(request, 'diabetes/Dabout.html')

def Dexercise(request):
    return render(request, 'diabetes/Dexercise.html')




