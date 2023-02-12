from django.urls import path
from reviews import views
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
    path('<int:product_id>/', views.reviews, name='review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
