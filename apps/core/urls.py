from django.urls import path
from .views import (
    signIn, signup,
    postsign, logout_get,
    inicio, cadastrar_disciplina,
    editar_disciplina, excluir_disciplina
    )


app_name='core'

urlpatterns = [
    # Login and logout
    path('', signIn, name='signIn'),
    path('postsign/', postsign, name='postsign'),
    path('signup/', signup, name='signup'),
    path('logout_get/', logout_get, name='logout_get'),

    # lista de disciplinas
    path('inicio/', inicio, name='inicio'),
    path('cadastrar_disciplina/', cadastrar_disciplina, name='nova_disciplina'),
    path('editar_disciplina/', editar_disciplina, name='editar_disciplina'),
    path('excluir_disciplina/', excluir_disciplina, name='nova_disciplina'),
]
