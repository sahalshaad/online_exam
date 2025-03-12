# Generated by Django 5.1.7 on 2025-03-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0005_alter_teacher_signup_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_signup',
            new_name='StudentSignup',
        ),
        migrations.RenameModel(
            old_name='teacher_signup',
            new_name='TeacherSignup',
        ),
        migrations.AlterModelOptions(
            name='login',
            options={},
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
