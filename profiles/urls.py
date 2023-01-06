from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_account, name='my_account'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]