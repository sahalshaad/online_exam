# Generated by Django 5.1.7 on 2025-03-17 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0013_rename_duration_exammodel_duration1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
