# Generated by Django 4.2.2 on 2023-07-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expire',
            field=models.DateTimeField(null=True),
        ),
    ]
