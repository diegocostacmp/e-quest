from django import forms
from .models import Discipline, User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, Submit, Row, Column, Div,
    ButtonHolder, Field)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('full_name', css_class="form-group has-top-label"),
                Field('email', css_class="form-group has-top-label"),
                Field('password', css_class="form-group has-top-label"),
                Field('type_profile', css_class="form-group has-top-label"),
                )
        )
    class Meta:
        model = User
        sequence = ['full_name', 'email', 'password', 'type_profile']
        exclude = ['username', 'uuid', 'cpf', 'birth_date', 'sex', 
                    'marital_status', 'phone', 'street', 'street_number',
                    'complement', 'state', 'city', 'last_login', 'is_superuser',
                    'groups', 'user_permissions'
            ]
    
class SignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('email', css_class="form-group has-top-label"),
                Field('password', css_class="form-group has-top-label")
                )
        )
    class Meta:
        model = User
        sequence = ['email', 'password']
        exclude = ['username', 'uuid', 'cpf', 'birth_date', 'sex', 
                    'marital_status', 'phone', 'street', 'street_number',
                    'complement', 'state', 'city', 'last_login', 'is_superuser',
                    'type_profile', 'full_name', 'is_active', 'groups', 'user_permissions'
            ]


class DisciplineCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DisciplineCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('title', css_class="form-group has-top-label"),
                Field('description', css_class="form-group has-top-label")
                )
        )

    class Meta:
        model = Discipline
        sequence = ['title', 'description']
        exclude = ['uuid', 'date_create', 'date_edit', 'status', 'user_create',
                    'teacher']