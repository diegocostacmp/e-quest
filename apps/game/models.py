from django.db import models
import uuid

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse

from django.utils.safestring import mark_safe
from apps.core.models import (
    User, Discipline
)
from apps.quiz.models import (
    Quizzes
)

# Status choices
STATUS_CHOICES = (
    ("A", "Ativo"),
    ("O", "Online"),
    ("E", "Executado"),
    ("D", "Desativado")
)

STATUS_QUIZ_PLAYED = (
    ("A", "Ativo"),
    ("F", "Finalizado")
)
class Played(models.Model):
    date_create = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    status = models.CharField(verbose_name="Status", choices=STATUS_QUIZ_PLAYED, max_length=15, default="A")
    user_create = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)
    uuid = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)

    quiz = models.ForeignKey(Quizzes, editable=False, related_name="+", on_delete=models.CASCADE)

class Game(models.Model):
    title = models.CharField(verbose_name="Título", max_length=512, help_text="Digite o nome do game", null=False, blank=False, default=None)
    description = models.CharField(verbose_name="Descrição", max_length=1024, help_text="Digite a descrição do game", null=True, blank=True, default=None)
    uuid = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    user_create = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)

    # fks
    discipline = models.ForeignKey(Discipline, verbose_name="Disciplina", on_delete=models.PROTECT)
    students = models.CharField(max_length=128, verbose_name="Participantes", blank=True, null=True, default=None)
    played = models.ForeignKey(Played, verbose_name="Quiz", related_name="+", on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    def __str__(self):
        return str(self.pk)

    def get_discipline(self):
        return self.discipline.title    

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span class="kt-badge  kt-badge--info kt-badge--inline kt-badge--pill">Ativo</span>') 
        elif self.status == 'O':
            return mark_safe('<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Online</span>') 
        elif self.status == 'E':
            return mark_safe('<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Executado</span>') 
        else:
            return mark_safe('<span class="kt-badge  kt-badge--primary kt-badge--inline kt-badge--pill">Desativo</span>') 



class ClassRoom(models.Model):

    # Get all users online to Game opened
    uuid = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    user_create = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)

    game = models.ForeignKey(Game, editable=False, related_name="+", on_delete=models.CASCADE, default=None, blank=True, null=True)
    student = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.pk)