from django.urls import path
from .views import *

app_name='quiz'

urlpatterns = [
    # CRUD disciplina
    path('inicio/', inicio, name='inicio'),
    # path('', listar_disciplina, name='disciplina_list'),
    # path('cadastrar_disciplina', cadastrar_disciplina, name='nova_disciplina'),

]
