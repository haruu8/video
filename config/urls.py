from django.contrib import admin
from django.urls import include, path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('movies.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
