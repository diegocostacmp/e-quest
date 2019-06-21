from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect
    )
from django.http import JsonResponse    
from django.urls import reverse, reverse_lazy    
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



# tela de login inicial no sistema
def signIn(request):
    return render(request, 'registration/signIn.html')

# autenticacao com usuario e senha
@require_POST
def postsign(request):
    print('veio aqui')
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    try:
        user = authenticate(username=email, password=senha)
        login(request, user)
        if request.user.is_authenticated:
            data = {
                'status'        : 1,
                'url_retorno'   : '/inicio/'
            }
            return JsonResponse(data)
        else:
            data = {
                'status'        : 0,
                'url_retorno'   : ''
            }
            return JsonResponse(data)      
    except:
        print('na excessao')
        template_name = 'registration/signIn.html'
        return render(request, template_name)

    

def logout_get(request):
    logout(request)
    template_name = 'registration/signIn.html'
    return render(request, template_name)
    
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
   
    template_name   = 'inicio.html'
    context = {
        'alias_name'    : alias_final,
        'tipo_perfil'   : perfil,
        'short_name'    : short_name
    }
    return render(request, template_name, context)

@require_POST
def signup(request):
    if request.method == 'POST':
        nome                = request.POST.get('nome', '')
        email               = request.POST.get('email', '')
        senha               = request.POST.get('senha', '')
        tipo                = request.POST.get('tipo', '')

        if len(nome) > 0 and len(email) > 0 and len(senha) > 0:
            # verifica se a conta ja existe
            user = authenticate(request, email=email, password=senha)
            if user is None:
                # cria conta de usuario
                # user = get_user_model().objects.create_user(username=nome, email=email, password=senha)
                from .models import Usuario
                user = Usuario.objects._create_user(email=email, password=senha)

                # Atualiza objeto user e salva no banco
                if user is not None:
                    user.is_staff = True

                    # Professor ou aluno
                    user.tipo = tipo
                    user.nome_completo = nome
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
