from django.shortcuts import render

# Create your views here.
def index(request):
    '''A view to return the index page'''
    return render(request, 'home/index.html')

def plants(request):
    '''A view to return the plants page'''
    return render(request, 'home/plants.html')

def about(request):
    '''A view to return the about page'''
    return render(request, 'home/about.html')