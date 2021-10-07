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
    path('parkinson_predict/', views.Ppredict, name='parkinson_predict'),
    path('parkinson_about/', views.Pabout, name='parkinson_about'),
    path('parkinson_exercise/', views.Pexercise, name='parkinson_exercise'),
    path('diabetes_predict/', views.Dpredict, name='diabetes_predict'),
    path('diabetes_about/', views.Dabout, name='diabetes_about'),
    path('diabetes_exercise/', views.Dexercise, name='diabetes_exercise'),
   
]
