# Generated by Django 2.0.2 on 2019-06-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190613_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
    ]
