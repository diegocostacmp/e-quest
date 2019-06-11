from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect
    )
from django.contrib.auth.decorators import login_required
from django.contrib import auth
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
    
    login = request.POST.get('email')
    senha = request.POST.get('senha')

    try:
        user = auth.authenticate(username=login, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('core:inicio')

    except:
        template_name = 'registration/signIn.html'
        return render(request, template_name)

    return render(request, 'inicio.html')

def logout(request):
    auth.logout(request)
    template_name = 'registration/signIn.html'
    return render(request, template_name)
    
@login_required
def inicio(request):
    template_name = 'inicio.html'
    return render(request, template_name)

@require_POST
@login_required
def signup(request):
    if request.method == 'POST':
        name    = request.POST.get('fullname')
        email   = request.POST.get('email')
        passw   = request.POST.get('password')
        rpassw  = request.POST.get('rpassword')
        tipo    = request.POST.get('')


        user    = User.objects.create_user(name, email, passw) 
        user.save()  
    
    return render(request, 'registration/signIn.html')

def recuperar_senha(request):
    return render(request, '')
