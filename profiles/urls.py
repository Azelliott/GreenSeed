from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_account, name='my_account'),
]