# Generated by Django 2.0.2 on 2019-11-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191113_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_profile',
            field=models.CharField(choices=[('1', 'Professor'), ('2', 'Aluno')], default=None, max_length=1, verbose_name='Tipo do perfil'),
        ),
    ]
