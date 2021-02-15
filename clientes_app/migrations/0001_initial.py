# Generated by Django 3.1 on 2021-01-09 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': '"basicos"."Sexo"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': '"basicos"."tipoidentificacion"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=60)),
                ('identificacion', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=10)),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.sexo')),
                ('tipoidentificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.tipoidentificacion')),
            ],
        ),
    ]
