from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('plants/', views.plants, name='plants'),
    path('about/', views.about, name='about'),
]
