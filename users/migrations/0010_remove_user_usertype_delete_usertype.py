# Generated by Django 4.1.6 on 2023-03-24 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userType',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
