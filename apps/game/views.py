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
from django.db.models import Q


from apps.core.models import (
    User, Discipline
)

from apps.quiz.models import (
    Quiz, Question,
    Answer
)
from .models import (
    Game, Played,
    ClassRoom, Played
)
from .tables import (
    GameTable, GameStart, GameAlunoStart
)

import json
import random
import string

@login_required
@require_http_methods(["GET"])
def game_list(request):

    queryset = Game.objects.filter(discipline__teacher=request.user)
    table = GameTable(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table
    }
    template_name   = "game/game_list.html"
    return render(request, template_name, context)

@login_required
@require_http_methods(['POST'])
def game_discipline_book(request):
    # Get disciplines 
    result = []
    discipline_list = Discipline.objects.filter(teacher=request.user)

    for item in discipline_list:
        result.append({
            "discipline": item.title,
            "uuid": item.uuid
        })
        
    return JsonResponse(result, safe=False)

@login_required
@require_http_methods(["GET"])
def game_create(request, discipline_uuid):

    # List quizzes and register new game
    discipline_instance = get_object_or_404(Discipline, uuid=discipline_uuid)

    random = randomString(5)
    register = Game(title=random, discipline=discipline_instance, students=10, user_create=request.user)
    register.save()



    return redirect('game:game_list')
    
def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters.upper()) for i in range(stringLength))

@login_required
def quiz_book_list(request, discipline_uuid, game_uuid):
    queryset = Quizzes.objects.filter(discipline__teacher=request.user, discipline__uuid=discipline_uuid)
    table = GameStart(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "game_uuid":game_uuid
    }
    template_name   = "game/game_show_quiz.html"
    return render(request, template_name, context)

@login_required
def quiz_book_list_aluno(request, game_uuid, discipline_id):
    queryset = Quizzes.objects.filter(status='A', discipline__id=discipline_id)
    print('queryset: ',queryset)
    table = GameAlunoStart(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "game_uuid":game_uuid
    }
    template_name   = "game/game_show_quiz_aluno.html"
    return render(request, template_name, context)

@login_required
def game_await(request, game_uuid, quiz_uuid):
    # get quiz edit
    quiz = get_object_or_404(Quizzes, uuid=quiz_uuid)

    # Register new game_played
    new_played = Played(quiz=quiz, user_create=request.user, status="A")
    new_played.save()

    # Updated status and quiz_played
    game = get_object_or_404(Game, uuid=game_uuid)
    game.status = "O"
    game.played = new_played
    game.save()

    question = Question.objects.filter(quiz=quiz.pk, status="A")
    answer = Answer.objects.filter(question__quiz=quiz.pk, status="A")

    # Get first question
    next_question = Question.objects.filter(quiz=quiz.pk, status="A").first()
    

    context = {
        "game_uuid": game.uuid,
        "game_title": game.title,
        "quiz_title": quiz.title,
        "quiz_discipline": quiz.discipline.title,
        "question": question,
        "answer": answer,
        "amount_questions": question.count(),

        "next_question": next_question.uuid
        
    }

    return render(request, 'game/game_await.html', context)

@login_required
def game_await_aluno(request, game_uuid, quiz_uuid):
    # get quiz edit
    quiz = get_object_or_404(Quizzes, uuid=quiz_uuid)

    # Register new game_played
    new_played = Played(quiz=quiz, user_create=request.user, status="A")
    new_played.save()

    # Updated status and quiz_played
    game = get_object_or_404(Game, uuid=game_uuid)
    game.status = "O"
    game.played = new_played
    game.save()

    question = Question.objects.filter(quiz=quiz.pk, status="A")
    # print('question: ',question)
    # question_obj = get_object_or_404(Question, quiz=quiz.pk, status="A")
    answer = Answer.objects.filter(question__id=16, status="A")
    # print('answer: ',answer)
    # Get first question
    next_question = Question.objects.filter(quiz=quiz.pk, status="A").first()

    context = {
        "game_uuid": game.uuid,
        "game_title": game.title,
        "quiz_title": quiz.title,
        "quiz_discipline": quiz.discipline.title,
        "question": question,
        "answer": answer,
        "amount_questions": question.count(),

        "next_question": next_question.uuid
    }

    return render(request, 'game/game_await _aluno.html', context)

@login_required
@require_http_methods(["POST"])
def next_question(request):
    question = request.POST.get('question_principal', '')
    question_edit = get_object_or_404(Question, uuid=question)
    qs = Question.objects.filter(quiz=question_edit.quiz)

    next_list = []
    for i in qs:
        if i.pk > question_edit.pk:
            next_list.append(
                i.pk
            )
    print(next_list)
    next_question = get_object_or_404(Question, pk=next_list[0])    
    slug_random = randomString(5)
    print(slug_random)
    

    context = {
        "question_title": str(next_question.title),
        "question_uuid": str(next_question.uuid),
        "slug_random": str(slug_random)
    }
    data = render_to_string("teacher/question_list.html", context)
    return JsonResponse(data, safe=False)




@login_required
@require_http_methods(['POST'])
def students_online(request):

    # Get game active
    game_uuid = request.POST.get('game_uuid', '')
    game_active = get_object_or_404(Game, uuid=game_uuid)

    # Get students online
    students = ClassRoom.objects.filter(game=game_active.pk, status="O")
    context = {
        "students": students
    }

    message = render_to_string("student/student_online.html", context=context)
    return JsonResponse(message, safe=False)

@login_required
def game_init(request, uuid_question):
    question_edit = get_object_or_404(Question, uuid=uuid_question)
    slug_random = randomString(5)
    context = {
        "question_title": question_edit.title,
        "question_uuid": question_edit.uuid,
        "slug_random": str(slug_random)
        
    }
    return render(request, 'game/game_start.html', context)


#Aluno
@login_required
def painel_quiz_aluno(request, game_uuid):
    queryset = Quizzes.objects.filter(discipline__teacher=request.user, discipline__uuid=discipline_uuid)
    table = GameStart(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table,
        "game_uuid":game_uuid
    }
    template_name   = "game/game_show_quiz.html"
    return render(request, template_name, context)