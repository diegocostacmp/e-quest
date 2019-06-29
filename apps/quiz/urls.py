from django.urls import path
from .views import *

app_name='quiz'

urlpatterns = [
    # lista de disciplinas
    path('inicio/', inicio, name='inicio'),
    path('cadastrar_disciplina/', cadastrar_disciplina, name='nova_disciplina'),
    path('excluir_disciplina/', excluir_disciplina, name='excluir_disciplina')

]
