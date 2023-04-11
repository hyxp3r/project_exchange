# Generated by Django 4.1.6 on 2023-03-05 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_program_department_program_department'),
        ('users', '0003_alter_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booknumber', models.BigIntegerField(verbose_name='Номер зачетки')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group', verbose_name='Группа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студент',
            },
        ),
    ]
