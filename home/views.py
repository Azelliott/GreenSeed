from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    '''A view to return the index page'''
    return render(request, 'home/index.html')

def plants(request):
    '''A view to return the plants page'''
    return render(request, 'home/plants.html')

def about(request):
    '''A view to return the about page'''
    current_year = date.today().year
    years = current_year - 2012
    return render(request, 'home/about.html', {'years': years})

def contact(request):
    '''A view to return the contact page'''
    return render(request, 'home/contact.html')