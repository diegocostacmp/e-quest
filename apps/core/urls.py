from django.urls import path
from .views import signIn

urlpatterns = [
    path('', signIn, name='signIn')
]
