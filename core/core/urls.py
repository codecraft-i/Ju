from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the urls from the backend app
    path('', include('backend.urls')),
    path('', include('Bot.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)