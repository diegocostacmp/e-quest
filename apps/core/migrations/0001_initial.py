# Generated by Django 2.0.2 on 2019-07-09 23:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome_completo', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('username', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identificador Unico')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=10, null=True, verbose_name='Sexo')),
                ('estado_civil', models.CharField(choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')], max_length=10, null=True, verbose_name='Estado Civil')),
                ('telefone', models.CharField(max_length=19, null=True, verbose_name='Telefone')),
                ('logradouro', models.CharField(max_length=150, null=True, verbose_name='Logradouro')),
                ('numero_endereco', models.PositiveIntegerField(null=True, verbose_name='Número')),
                ('complemento_endereco', models.CharField(max_length=200, verbose_name='Complemento')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia '), ('CE', 'Ceará'), ('DF', 'Distrito Federal '), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=15, null=True)),
                ('cidade', models.CharField(max_length=40, null=True, verbose_name='Cidade')),
                ('tipo', models.CharField(max_length=10, null=True, verbose_name='Tipo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
