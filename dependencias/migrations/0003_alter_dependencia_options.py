# Generated by Django 3.2.6 on 2021-08-19 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependencias', '0002_rename_nombre_dependencia_dependencia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dependencia',
            options={'verbose_name': 'Dependencia', 'verbose_name_plural': 'Dependencias'},
        ),
    ]
