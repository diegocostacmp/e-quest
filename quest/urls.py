
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name='quest'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),








    # path('', views.signIn, name='inicio'),
    # path('postsign/', views.postsign),
    # path('logout/', views.logout, name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('postsignup/', views.postsignup, name='postsignup')

]
