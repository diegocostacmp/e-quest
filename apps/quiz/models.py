from django.db import models
import uuid

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse

from django.utils.safestring import mark_safe

from apps.core.models import (
    User, Discipline
    )

# Status choices
STATUS_CHOICES = (
    ("A", "Ativo"),
    ("B", "Bloqueado"),
    ("D", "Desativado")
    )
class Quiz(models.Model):

    title = models.CharField(verbose_name="Título", max_length=128, help_text="Digite o nome da Discipline", null=False, blank=False, default=None)
    description = models.CharField(verbose_name="Descrição", max_length=512, help_text="Digite a descrição da Discipline", null=True, blank=True, default=None)
    uuid = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    date_edit = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")

    # fks
    discipline = models.ForeignKey(Discipline, verbose_name="Discipline", on_delete=models.PROTECT)
    user_create = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_professor(self):
        return self.teacher.full_name

    def get_discipline(self):
        return self.discipline.title

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span style="width: 100%;"><span class="kt-badge kt-badge--success kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-success">Ativo</span></span>') 
        elif self.status == 'B':
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--danger kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-danger">Bloqueado</span></span>') 
        else:
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--warning kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-warnings">Desativado</span></span>') 

class Question(models.Model):
    title           = models.CharField(verbose_name="Título", max_length=512, help_text="Digite o nome da Discipline", null=False, blank=False, default=None)
    description     = models.CharField(verbose_name="Descrição", max_length=1024, help_text="Digite a descrição da Discipline", null=True, blank=True, default=None)
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create     = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    date_edit       = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")

    # fks
    quiz            = models.ForeignKey(Quiz, verbose_name="Quiz", on_delete=models.PROTECT)
    user_create     = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)

    last_id         =  models.CharField(verbose_name="Proximo", max_length=10, blank=True, null=True, default=None)

    time_solution = models.CharField(max_length=16, verbose_name="Tempo de solução", help_text = ("Tempo para resolver a questão"), blank=False, null=False, default=None)

    def __str__(self):
            return str(self.pk)

    def get_status(self):
        if self.status == 'A':
                return mark_safe('<span style="width: 100%;"><span class="kt-badge kt-badge--success kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-success">Ativo</span></span>') 
        elif self.status == 'B':
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--danger kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-danger">Bloqueado</span></span>') 
        else:
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--warning kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-warnings">Desativado</span></span>') 


class Answer(models.Model):

    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create     = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    date_edit       = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    user_create     = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, default=None)

    # Anwers
    alternative_A = models.CharField(max_length=512, verbose_name="Alternativa A", blank=False, null=False, default=None)
    alternative_B = models.CharField(max_length=512, verbose_name="Alternativa B", blank=False, null=False, default=None)
    alternative_C = models.CharField(max_length=512, verbose_name="Alternativa C", blank=False, null=False, default=None)
    alternative_D = models.CharField(max_length=512, verbose_name="Alternativa D", blank=False, null=False, default=None)

    alternative_true = models.CharField(max_length=16, verbose_name="Alternativa correta", blank=False, null=False)  
    question = models.OneToOneField(Question, editable=False, related_name="question_related", on_delete=models.CASCADE)

# Recompensas
class reward(models.Model):
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create     = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    description     = models.CharField(verbose_name="Descrição", max_length=1024, help_text="Digite a descrição da Discipline", null=True, blank=True, default=None)
    points          = models.CharField(verbose_name="Pontos", max_length=5, help_text="Pontos ganhos", null=True, blank=True, default='0')
    # fks
    user            = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)
    discipline      = models.ForeignKey(Discipline, editable=False, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_nome_disciplina(self):
        return self.discipline.title

# Recompensas alunos
class reward_user(models.Model):
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create     = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    # fks
    user            = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)
    reward          = models.ForeignKey(reward, editable=False, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_nome_disciplina(self):
        return self.reward.title