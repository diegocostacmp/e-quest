from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect
    )
from django.http import JsonResponse    
from django.urls import reverse, reverse_lazy    
from django.contrib.auth.decorators import login_required

from django_tables2 import RequestConfig

from .models import Disciplina
from .tables import DisciplinaTable

@login_required
def inicio(request):
    # Alias do usuario
    nome_completo   = request.user.nome_completo
    aux             = nome_completo.split(' ')
    alias_first     = aux[0][:1]
    alias_last      = aux[-1][:1]
    alias_final = str(alias_first) + str(alias_last)

    # Perfil usuario
    perfil = str(request.user.tipo)

    # Short name
    short_first = aux[0]
    short_last  = aux[-1]
    short_name  = str(short_first) + str(short_last) 

    # Lista as disciplinas do professor
    table = DisciplinaTable(Disciplina.objects.all())
    RequestConfig(request).configure(table)
   
    context = {
        'alias_name'    : alias_final,
        'tipo_perfil'   : perfil,
        'short_name'    : short_name,
        'table'         : table
    }
    template_name   = 'inicio.html'
    return render(request, template_name, context)

