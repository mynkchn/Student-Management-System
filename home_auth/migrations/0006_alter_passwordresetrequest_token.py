# Generated by Django 5.1.3 on 2025-01-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0005_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='xSsn5qvUKHkaSOiFOzK0TciMKUEUNw6s', editable=False, max_length=32, unique=True),
        ),
    ]
