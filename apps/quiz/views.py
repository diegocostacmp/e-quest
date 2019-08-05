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
from django.template.loader import render_to_string

from apps.core.models import User, Discipline

from .models import (Quizzes, Question,
    Answer
    )
from .tables import (QuizzesTable,
    QuestionTable
    )

@login_required
@require_http_methods(['POST', 'GET'])
def quiz_list(request, discipline_uuid):
    # Verifica se a instancia da Discipline existe
    discipline_edit = get_object_or_404(Discipline, uuid=discipline_uuid)
    # Lista os quizzes cadastrados por Discipline

    # Query
    queryset = Quizzes.objects.filter(discipline__uuid=discipline_edit.uuid)

    table = QuizzesTable(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "discipline_uuid": discipline_edit.uuid
    }

    template_name   = "quizzes/quiz_list.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST'])
def quiz_create(request):
    try:
        title = request.POST.get('name', '')
        discipline= request.POST.get('discipline', '')

        # Get instance
        discipline_edit = get_object_or_404(Discipline, uuid=discipline)

        # Os dados sao gravados sem a necessidade de forms
        if request.method == "POST":
            register = Quizzes(title=title, status="A", discipline=discipline_edit, user_create=request.user)
            register.save()
        
            data = {
                "status" : "OK",
                "url_return" : "/quiz/quiz_list/"+str(discipline_edit.uuid)+"/" 
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
    print(quiz_editando.Discipline)
    quiz_editando.titulo = str(quiz)
    quiz_editando.save()

    data = {
        'status': 'OK'
    }

    return JsonResponse(data, safe=False)

@login_required
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

    # Get discipline
    discipline = get_object_or_404(Discipline, pk=quiz_edit.discipline.pk)

    # Query
    queryset = Question.objects.filter(quiz__uuid=quiz_edit.uuid)

    table = QuestionTable(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "discipline_uuid": discipline.uuid,
        "quiz_uuid": quiz_edit.uuid
    }

    template_name   = "question/question_list.html"
    return render(request, template_name, context)


@login_required
@require_http_methods(['POST'])
def question_book(request):
    data = dict()
    quiz_uuid = request.POST.get('quiz_uuid', '')
    context = {}
    context['data'] = render_to_string("question/question_form.html")
    return JsonResponse(context)


@login_required
@require_http_methods(['POST'])
def question_create(request):
    try:
        # Question
        quiz_uuid = request.POST.get('quiz_uuid', '')
        message = request.POST.get('message', '')

        # Answer
        msg_A = request.POST.get('msg_A', '')
        msg_B = request.POST.get('msg_B', '')
        msg_C = request.POST.get('msg_C', '')
        msg_D = request.POST.get('msg_D', '')
        seconds = request.POST.get('seconds', '')
        optSelected = request.POST.get('optSelected', '')

        # Get quiz edit
        quiz_edit = get_object_or_404(Quizzes, uuid=quiz_uuid)

        # Create question
        if request.method == "POST":
            question_register = Question(title=message, status="A", time_solution=str(seconds), quiz=quiz_edit, user_create=request.user)
            question_register.save()

            answer_register = Answer(question=question_register, alternative_A=msg_A, alternative_B=msg_B, alternative_C=msg_C, alternative_D=msg_D, user_create=request.user, alternative_true=optSelected)
            answer_register.save()

        data = {
            "status": "OK"
        }
        return JsonResponse(data)
    except:
        data = {
            "status":"",
            "msg_return": "Desculpe, tivemos algum problema ao cadastrar a questão"
        }
        return JsonResponse(data)
        
@login_required
@require_http_methods(['POST'])        
def question_delete(request):
    uuid_edit = request.POST.get('uuid_edit', '')
    question = get_object_or_404(Question, uuid=uuid_edit)

    exists_answer = get_object_or_404(Answer, question=question.pk)
    if exists_answer is not None:
        if request.method == "POST":
            exists_answer.delete()
            question.delete()
    else:
        print('Desculpe, tivemos algum problema')

    data = {
        "status": "OK"
    }
    return JsonResponse(data)

@login_required
@require_http_methods(['POST'])
def question_book_preview(request):
    data = dict()
    context = {}
    context['string_html'] = render_to_string("question/question_preview.html")
    return JsonResponse(context)
