# Generated by Django 3.0.3 on 2020-03-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyregistration', '0009_departmentalcourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('CourseId', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('CoueseName', models.CharField(max_length=50)),
                ('Semester', models.IntegerField()),
            ],
        ),
    ]
