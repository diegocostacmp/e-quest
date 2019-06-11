from django.urls import path
from .views import (
    signIn, 
    signup,
    postsign,
    logout_get,
    inicio

    )


app_name='core'

urlpatterns = [
    # Login and logout
    path('', signIn, name='signIn'),
    path('postsign/', postsign, name='postsign'),
    path('signup/', signup, name='signup'),
    path('logout_get/', logout_get, name='logout_get'),
    path('inicio/', inicio, name='inicio')
]
