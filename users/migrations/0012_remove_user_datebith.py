# Generated by Django 4.1.6 on 2023-03-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_studentuser_datebith'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dateBith',
        ),
    ]
