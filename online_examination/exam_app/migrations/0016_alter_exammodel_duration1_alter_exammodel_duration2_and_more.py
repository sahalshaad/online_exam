# Generated by Django 5.1.7 on 2025-03-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0015_alter_exammodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='duration1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='duration2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
