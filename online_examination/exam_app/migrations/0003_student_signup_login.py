# Generated by Django 5.1.7 on 2025-03-11 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_student_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_signup',
            name='login',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam_app.login'),
            preserve_default=False,
        ),
    ]
