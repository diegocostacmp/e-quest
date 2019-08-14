import django_tables2 as tables
from .models import (
    Game
)
from apps.quiz.models import Quizzes


class GameTable(tables.Table):
    
    # Status personalizado
    status = tables.Column(accessor='get_status')

    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/game_actions.html', verbose_name="Ações")
    class Meta:
        model = Game
        sequence = ('title', 'students', 'discipline', 'status', 'actions')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create')

class GameStart(tables.Table):

    # Status personalizado
    status = tables.Column(accessor='get_status')

    # Template actions avaiables
    # actions = tables.TemplateColumn(template_name='game/start_actions.html', verbose_name="Ações")
    class Meta:
        model = Quizzes
        sequence = ('title', 'status')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'discipline')
