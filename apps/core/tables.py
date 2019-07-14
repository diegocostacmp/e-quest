import django_tables2 as tables
from .models import (
    Disciplina
    )


class DisciplinaTable(tables.Table):
    # Acessor para obter nome do professor
    professor= tables.Column(accessor='get_professor')

    # Template com as acoes disponiveis
    acoes = tables.TemplateColumn(template_name='disciplina/disciplina_actions.html')

    # Status personalizado
    status = tables.Column(accessor='get_status')
    class Meta:
        model = Disciplina
        sequence = ['titulo', 'professor', 'status', 'acoes']
        exclude = ['id', 'uuid', 'data_criacao', 'data_alteracao', 'descricao', 'usuario_criacao']
