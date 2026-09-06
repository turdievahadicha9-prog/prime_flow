from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from about.views import about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about_page, name='home'),
    path('api/', include('about.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)