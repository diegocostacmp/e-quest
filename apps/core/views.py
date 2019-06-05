from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect
    )
from django.contrib.auth.decorators import login_required
from django.contrib import auth

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
        return render(request, template_name, {''})

    return render(request, 'inicio.html', {''})

def logout(request):
    auth.logout(request)
    template_name = 'registration/signIn.html'
    return render(request, template_name)
    
@login_required
def inicio(request):
   
    template_name = 'inicio.html'
    return render(request, template_name)

    # # cadastro de novos usuarios
# def signup(request):
#     return render(request, 'registration/signup.html')

# def postsignup(request):

#     name    = request.POST.get('name')
#     email   = request.POST.get('email')
#     passw   = request.POST.get('pass')

#     # try:
#     user = auth_user.create_user_with_email_and_password(email, passw)
#     auth_user.send_email_verification(user['idToken'])
#     auth_user.send_password_reset_email(email)

#     data = {"name": "Diego Costa", "cargo": "Analista Programador"}
#     db.child("users").push("diego costa")

#     # except:
#     #     return render(request, 'signup.html', {''})
    
#     return render(request, 'registration/signIn.html')

# def recuperar_senha(request):
#     return render(request, '')
