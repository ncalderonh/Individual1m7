# Generated by Django 4.2.2 on 2023-07-05 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_statustask'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='deleted',
        ),
    ]