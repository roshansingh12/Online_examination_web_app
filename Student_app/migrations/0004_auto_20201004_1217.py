# Generated by Django 3.0.6 on 2020-10-04 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0003_test_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_score',
            old_name='Student_email',
            new_name='student_email',
        ),
        migrations.RenameField(
            model_name='test_status',
            old_name='Student_email',
            new_name='student_email',
        ),
    ]
