# Generated by Django 5.1.7 on 2025-03-17 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0010_exammodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')], max_length=100)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam_app.exammodel')),
            ],
        ),
    ]
