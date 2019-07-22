from django.shortcuts import (
    render, redirect,
    HttpResponseRedirect,
    get_object_or_404
    )
from django.http import JsonResponse    
from django.urls import (
    reverse, 
    reverse_lazy
    )    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate, 
    login, 
    logout, 
    get_user_model
    )
from django.contrib.auth.models import User

from django.views.decorators.http import (
    require_http_methods,
    require_GET, 
    require_POST,
    ) 

from django_tables2 import RequestConfig
from django.utils import timezone

from .models import (
    User, Discipline
    )
from .tables import DisciplineTable

# tela de login inicial no sistema
def signIn(request):
    return render(request, 'registration/signIn.html')

# autenticacao com User e senha
@require_POST
def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = authenticate(username=email, password=password)
        login(request, user)
        if request.user.is_authenticated:
            data = {
                'status'        : 1,
                'url_return'   : '/begin/'
            }
            return JsonResponse(data)
        else:
            data = {
                'status'        : 0,
                'url_return'   : ''
            }
            return JsonResponse(data)      
    except:
        template_name = 'registration/signIn.html'
        return render(request, template_name)

def logout_get(request):
    logout(request)
    template_name = 'registration/signIn.html'
    return render(request, template_name)
    
@require_POST
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        type_profile = request.POST.get('type_profile', '')

        if len(name) > 0 and len(email) > 0 and len(password) > 0:
            # verifica se a conta ja existe
            user = authenticate(request, email=email, password=password)
            if user is None:
                # cria conta de User
                # user = get_user_model().objects.create_user(username=nome, email=email, password=senha)
                user = User.objects._create_user(email=email, password=password)

                # Atualiza objeto user e salva no banco
                if user is not None:
                    user.is_staff = True

                    # Professor ou aluno
                    user.type_profile = type_profile
                    user.full_name= name
                    user.save()
                    return HttpResponseRedirect('/')
            else:
                error_json  =  {
                    'errors': '1'                    
                }
                template_name = 'registration/signIn.html'    
                return render(request, template_name, error_json)  
        else:
            error_json = {
                'errors': '0'
            }
            template_name = 'registration/signIn.html'    
            return render(request, template_name, error_json)  
    
    return render(request, 'registration/signIn.html')

@login_required
def begin(request):
    # Alias do User
    full_name   = request.user.full_name
    aux             = full_name.split(' ')
    alias_first     = aux[0][:1]
    alias_last      = aux[-1][:1]
    alias_final = str(alias_first) + str(alias_last)

    # Perfil User
    profile = str(request.user.type_profile)

    # Short name
    short_first = aux[0]
    short_last  = aux[-1]
    short_name  = str(short_first) + str(short_last) 

    # Lista as Disciplines do professor
    table = DisciplineTable(Discipline.objects.filter(user_create=request.user))
    RequestConfig(request).configure(table)

    context = {
        "alias_name"    : alias_final,
        "tipo_perfil"   : profile,
        "short_name"    : short_name,
        "table"         : table
    }
    template_name   = "begin.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST'])
def discipline_create(request):
    try:
        nome_Discipline = request.POST.get('name', '')
        print(nome_Discipline)

        # Os dados sao gravados sem a necessidade de forms
        # ja que esta usando sweetalert
        if request.method == "POST":
            title      = nome_Discipline
            register    = Discipline(title=title, status="A", teacher=request.user, user_create=request.user)
            register.save()

            data = {
                "status"        : "OK"
            }
            return JsonResponse(data, safe=False)
    except:
        data = {
            "status": ""
        }
        return JsonResponse(data, safe=False)

@login_required
@require_http_methods(['POST'])
def discipline_delete(request):
    try:
        template_name = 'begin.html'
        uuid_edit   = request.POST.get('uuid_edit', '')
        discipline      = get_object_or_404(Discipline, uuid=uuid_edit)
        if request.method == "POST":
            discipline.delete()

            data = {
                "status": "OK"
            }

            return JsonResponse(data, safe=False)
    except:
        return render(request, template_name, {})
    
@login_required
@require_http_methods(['POST'])
def discipline_edit(request):

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