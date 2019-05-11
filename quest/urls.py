
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signIn),
    path('postsign/', views.postsign),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('postsignup/', views.postsignup, name='postsignup'),
    path('create/', views.create, name='create')

]
