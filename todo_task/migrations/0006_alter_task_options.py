# Generated by Django 4.2.3 on 2023-07-31 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_task', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority']},
        ),
    ]