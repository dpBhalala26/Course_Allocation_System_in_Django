# Generated by Django 3.0.3 on 2020-03-17 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyregistration', '0015_deptmembers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deptmembers',
            name='priority1',
        ),
        migrations.RemoveField(
            model_name='deptmembers',
            name='priority2',
        ),
        migrations.RemoveField(
            model_name='deptmembers',
            name='priority3',
        ),
        migrations.RemoveField(
            model_name='deptmembers',
            name='priority4',
        ),
        migrations.RemoveField(
            model_name='deptmembers',
            name='priority5',
        ),
    ]