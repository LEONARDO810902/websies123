# Generated by Django 3.2.6 on 2021-08-23 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='NumExtension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.TextField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
            ],
            options={
                'verbose_name': 'NumExtension',
                'verbose_name_plural': 'NumExtensiones',
            },
        ),
        migrations.CreateModel(
            name='DirExtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=60)),
                ('sigla', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extenciones.estado')),
                ('extension', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extenciones.numextension')),
            ],
            options={
                'verbose_name': 'DirExtencion',
                'verbose_name_plural': 'DirExtencions',
            },
        ),
    ]
