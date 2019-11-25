from django import forms
from .models import Quiz

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, Submit, Row, Column, Div,
    ButtonHolder, Field)


class QuizCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuizCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('title', css_class="form-group has-top-label"),
                Field('description', css_class="form-group has-top-label")
                )
        )

    class Meta:
        model = Quiz
        sequence = ['title', 'description']
        exclude = ['uuid', 'date_create', 'date_edit', 'status', 'user_create',
                    'discipline']

