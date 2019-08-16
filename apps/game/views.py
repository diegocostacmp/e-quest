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
from .models import Game
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
def quiz_book_list(request, discipline_uuid):
    queryset = Quizzes.objects.filter(discipline__teacher=request.user, discipline__uuid=discipline_uuid)
    table = GameStart(queryset)
    RequestConfig(request).configure(table)

    context = {
        "table" : table
    }
    template_name   = "game/game_show_quiz.html"
    return render(request, template_name, context)

