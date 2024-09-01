# Generated by Django 5.1 on 2024-09-01 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_remove_task_status_work_log_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_log',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='work_log_Test', to='Todo.task'),
            preserve_default=False,
        ),
    ]
