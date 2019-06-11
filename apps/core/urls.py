from django.urls import path
from .views import (
    signIn, 
    signup,
    postsign,
    logout,
    inicio

    )


app_name='core'

urlpatterns = [
    path('', signIn, name='signIn'),
    path('postsign/', postsign, name='postsign'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('inicio/', inicio, name='inicio')
]
