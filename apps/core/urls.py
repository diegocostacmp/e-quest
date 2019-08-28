from django.urls import path
from .views import (
    signIn, signup,
    postsign, logout_get,
    begin, discipline_create,
    discipline_edit, discipline_delete, discipline_add_aluno
    )


app_name='core'

urlpatterns = [
    # Login and logout
    path('', signIn, name='signIn'),
    path('postsign/', postsign, name='postsign'),
    path('signup/', signup, name='signup'),
    path('logout_get/', logout_get, name='logout_get'),

    # lista de Disciplines
    path('begin/', begin, name='begin'),
    path('discipline_create/', discipline_create, name='discipline_create'),
    path('discipline_edit/', discipline_edit, name='discipline_edit'),
    path('discipline_delete/', discipline_delete, name='discipline_delete'),

    path('discipline/aluno/<uuid:uid_aluno>/add/', discipline_add_aluno, name='discipline_add_aluno'),
]
