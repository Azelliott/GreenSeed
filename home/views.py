from django.shortcuts import render
from datetime import date
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# Index page
def index(request):
    '''A view to return the index page'''
    return render(request, 'home/index.html')

# Our plants page
def plants(request):
    '''A view to return the plants page'''
    return render(request, 'home/plants.html')

# About Us page
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


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'home/shop.html')


# Robots.txt view
@require_GET
def robots_txt(request):
    '''A view to return the robots.txt file'''
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


# Custom 404 page
def handler404(request, exception):
    return render(request, 'home/404.html', status=404)