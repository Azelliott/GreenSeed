from django.shortcuts import render


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'shop/shop.html')
