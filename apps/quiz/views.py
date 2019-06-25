from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect
    )
from django_tables2 import RequestConfig

from .models import Disciplina
from .tables import DisciplinaTable


def listar_disciplina(request):
    # Listagem de disciplinas
    table = DisciplinaTable(Disciplina.objects.all())
    RequestConfig(request).configure(table)
    
    context = {
        'table' : table
    }
    return render(request, 'disciplina/disciplina_list.html', context)
