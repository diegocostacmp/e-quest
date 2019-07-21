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
from django.utils import timezone

from apps.core.models import Usuario, Disciplina

from .models import Quizzes, Question
from .tables import QuizzesTable, QuestionTable

@login_required
@require_http_methods(['POST', 'GET'])
def quiz_list(request, disciplina_uuid):
    print('chegou no metodo')

    # Verifica se a instancia da disciplina existe
    disciplina_editando = get_object_or_404(Disciplina, uuid=disciplina_uuid)
    # Lista os quizzes cadastrados por disciplina

    # Query
    queryset = Quizzes.objects.filter(disciplina__uuid=disciplina_editando.uuid)

    table = QuizzesTable(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "disciplina_uuid": disciplina_editando.uuid
    }

    template_name   = "quizzes/quiz_list.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST'])
def quiz_create(request):
    try:
        titulo = request.POST.get('nome', '')
        disciplina= request.POST.get('disciplina', '')

        print(titulo)
        print(disciplina)

        # Get instance
        disciplina_editando = get_object_or_404(Disciplina, uuid=disciplina)

        # Os dados sao gravados sem a necessidade de forms
        if request.method == "POST":
            cadastro = Quizzes(titulo=titulo, status="A", disciplina=disciplina_editando, usuario_criacao=request.user)
            cadastro.save()
        
            data = {
                "status" : "OK",
                "url_retorno" : "/quiz/quiz_list/"+str(disciplina_editando.uuid)+"/" 
            }
            return JsonResponse(data)
    except: 
        data = {
            "status": ""
        }
        return JsonResponse(data, safe=False)

@login_required
@require_http_methods(['POST'])
def quiz_edit(request):

    # Obtenho as strings via POST
    quiz          = request.POST.get('titulo', '')
    uuid_quiz     = request.POST.get('uuid_quiz', '')

    # Retorna objeto com o quiz
    quiz_editando = get_object_or_404(Quizzes, uuid=uuid_quiz)
    print(quiz_editando.disciplina)
    quiz_editando.titulo = str(quiz)
    quiz_editando.save()

    data = {
        'status': 'OK'
    }

    return JsonResponse(data, safe=False)

def quiz_delete(request):
    
    uuid_editando   = request.POST.get('uuid_editando', '')
    quiz      = get_object_or_404(Quizzes, uuid=uuid_editando)
    if request.method == "POST":
        quiz.delete()
        data = {
            "status": "OK"
        }
    return JsonResponse(data)
   
@login_required
@require_http_methods(['GET'])
def question_list(request, quiz_uuid):

    # Verifica se a instancia do quiz existe
    quiz_edit = get_object_or_404(Quizzes, uuid=quiz_uuid)
    # Lista os quizzes cadastrados por disciplina

    # Query
    queryset = Question.objects.filter(quiz__uuid=quiz_edit.uuid)

    table = QuestionTable(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "quiz_uuid": quiz_edit.uuid
    }

    template_name   = "question/question_list.html"
    return render(request, template_name, context)
