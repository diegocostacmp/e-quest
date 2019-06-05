from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# redireciomanento para os apps
urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path('admin/', admin.site.urls)

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
