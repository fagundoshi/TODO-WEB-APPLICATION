# Generated by Django 4.0.3 on 2022-05-03 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_todo_time1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='time1',
            new_name='time',
        ),
    ]
