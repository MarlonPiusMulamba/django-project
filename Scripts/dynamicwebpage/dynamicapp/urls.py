import os
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import dynamic_page

urlpatterns = [
    path('', dynamic_page, name='dynamic_page'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/hongo_image'
