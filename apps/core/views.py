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

from django.utils.decorators import classonlymethod
from apps.core.crud_views import (discipline_list)

# tela de login inicial no sistema
def sign_in(request):
    return render(request, 'registration/signIn.html')

# autenticacao com User e senha
@require_POST
@csrf_exempt
def login(request):
    username = request.POST.get('email', '')
    password = request.POST.get('password', '')

    try:
        user = authenticate(email=username, password=password)
        login(request, user)
        if request.user.is_authenticated:
            return redirect('core:discipline-list')
            # FIXME: mensagens de excessao
    except:
        template_name = 'registration/signIn.html'
        return render(request, template_name, {})

def logout(request):
    logout(request)
    template_name = 'registration/signIn.html'
    return render(request, template_name)
    
# @require_POST
# def sign_up(request):
#     print('sign_up')
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         password = request.POST.get('password', '')
#         type_profile = request.POST.get('type_profile', '')

#         print('---------------------------------')
#         print(name, email, password, type_profile)
#         print('---------------------------------')

#         if len(name) > 0 and len(email) > 0 and len(password) > 0:
#             # verifica se a conta ja existe
#             user = authenticate(request, email=email, password=password)
#             if user is None:
#                 # cria conta de User
#                 # user = get_user_model().objects.create_user(username=nome, email=email, password=senha)
#                 user = User.objects._create_user(email=email, password=password)

#                 # Atualiza objeto user e salva no banco
#                 if user is not None:
#                     user.is_staff = True

#                     # Professor ou aluno
#                     user.type_profile = type_profile
#                     user.full_name= name
#                     user.save()
#                     return HttpResponseRedirect('/')
#             else:
#                 error_json  =  {
#                     'errors': '1'                    
#                 }
#                 template_name = 'registration/signIn.html'    
#                 return render(request, template_name, error_json)  
#         else:
#             error_json = {
#                 'errors': '0'
#             }
#             template_name = 'registration/signIn.html'    
#             return render(request, template_name, error_json)  
    
#     return render(request, 'registration/signIn.html')

@require_POST
def sign_up(request):
    print('sign_up')
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # verifica se a conta ja existe
            user = authenticate(request, email=form.mail, password=form.password)
            if user is not None:
                

            instance = form.save(commit=False)
            instance.user_create = request.user
            instance.teacher= request.user
            instance.save()     
        return HttpResponseRedirect(reverse('core:discipline-list'))
    
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        template_name = 'discipline/form.html' 
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