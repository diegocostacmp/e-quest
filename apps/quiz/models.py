from django.db import models
import uuid

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse

from django.utils.safestring import mark_safe

from apps.core.models import Usuario, Disciplina

# Status choices
STATUS_CHOICES = (
    ("A", "Ativo"),
    ("B", "Bloqueado"),
    ("D", "Desativado")
    )
class Quizzes(models.Model):

    titulo          = models.CharField(verbose_name="Título", max_length=128, help_text="Digite o nome da disciplina", null=False, blank=False, default=None)
    descricao       = models.CharField(verbose_name="Descrição", max_length=512, help_text="Digite a descrição da disciplina", null=True, blank=True, default=None)
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    data_criacao    = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    data_alteracao  = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")

    # fks
    disciplina      = models.ForeignKey(Disciplina, verbose_name="Disciplina", on_delete=models.PROTECT)
    usuario_criacao = models.ForeignKey(Usuario, editable=False, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_professor(self):
        return self.professor.nome_completo

    def get_disciplina(self):
        return self.disciplina.titulo

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Ativo</span>') 
        elif self.status == 'B':
            return mark_safe('<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Bloqueado</span>') 
        else:
            return mark_safe('<span class="kt-badge  kt-badge--warning kt-badge--inline kt-badge--pill">Desativo</span>') 

