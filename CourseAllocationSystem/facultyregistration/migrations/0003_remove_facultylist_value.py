# Generated by Django 3.0.3 on 2020-03-06 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyregistration', '0002_facultylist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultylist',
            name='Value',
        ),
    ]
