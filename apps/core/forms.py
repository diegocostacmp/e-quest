from django import forms
from .models import Discipline

from crispy_forms.helper import FormHelper


class DisciplineCreateForm(forms.ModelForm):
    class Meta:
        model = Discipline
        # fields = ['title', 'description']
        sequence = ['title', 'description']
        exclude = ['uuid', 'date_create', 'date_edit', 'status', 'user_create', 'teacher']
