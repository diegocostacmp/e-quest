from django.urls import path
from .views import *

app_name='quiz'

urlpatterns = [
    # lista de disciplinas
    path('inicio/', inicio, name='inicio'),
    path('cadastrar_disciplina/', cadastrar_disciplina, name='nova_disciplina'),
    path('editar_disciplina/', editar_disciplina, name='editar_disciplina'),
    path('excluir_disciplina/', excluir_disciplina, name='nova_disciplina'),
]
