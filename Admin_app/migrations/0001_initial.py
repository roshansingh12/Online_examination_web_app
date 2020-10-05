# Generated by Django 3.0.6 on 2020-10-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=300)),
                ('student_email', models.CharField(max_length=300)),
                ('student_class', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=300)),
                ('teacher_email', models.CharField(max_length=300)),
                ('class1', models.CharField(max_length=300)),
                ('class2', models.CharField(max_length=300)),
                ('class3', models.CharField(max_length=300)),
                ('class4', models.CharField(max_length=300)),
                ('class5', models.CharField(max_length=300)),
            ],
        ),
    ]
