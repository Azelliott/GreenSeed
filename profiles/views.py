from django.shortcuts import render


def my_account(request):
    """ A view to return the profile page """

    template = 'profiles/my_account.html'
    context = {}

    return render(request, template, context)
