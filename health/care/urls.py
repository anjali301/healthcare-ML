from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('heart/', views.heart, name='heart'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('parkinson/', views.parkinson, name='parkinson'),
]
