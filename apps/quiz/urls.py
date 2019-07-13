from django.urls import path
from .views import *

app_name='quiz'

urlpatterns = [
    # lista de disciplinas
    path('inicio/', inicio, name='inicio'),
    path('cadastrar_disciplina/', cadastrar_disciplina, name='nova_disciplina'),
    path('editar_disciplina/', editar_disciplina, name='editar_disciplina'),
    path('excluir_disciplina/', excluir_disciplina, name='nova_disciplina'),

    # listar quizzes
    path('listar_quizzes/<uuid:disciplina_uuid>/', listar_quizzes, name='listar_quizzes'),
    path('cadastrar_quiz/', cadastrar_quiz, name='cadastrar_quiz'),
]
