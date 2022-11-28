from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('plants/', views.plants, name='plants'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

handler404 = 'home.views.handler404'