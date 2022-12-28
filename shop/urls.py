from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('shop-products/', views.shop_products, name='shop-products'),
]
