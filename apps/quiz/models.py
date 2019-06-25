from django.db import models
import uuid

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse

from apps.core.models import Usuario

# Cadastro de disciplina
class Disciplina(models.Model):
    titulo          = models.CharField(verbose_name="Título", max_length=128, help_text="Digite o nome da disciplina", null=False, blank=False, default=None)
    descricao       = models.CharField(verbose_name="Descrição", max_length=512, help_text="Digite a descrição da disciplina", null=True, blank=True, default=None)
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    data_criacao    = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True)
    data_alteracao  = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True)

    # fks
    professor       = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

    def get_professor(self):
        return self.professor.nome_completo

