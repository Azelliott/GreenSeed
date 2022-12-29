from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('shop-products/<slug:category_slug>/', views.shop_products,
         name='shop-products'),
]
