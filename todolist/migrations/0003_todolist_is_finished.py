# Generated by Django 4.1 on 2022-10-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
