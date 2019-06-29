from django.forms import ModelForm
from .models import Disciplina

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ('titulo', 'status', 'professor')