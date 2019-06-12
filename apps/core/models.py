from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    AbstractUser, 
    AbstractBaseUser,
    PermissionsMixin, 
    BaseUserManager
    )

# backend personalizado
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

import uuid

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _



# backend de autenticacao personalizado
from django.contrib.auth.models import BaseUserManager


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
    email                       = models.EmailField(null=False, verbose_name="E-mail", unique=True)
    uid                         = models.UUIDField(verbose_name='Identificador Unico', default=uuid.uuid4, editable=False)
    
    
    cpf                         = models.CharField(max_length=14, null=False, verbose_name="CPF", unique=True)
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


# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         Usuario = get_user_model()
#         if username is None:
#             username = kwargs.get(Usuario.USERNAME_FIELD)
            
#         try:
#             if '@' in username:
#                 Usuario.USERNAME_FIELD = 'email'
#             else:
#                 Usuario.USERNAME_FIELD = 'username'

#             user = Usuario._default_manager.get_by_natural_key(username)
#         except Usuario.DoesNotExist:
#             Usuario().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user    
        
   






