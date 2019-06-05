from django.urls import path
from .views import (
    signIn, 
    postsign,
    logout,
    inicio

    )


app_name='core'

urlpatterns = [
    path('', signIn, name='signIn'),
    path('postsign/', postsign, name='postsign'),
    path('logout/', logout, name='logout'),
    path('inicio/', inicio, name='inicio')
]
