# Generated by Django 4.1.6 on 2023-10-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_mail_applicationbuisness_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customergoal',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
    ]
