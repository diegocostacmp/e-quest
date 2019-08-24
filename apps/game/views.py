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

from django.core import serializers

from apps.core.models import (
    User, Discipline
)

from apps.quiz.models import (
    Quizzes, Question,
    Answer
)
from .models import (
    Game, Played,
    ClassRoom, Played
)
from .tables import (
    GameTable, GameStart
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

    context = {
        "game_uuid": game.uuid,
        "game_title": game.title,
        "quiz_title": quiz.title,
        "quiz_discipline": quiz.discipline.title,
        "question": question,
        "answer": answer,
        "amount_questions": question.count()
    }

    return render(request, 'game/game_await.html', context)

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

    message = render_to_string("student/student_online.html", context)
    return JsonResponse(message, safe=False)
