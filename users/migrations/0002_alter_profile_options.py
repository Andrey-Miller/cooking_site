# Generated by Django 5.0.6 on 2024-05-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]
