from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    AbstractUser, 
    AbstractBaseUser,
    PermissionsMixin, 
    BaseUserManager
    )

import uuid

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager

from django.utils.safestring import mark_safe


# Status choices
STATUS_CHOICES = (
    ("A", "Ativo"),
    ("B", "Bloqueado"),
    ("D", "Desativado")
    )

# backend de autenticacao personalizado com email
class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):

    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia "),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal "),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    )

    ESTADO_CIVIL_CHOICES = (
        ("Solteiro", "Solteiro"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viúvo", "Viúvo")
    )

    # Informacoes do usuario
    nome_completo               = models.CharField(max_length=50, null=False, verbose_name="Nome Completo")
    username                    = models.CharField(max_length=512, blank=True, null=True, default=None)
    email                       = models.EmailField(null=False, verbose_name="E-mail", unique=True)
    uid                         = models.UUIDField(verbose_name='Identificador Unico', default=uuid.uuid4, editable=False)
    
    
    cpf                         = models.CharField(max_length=14, null=False, verbose_name="CPF")
    data_nascimento             = models.DateField(null=True, verbose_name="Data de Nascimento")
    sexo                        = models.CharField(null=True, verbose_name="Sexo", choices=SEXO_CHOICES, max_length=10)
    estado_civil                = models.CharField(null=True, verbose_name="Estado Civil", choices=ESTADO_CIVIL_CHOICES, max_length=10)
    telefone                    = models.CharField(null=True, verbose_name="Telefone", max_length=19)
    logradouro                  = models.CharField(null=True, max_length=150, verbose_name="Logradouro")
    numero_endereco             = models.PositiveIntegerField(null=True, verbose_name="Número")
    complemento_endereco        = models.CharField(max_length=200, verbose_name="Complemento", null=False)
    estado                      = models.CharField(null=True, choices=ESTADO_CHOICES, max_length=15)
    cidade                      = models.CharField(null=True, max_length=40, verbose_name="Cidade")
    tipo                        = models.CharField(null=True, max_length=10, verbose_name="Tipo")   
    

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return str(self.pk)

    def get_tipo_user(self):
        return self.tipo

# Cadastro de disciplina
class Disciplina(models.Model):
    
    titulo          = models.CharField(verbose_name="Título", max_length=128, help_text="Digite o nome da disciplina", null=False, blank=False, default=None)
    descricao       = models.CharField(verbose_name="Descrição", max_length=512, help_text="Digite a descrição da disciplina", null=True, blank=True, default=None)
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    data_criacao    = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    data_alteracao  = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    usuario_criacao = models.ForeignKey(Usuario, editable=False, related_name="+", on_delete=models.CASCADE)

    # fks
    professor       = models.ForeignKey(Usuario, editable=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    def get_professor(self):
        return self.professor.nome_completo

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Ativo</span>') 
        elif self.status == 'B':
            return mark_safe('<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Bloqueado</span>') 
        else:
            return mark_safe('<span class="kt-badge  kt-badge--warning kt-badge--inline kt-badge--pill">Desativo</span>') 







