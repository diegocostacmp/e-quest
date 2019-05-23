from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# tela de login inicial no sistema
def signIn(request):
    print('chegou aqui.')
    return render(request, 'registration/signIn.html')