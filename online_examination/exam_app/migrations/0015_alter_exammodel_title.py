# Generated by Django 5.1.7 on 2025-03-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0014_alter_exammodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
