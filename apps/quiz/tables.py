import django_tables2 as tables
from .models import (
    Quizzes,
    Question
    )


class QuizzesTable(tables.Table):

    # Status personalizado
    status = tables.Column(accessor='get_status')

    # Template com as acoes disponiveis
    acoes = tables.TemplateColumn(template_name='quizzes/quiz_actions.html', verbose_name="Ações")
    class Meta:
        model = Quizzes
        sequence = ('titulo', 'status', 'acoes')
        exclude = ('id', 'uuid', 'data_criacao', 'data_alteracao', 'descricao', 'usuario_criacao', 'disciplina')

class QuestionTable(tables.Table):
    acoes = tables.TemplateColumn(template_name='question/question_actions.html', verbose_name="Ações")
    class Meta:
        model = Question
        sequence = ('title', 'status', 'acoes')
        exclude = ('id', 'uuid', 'description', 'date_create', 'date_edit', 'quiz', 'user_create', 'time_solution')