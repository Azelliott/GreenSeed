from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from checkout.models import Order


@login_required
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


@login_required
def order_history(request, order_number):
    """ A view to return the order history page """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
