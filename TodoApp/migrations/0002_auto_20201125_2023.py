# Generated by Django 3.1.3 on 2020-11-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoapp',
            old_name='text',
            new_name='todo',
        ),
    ]