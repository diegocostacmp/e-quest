import django_tables2 as tables
from .models import Disciplina


class DisciplinaTable(tables.Table):
    professor= tables.Column(accessor='get_professor')
    class Meta:
        model = Disciplina
        sequence = ['titulo', 'descricao', 'professor']
        exclude = ['id', 'uuid', 'data_criacao', 'data_alteracao']
      