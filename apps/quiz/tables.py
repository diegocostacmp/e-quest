import django_tables2 as tables
from .models import (
    Quizzes
    )


class QuizzesTable(tables.Table):

    # Status personalizado
    status = tables.Column(accessor='get_status')
    class Meta:
        model = Quizzes
        sequence = ('titulo', 'status')
        exclude = ('id', 'uuid', 'data_criacao', 'data_alteracao', 'descricao', 'usuario_criacao', 'disciplina')