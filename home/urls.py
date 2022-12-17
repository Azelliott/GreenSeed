from django.urls import path
from home import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import homeSitemap

sitemaps = {
    'home': homeSitemap,
}

urlpatterns = [
    path('', views.index, name='home'),
    path('plants/', views.plants, name='plants'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': {'home': homeSitemap}}),
    path('signup/', views.signup, name='signup'),
    ]

handler404 = 'home.views.handler404'
