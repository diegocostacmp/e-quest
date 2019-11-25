from datetime import datetime

from django.shortcuts import (
    render, redirect,
    HttpResponseRedirect,
    get_object_or_404, HttpResponse
    )
from django.http import JsonResponse    
from django.urls import (
    reverse, 
    reverse_lazy
    )    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views, authenticate, login, logout, get_user_model

from django.contrib.auth.models import User

from django.views.decorators.http import (
    require_http_methods,
    require_GET, 
    require_POST,
    ) 
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import RequestConfig
from django.utils import timezone

# django CBV
from django.views.generic import CreateView
from django.views import View

# models
from apps.game.models import Game
from .models import (
    User, Discipline, Disciplines_user
    )

# Tables
from .tables import DisciplineTable, DisciplineAlunosTable, MinhasDisciplineAlunosTable
from apps.game.tables import GameAlunoTable

# Forms
from apps.core.forms import DisciplineCreateForm

from django.utils.decorators import classonlymethod

import sweetify


@login_required
def discipline_list(request):
    # Profile
    profile = str(request.user.type_profile)
    
    if int(profile) == 1:
        # Lista as Disciplines do professor
        table = DisciplineAlunosTable(Discipline.objects.all())
        RequestConfig(request).configure(table)

        print(Discipline.objects.all())

        table_user = MinhasDisciplineAlunosTable(Disciplines_user.objects.filter(user=request.user))
        RequestConfig(request).configure(table_user)

        queryset = Game.objects.filter(status='O')
        table_jogos = GameAlunoTable(queryset)
        RequestConfig(request).configure(table_jogos)

        context = {
            "table": table,
            "table_user": table_user,
            "table_jogos" : table_jogos,
        }
        # print('profile: ',profile)
        template_name   = "begin_aluno.html"
    else:
        # Lista as Disciplines do professor
        table = Discipline.objects.filter(user_create=request.user)

        context = {
            "tipo_perfil"   : profile,
            "table"         : table
        }

        template_name = "discipline/list.html"
    return render(request, template_name, context)


@require_http_methods(['POST', 'GET'])
@login_required
def discipline_create(request):
    form = DisciplineCreateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_create = request.user
            instance.teacher= request.user
            instance.save()  
            sweetify.success(request, 'Parabens',
                            text='A disciplina foi cadastrada com sucesso',
                            persistent='OK', timer=2500)
            return HttpResponseRedirect(reverse('core:discipline-list'))
    else:
        template_name = 'discipline/form.html' 
        return render(request, template_name, {'form': form})



@login_required
@require_POST
def discipline_update(request):
    # Obtenho as strings via POST
    discipline          = request.POST.get('title', '')
    discipline_uuid     = request.POST.get('discipline_uuid', '')

    # Retorna objeto com a Discipline
    discipline_edit = get_object_or_404(Discipline, uuid=discipline_uuid)
    discipline_edit.title = str(discipline)
    discipline_edit.save()

    data = {
        'status': 'OK',
        'url_return': '/begin/'
    }

    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(['GET'])
def discipline_delete(request, uuid_discipline):
    try:
        discipline = get_object_or_404(Discipline, uuid=uuid_discipline)
        discipline.delete()
        sweetify.success(request, 'Parabens',
                            text='A disciplina foi removida com sucesso',
                            persistent='OK', timer=2500)

        return redirect('core:discipline-list')
    except:
        sweetify.success(request, 'Ops...',
                            text='Existem dependências associadas a este cadastro',
                            persistent='OK', timer=2500)
        return redirect('core:discipline-list')