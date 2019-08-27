import django_tables2 as tables
from .models import (
    Discipline,
    Disciplines_user
    )


class DisciplineTable(tables.Table):
    # Acessor para obter nome do professor
    teacher= tables.Column(accessor='get_teacher', verbose_name="Professor")

    # Template com as acoes disponiveis
    actions = tables.TemplateColumn(template_name='discipline/discipline_actions.html', verbose_name="Ações")

    # Status personalizado
    status = tables.Column(accessor='get_status')
    class Meta:
        model = Discipline
        sequence = ['title', 'teacher', 'status', 'actions']
        exclude = ['id', 'uuid', 'date_create', 'date_edit', 'description', 'user_create']

class DisciplineAlunosTable(tables.Table):
    # Acessor para obter nome do professor
    teacher= tables.Column(accessor='get_teacher', verbose_name="Professor")

    # Template com as acoes disponiveis
    actions = tables.TemplateColumn(template_name='discipline/discipline_user_actions.html', verbose_name="Ações")

    # Status personalizado
    status = tables.Column(accessor='get_status')
    class Meta:
        model = Discipline
        sequence = ['title', 'teacher', 'actions']
        exclude = ['id', 'uuid', 'date_create', 'date_edit','status', 'description', 'user_create']

class MinhasDisciplineAlunosTable(tables.Table):
    # Template com as acoes disponiveis
    name_discipline= tables.Column(accessor='get_nome_disciplina', verbose_name="Professor")
    actions = tables.TemplateColumn(template_name='discipline/minhas_discipline_user_actions.html', verbose_name="Ações")

    class Meta:
        model = Disciplines_user
        sequence = [ 'name_discipline', 'actions']
        exclude = ['id','user','uuid', 'date_create', 'discipline']