from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('heart_predict/', views.Hpredict, name='heart_predict'),
    path('heart_about/', views.Habout, name='heart_about'),
    path('heart_exercise/', views.Hexercise, name='heart_exercise'),
    path('heart_result/', views.Hresult, name= 'heart_result'),
    path('liver_predict/', views.Lpredict, name='liver_predict'),
    path('liver_about/', views.Labout, name='liver_about'),
    path('liver_exercise/', views.Lexercise, name='liver_exercise'),
    path('liver_result/', views.Lresult, name='liver_result'),
    path('diabetes_predict/', views.Dpredict, name='diabetes_predict'),
    path('diabetes_about/', views.Dabout, name='diabetes_about'),
    path('diabetes_exercise/', views.Dexercise, name='diabetes_exercise'),
   
]
