# Generated by Django 4.0 on 2023-06-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prof',
            old_name='about',
            new_name='bca',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='designation',
            new_name='lang',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='github',
            new_name='mca',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='interests',
            new_name='tenth',
        ),
        migrations.RenameField(
            model_name='prof',
            old_name='qualification',
            new_name='twelth',
        ),
        migrations.RemoveField(
            model_name='prof',
            name='image',
        ),
        migrations.RemoveField(
            model_name='prof',
            name='tech_skills',
        ),
    ]