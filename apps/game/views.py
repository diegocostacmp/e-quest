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
    User, Discipline
)

from apps.quiz.models import (
    Quizzes, Question,
    Answer
)
from .models import Game
from .tables import GameTable

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



