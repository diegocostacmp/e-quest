# Generated by Django 2.0.2 on 2019-08-03 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20190731_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='question_related', to='quiz.Question'),
        ),
    ]