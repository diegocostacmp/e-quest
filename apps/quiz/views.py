from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect,
    get_object_or_404
    )
from django.http import JsonResponse    
from django.urls import reverse, reverse_lazy    
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from django_tables2 import RequestConfig

from apps.core.models import Usuario

from .models import Disciplina
from .tables import DisciplinaTable
from .forms import (
    DisciplinaForm
    )  

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
        "alias_name"    : alias_final,
        "tipo_perfil"   : perfil,
        "short_name"    : short_name,
        "table"         : table
    }
    template_name   = "inicio.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST'])
def cadastrar_disciplina(request):
    try:
        nome_disciplina = request.POST.get('nome', '')

        # Os dados sao gravados sem a necessidade de forms
        # ja que esta usando sweetalert
        if request.method == "POST":
            titulo      = str(nome_disciplina)
            cadastro    = Disciplina(titulo=titulo, status="A", professor=request.user)
            cadastro.save()

            data = {
                "status"        : "OK",
                "url_retorno"   : "/quiz/inicio/" 
            }
        
            return JsonResponse(data, safe=False)
        
    except:
        data = {
            "status": ""
        }
        return JsonResponse(data, safe=False)

@login_required
@require_http_methods(['POST'])
def excluir_disciplina(request):
    print('chegou excluir!')
    try:
        template_name = 'inicio.html'
        uuid_editando   = request.POST.get('uuid_editando', '')
        disciplina      = get_object_or_404(Disciplina, uuid=uuid_editando)
        if request.method == "POST":
            disciplina.delete()

            data = {
                "status": "OK"
            }

            return JsonResponse(data, safe=False)
    except:
        return render(request, template_name, {})
    