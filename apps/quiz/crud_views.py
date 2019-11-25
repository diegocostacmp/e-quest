from django.shortcuts import (
    render, 
    redirect,
    HttpResponseRedirect,
    get_object_or_404
    )

from django.core import serializers
from django.http import JsonResponse    
from django.urls import reverse, reverse_lazy    
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


from django_tables2 import RequestConfig
from django.utils import timezone
from django.template.loader import render_to_string

from apps.core.models import (
    User, Discipline,
    Disciplines_user
    )

from apps.core.tables import(
    UserDisciplineTable
    )

from .models import (Quiz, Question,
    Answer
    )
from .tables import (QuizzesTable,
    QuestionTable
    )
from .forms import (QuizCreateForm)

@login_required
@require_http_methods(['POST', 'GET'])
def quiz_list(request, uuid_discipline):
    queryset = Quiz.objects.filter(discipline__uuid=uuid_discipline)
    context = {
        "table" : queryset,
        "uuid": uuid_discipline
    }
    template_name   = "quiz/list.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST', 'GET'])
def quiz_create(request, uuid_discipline):
    form = QuizCreateForm(request.POST)
    discipline = get_object_or_404(Discipline, uuid=uuid_discipline)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_create = request.user
            instance.discipline = discipline
            instance.save()     
        return redirect('quiz:quiz-list', uuid_discipline)
    else:
        template_name = 'quiz/form.html' 
        return render(request, template_name, {'form': form})

@login_required
@require_http_methods(['POST'])
def quiz_update(request):

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
@require_http_methods(["POST"])
def quiz_delete(request):
    
    uuid_editando   = request.POST.get('uuid_edit', '')
    quiz      = get_object_or_404(Quizzes, uuid=uuid_editando)
    if request.method == "POST":
        quiz.delete()
        data = {
            "status": "OK"
        }
    return JsonResponse(data)

