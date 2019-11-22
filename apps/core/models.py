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

import hashlib
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
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

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

    TIPO_PERFIL = (
        ("1", "Professor"),
        ("2", "Aluno")
    )

    # Info signUp
    full_name = models.CharField(max_length=50, null=False, verbose_name="Nome Completo", default=None)
    email = models.EmailField(null=False, verbose_name="E-mail")
    type_profile = models.CharField(verbose_name="Tipo do perfil", max_length=1, choices=TIPO_PERFIL, default=1)   
    password = models.CharField(_('password'), max_length=128)
    is_active = models.BooleanField(_("Ativo"), null=False, blank=False, default=True)
    
    username = models.CharField(max_length=512, blank=True, null=True, default=None)
    uuid = models.UUIDField(verbose_name='Identificador Unico', default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF")
    birth_date = models.DateField(null=True, verbose_name="Data de Nascimento")
    sex = models.CharField(null=True, verbose_name="Sexo", choices=SEXO_CHOICES, max_length=10)
    marital_status = models.CharField(null=True, verbose_name="Estado Civil", choices=ESTADO_CIVIL_CHOICES, max_length=10)
    phone = models.CharField(null=True, verbose_name="Telefone", max_length=19)
    street = models.CharField(null=True, max_length=150, verbose_name="Logradouro")
    street_number = models.PositiveIntegerField(null=True, verbose_name="Número")
    complement = models.CharField(max_length=200, verbose_name="Complemento", null=False)
    state = models.CharField(null=True, choices=ESTADO_CHOICES, max_length=15)
    city = models.CharField(null=True, max_length=40, verbose_name="Cidade")
    
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.pk)

    def get_tipo_user(self):
        return self.type_profile

    # def save(self, *args, **kwargs):        
    #     self.password = hashlib.md5(self.password).hexdigest()
    #     super().save(*args, **kwargs)
        
    

# Cadastro de Discipline
class Discipline(models.Model):
    
    title = models.CharField(verbose_name="Título", max_length=128, help_text="Digite o nome da Disciplina", null=False, blank=False, default=None)
    description = models.CharField(verbose_name="Descrição", max_length=512, help_text="Digite a descrição da Disciplina", null=True, blank=True, default=None)
    uuid = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    date_edit = models.DateTimeField(verbose_name="Data alteração", auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    user_create = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)

    # fks
    teacher = models.ForeignKey(User, editable=False, on_delete=models.PROTECT, verbose_name="Professor", blank=False, null=False)

    def __str__(self):
        return str(self.pk)

    def get_teacher(self):
        return self.teacher.full_name

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span style="width: 100%;"><span class="kt-badge kt-badge--success kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-success">Ativo</span></span>') 
        elif self.status == 'B':
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--danger kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-danger">Bloqueado</span></span>') 
        else:
            return mark_safe('<span style="width: 123px;"><span class="kt-badge kt-badge--warning kt-badge--dot"></span>&nbsp;<span class="kt-font-bold kt-font-warnings">Desativado</span></span>') 
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

# Discipline
class Disciplines_user(models.Model):
    status          = models.CharField(choices=STATUS_CHOICES, max_length=15, default="A")
    uuid            = models.UUIDField(verbose_name='Identificador Único', default=uuid.uuid4, editable=False)
    date_create     = models.DateTimeField(verbose_name="Data criação", auto_now_add=True, blank=True, null=True)
    # fks
    user            = models.ForeignKey(User, editable=False, related_name="+", on_delete=models.CASCADE)
    discipline      = models.ForeignKey(Discipline, editable=False, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_nome_disciplina(self):
        return self.discipline.title

    def get_username(self):
        return self.user.full_name

    def get_status(self):
        if self.status == 'A':
            return mark_safe('<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Ativo</span>') 
        elif self.status == 'B':
            return mark_safe('<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Bloqueado</span>') 
        else:
            return mark_safe('<span class="kt-badge  kt-badge--warning kt-badge--inline kt-badge--pill">Desativo</span>') 

