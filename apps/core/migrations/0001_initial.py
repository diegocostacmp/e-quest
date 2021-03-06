# Generated by Django 2.0.2 on 2019-09-02 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('username', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identificador Unico')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('birth_date', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('sex', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=10, null=True, verbose_name='Sexo')),
                ('marital_status', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')], max_length=10, null=True, verbose_name='Estado Civil')),
                ('phone', models.CharField(max_length=19, null=True, verbose_name='Telefone')),
                ('street', models.CharField(max_length=150, null=True, verbose_name='Logradouro')),
                ('street_number', models.PositiveIntegerField(null=True, verbose_name='Número')),
                ('complement', models.CharField(max_length=200, verbose_name='Complemento')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia '), ('CE', 'Ceará'), ('DF', 'Distrito Federal '), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=15, null=True)),
                ('city', models.CharField(max_length=40, null=True, verbose_name='Cidade')),
                ('type_profile', models.CharField(max_length=10, null=True, verbose_name='Tipo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Digite o nome da Discipline', max_length=128, verbose_name='Título')),
                ('description', models.CharField(blank=True, default=None, help_text='Digite a descrição da Discipline', max_length=512, null=True, verbose_name='Descrição')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identificador Único')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data criação')),
                ('date_edit', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('B', 'Bloqueado'), ('D', 'Desativado')], default='A', max_length=15)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Professor')),
                ('user_create', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplines_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('B', 'Bloqueado'), ('D', 'Desativado')], default='A', max_length=15)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identificador Único')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data criação')),
                ('discipline', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Discipline')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
