# Generated by Django 4.2.3 on 2023-07-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_task', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
    ]
