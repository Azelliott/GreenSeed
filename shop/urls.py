from django.urls import path
from shop import views
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
    path('', views.shop, name='shop'),
    path('shop-products/<slug:category_slug>/', views.shop_products,
         name='shop-products'),
    path('shop-products/<slug:category_slug>/<str:search_query>/',
         views.shop_products, name='shop-products'),
    path('product-details/<int:product_id>/', views.product_details,
         name='product-details'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-item/<int:product_id>/', views.add_item, name='add_item'),
    path('cart/remove/', views.remove_item, name='remove_item'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
