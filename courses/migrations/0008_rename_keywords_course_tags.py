# Generated by Django 3.2 on 2021-06-09 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_suggest_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='keywords',
            new_name='tags',
        ),
    ]
