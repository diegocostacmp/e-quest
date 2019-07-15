from django.urls import path
from .views import (
    listar_quizzes,
    cadastrar_quiz,
    editar_quiz
    )

app_name='quiz'

urlpatterns = [
    # listar quizzes
    path('listar_quizzes/<uuid:disciplina_uuid>/', listar_quizzes, name='listar_quizzes'),
    path('cadastrar_quiz/', cadastrar_quiz, name='cadastrar_quiz'),
    path('editar_quiz/', editar_quiz, name='editar_quiz')
]
