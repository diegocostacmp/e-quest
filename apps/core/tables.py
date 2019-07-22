import django_tables2 as tables
from .models import (
    Discipline
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
