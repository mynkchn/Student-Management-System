# Generated by Django 5.1.4 on 2024-12-27 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_id',
            new_name='student_id',
        ),
    ]
