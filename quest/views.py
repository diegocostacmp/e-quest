from django.shortcuts import render
import pyrebase

from django.contrib import auth

# string de conexao com o projeto firebase
config = {
    'apiKey':               "AIzaSyDbScV081zr7iWPEmiCN9kPi3jeZlgWmTk",
    'authDomain':           "e-quest-aaecf.firebaseapp.com",
    'databaseURL':          "https://e-quest-aaecf.firebaseio.com",
    'projectId':            "e-quest-aaecf",
    'storageBucket':        "e-quest-aaecf.appspot.com",
    'messagingSenderId':    "662995373472"
}

# referencia para autenticar o servico
firebase = pyrebase.initialize_app(config)

auth_user = firebase.auth()
db = firebase.database()

def signIn(request):
    return render(request, 'registration/signIn.html')

# autenticacao com usario e senha
def postsign(request):

    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = auth_user.sign_in_with_email_and_password(email, passw)
    except:
        return render(request, 'registration/signIn.html', {''})

    session_id = user['idToken']  
    request.session['uid']=str(session_id)  

    return render(request, 'inicio.html', {''})

# logout do sistema
def logout(request):
    auth.logout(request)
    return render(request, 'registration/signIn.html')

# cadastro de novos usuarios
def signup(request):
    return render(request, 'registration/signup.html')

def postsignup(request):

    name    = request.POST.get('name')
    email   = request.POST.get('email')
    passw   = request.POST.get('pass')

    # try:
    user = auth_user.create_user_with_email_and_password(email, passw)
    auth_user.send_email_verification(user['idToken'])
    auth_user.send_password_reset_email(email)

    data = {"name": "Diego Costa", "cargo": "Analista Programador"}
    db.child("users").push("diego costa")

    # except:
    #     return render(request, 'signup.html', {''})
    
    return render(request, 'registration/signIn.html')

def recuperar_senha(request):
    return render(request, '')

