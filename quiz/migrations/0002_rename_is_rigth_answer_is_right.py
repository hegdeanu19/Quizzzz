# Generated by Django 4.0.2 on 2022-03-01 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_rigth',
            new_name='is_right',
        ),
    ]