from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<product_id>/', views.edit_product, name='edit_product'),
]
