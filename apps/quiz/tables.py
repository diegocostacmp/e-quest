import django_tables2 as tables
from .models import Disciplina

class DisciplinaTable(tables.Table):
    class Meta:
        model = Disciplina
      