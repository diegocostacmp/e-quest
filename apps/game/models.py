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
    ("O", "Online"),
    ("E", "Executado"),
    ("D", "Desativado")
)

STATUS_GAME = (
    ("A", "Ativo"),
    ("E", "Executando"),
    ("F", "Finalizado")
)
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
    
    def __str__(self):
        return str(self.pk)

    def get_discipline(self):
        return self.discipline.title    

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Ativo</span>') 
        elif self.status == 'F':
            return mark_safe('<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Bloqueado</span>') 
        else:
            return mark_safe('<span class="kt-badge  kt-badge--warning kt-badge--inline kt-badge--pill">Desativo</span>') 

