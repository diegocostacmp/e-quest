from datetime import datetime

from django.shortcuts import (
    render, redirect,
    HttpResponseRedirect,
    get_object_or_404, HttpResponse, Http404
    )
from django.http import JsonResponse    
from django.urls import (
    reverse, 
    reverse_lazy
    )    
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.contrib.auth.models import User

from django.views.decorators.http import (
    require_http_methods,
    require_GET, 
    require_POST,
    ) 
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import RequestConfig
from django.utils import timezone

from django.contrib import messages

# models
from apps.game.models import Game
from .models import (
    User, Discipline, Disciplines_user
    )

# Tables
from .tables import DisciplineTable, DisciplineAlunosTable, MinhasDisciplineAlunosTable
from apps.game.tables import GameAlunoTable

# Forms
from .forms import SignUpForm, SignInForm

from django.utils.decorators import classonlymethod
from apps.core.crud_views import (discipline_list)

import sweetify

# tela de login inicial no sistema
def sign_in(request):
    return render(request, 'registration/sign_in.html')

@require_http_methods(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # get data fields
            data = form.cleaned_data
            email = data['email']
            password = data['password']

            # verifica se a conta ja existe
            user = auth.authenticate(request, email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('core:discipline-list')
                # FIXME: mensagens de excessao
            else:
                print("Nao achou o usuario")

            return HttpResponse("OK")
                    # return HttpResponseRedirect(reverse_lazy('core:discipline-list'))
                # else:
                #     context = {
                #         "form": form,
                #     }
                #     template_name = 'registration/sign_in.html' 
                #     return render(request, template_name, context)
    
        else:
            return HttpResponse(str(form.errors))    
    else:
        form = SignInForm(request.POST)
        context = {
            "form": form
        }

        template_name = 'registration/sign_in.html' 
        return render(request, template_name, context)

def logout(request):
    auth.logout(request)
    return redirect('core:login')
    

@require_http_methods(['POST', 'GET'])
def sign_up(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            # get data fields
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            type_profile = data["type_profile"]
            full_name = data["full_name"]

            # verifica se a conta ja existe
            user = auth.authenticate(request, email=email, password=password)
            if user is None:
                user = User.objects._create_user(email=email, password=password)

                # Atualiza objeto user e salva no banco
                if user is not None:
                    user.is_staff = True

                    # Professor ou aluno
                    user.type_profile = type_profile
                    user.full_name= full_name
                    user.save()
                    return HttpResponseRedirect('/')
            else:
                context = {
                    "form": form,
                    "error": "True"
                }
                template_name = 'registration/sign_up.html' 
                return render(request, template_name, context)

    
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        template_name = 'registration/sign_up.html' 
        return render(request, template_name, {'form': form})
    
@login_required
def discipline_add_aluno(request, uid_aluno):
    now = datetime.now()
    disciplina = get_object_or_404(Discipline, uuid=uid_aluno)
    print('disciplina: ',disciplina)
    
    minhas_disciplinas_obj = Disciplines_user()
    minhas_disciplinas_obj.date_create  = now
    minhas_disciplinas_obj.user         = request.user
    minhas_disciplinas_obj.discipline   = disciplina
    minhas_disciplinas_obj.save()

    return redirect('core:begin')

def test_view(request):
    sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    return redirect('/')