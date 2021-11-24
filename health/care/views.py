from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np
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

def Hresult(request):

    heart = joblib.load('heart.sav')
    val = []
    
    val.append(request.GET['age'])
    val.append(request.GET['gender'])
    val.append(request.GET['cp'])
    val.append(request.GET['restbp'])
    val.append(request.GET['chol'])
    val.append(request.GET['fbs'])
    val.append(request.GET['max_heart'])
    val.append(request.GET['vessels'])
    val.append(request.GET['thal'])
    print(val)
    # val = np.asarray(val)
    # val = val.reshape(1, -1)
    # print(val)
    ans = heart.predict([val])
    res = []
    if ans[0] == 0:
        res.append("Don't worry! You're healthy!")
    elif ans[0] == 1:
        res.append("Uh oh! Seems like you're suffering from Heart disease :(")
    return render(request, 'heart/Hresult.html', {'ans': res[0]})

def Lpredict(request):
    return render(request, 'liver/Lpredict.html')

def Labout(request):
    return render(request, 'liver/Labout.html')

def Lexercise(request):
    return render(request, 'liver/Lexercise.html')

def Lresult(request):
    liv = joblib.load('liver.sav')
    val = []

    val.append(request.GET['age'])
    val.append(request.GET['gender'])
    val.append(request.GET['tot_bil'])
    val.append(request.GET['dir_bil'])
    val.append(request.GET['alk_phos'])
    val.append(request.GET['sgpt'])
    val.append(request.GET['sgot'])
    val.append(request.GET['tot_prot'])
    val.append(request.GET['albumin'])
    val.append(request.GET['alb_glob_ratio'])
    print(val)
    # val = np.asarray(val)
    # val = val.reshape(1, -1)
    # print(val)
    ans = liv.predict([val])
    res = []
    if ans[0] == 0:
        res.append("Don't worry! You're healthy!")
    elif ans[0] == 1:
        res.append("Uh oh! Seems like you're suffering from Liver disease :(")
    return render(request, 'liver/Lresult.html', {'ans': res[0]})

def Dpredict(request):
    return render(request, 'diabetes/Dpredict.html')

def Dabout(request):
    return render(request, 'diabetes/Dabout.html')

def Dexercise(request):
    return render(request, 'diabetes/Dexercise.html')

def Dresult(request):

    diabetes = joblib.load('diabetes.sav')

    lis = []

    lis.append(request.GET['Pregnancies'])
    lis.append(request.GET['Glucose'])
    lis.append(request.GET['BloodPressure'])
    lis.append(request.GET['SkinThickness'])
    lis.append(request.GET['Insulin'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['DiabetesPedigreeFunction'])
    lis.append(request.GET['Age'])
    print(lis)

    # lis_arr = np.asarray(lis)
    # lis1 = lis_arr.reshape(1, -1)
    final = diabetes.predict([lis])
    res = []
    if final[0] == 0:
        res.append("Don't worry! You're healthy!")
    elif final[0] == 1:
        res.append("Uh oh! Seems like you're suffering from Diabetes :(")
    return render(request, 'diabetes/Dresult.html', {'ans': res[0]})