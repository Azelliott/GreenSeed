from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile


def my_account(request):
    """ A view to return the profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/my_account.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
