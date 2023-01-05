from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm

from .models import UserProfile


def my_account(request):
    """ A view to return the profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
        else:
            messages.error(request, 'Update failed. Please check your form.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/my_account.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
