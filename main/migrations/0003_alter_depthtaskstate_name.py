# Generated by Django 4.1.6 on 2023-02-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_depthtaskstate_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depthtaskstate',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
    ]
