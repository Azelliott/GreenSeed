from django.shortcuts import render
from datetime import date
from .forms import ContactForm
from django.contrib import messages


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


# Contact form view, using the ContactForm model from forms.py
# after the form is submitted, form is cleared and success message is displayed
def contact(request):
    '''A view to return the contact page'''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent!')
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def shop(request):
    '''A view to return the shop page'''
    return render(request, 'home/shop.html')

