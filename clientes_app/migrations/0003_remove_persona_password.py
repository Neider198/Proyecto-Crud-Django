# Generated by Django 3.1 on 2021-02-20 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0002_auto_20210214_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='password',
        ),
    ]
