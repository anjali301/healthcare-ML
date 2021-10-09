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

def Lpredict(request):
    return render(request, 'liver/Lpredict.html')

def Labout(request):
    return render(request, 'liver/Labout.html')

def Lexercise(request):
    return render(request, 'liver/Lexercise.html')

def Dpredict(request):
    return render(request, 'diabetes/Dpredict.html')

def Dabout(request):
    return render(request, 'diabetes/Dabout.html')

def Dexercise(request):
    return render(request, 'diabetes/Dexercise.html')




