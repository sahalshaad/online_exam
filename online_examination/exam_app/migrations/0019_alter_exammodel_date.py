# Generated by Django 5.1.7 on 2025-03-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0018_alter_exammodel_date_alter_exammodel_duration1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
