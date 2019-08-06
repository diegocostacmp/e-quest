# Generated by Django 2.0.2 on 2019-08-06 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date_edit',
        ),
        migrations.AddField(
            model_name='game',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data criação'),
        ),
        migrations.AlterField(
            model_name='game',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Discipline', verbose_name='Disciplina'),
        ),
    ]
