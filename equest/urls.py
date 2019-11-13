from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('quiz/', include('apps.quiz.urls', namespace='quiz')),
    path('game/', include('apps.game.urls', namespace='game')),

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
