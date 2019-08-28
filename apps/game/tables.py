import django_tables2 as tables
from .models import (
    Game
)
from apps.quiz.models import Quizzes


class GameTable(tables.Table):
    
    # Status personalizado
    status = tables.Column(accessor='get_status')
    discipline = tables.Column(accessor='get_discipline', verbose_name='Disciplina')

    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/game_actions.html', verbose_name="Ações")
    class Meta:
        model = Game
        sequence = ('title', 'students', 'discipline', 'status', 'actions')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'played')

class GameAlunoTable(tables.Table):
    
    # Status personalizado
    status = tables.Column(accessor='get_status')
    disciplina = tables.Column(accessor='get_discipline', verbose_name='Disciplina')

    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/start_actions_aluno.html', verbose_name="Ações")
    class Meta:
        model = Game
        sequence = ('title', 'students', 'disciplina', 'status', 'actions')
        exclude = ('id', 'uuid', 'date_create', 'description', 'discipline', 'user_create', 'played')

class GameStart(tables.Table):
    
    # Status personalizado
    status = tables.Column(accessor='get_status')
    discipline = tables.Column(accessor='get_discipline')
    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/start_actions.html', verbose_name="Ações")
    class Meta:
        model = Quizzes
        sequence = ('title', 'status', 'discipline')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'discipline')

class GameAlunoStart(tables.Table):

    # Status personalizado
    status = tables.Column(accessor='get_status')
    discipline = tables.Column(accessor='get_discipline')
    # Template actions avaiables
    actions = tables.TemplateColumn(template_name='game/start_actions2.html', verbose_name="Ações")
    class Meta:
        model = Quizzes
        sequence = ('title', 'status', 'discipline')
        exclude = ('id', 'uuid', 'date_create', 'description', 'user_create', 'discipline')
