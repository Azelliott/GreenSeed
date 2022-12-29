from django.urls import path
from shop import views
from django.contrib.staticfiles.urls import static
from django.conf import settings




urlpatterns = [
    path('', views.shop, name='shop'),
    path('shop-products/<slug:category_slug>/', views.shop_products,
         name='shop-products'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
