import django_tables2 as tables
from .models import (
    Game
)
from apps.quiz.models import Quizzes


class GameTable(tables.Table):
    
    # Status personalizado
    status = tables.Column(accessor='get_status')

    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='quizzes/quiz_actions.html', verbose_name="Ações")
    class Meta:
        model = Game
        sequence = ('title', 'status', 'actions')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'discipline')

class GameStart(tables.Table):

    # Status personalizado
    status = tables.Column(accessor='get_status')

    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/start_actions.html', verbose_name="Ações")
    class Meta:
        model = Quizzes
        sequence = ('title', 'status', 'actions')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'discipline')
