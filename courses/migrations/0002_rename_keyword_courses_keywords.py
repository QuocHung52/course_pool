# Generated by Django 3.2 on 2021-05-02 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='keyword',
            new_name='keywords',
        ),
    ]
