# Generated by Django 3.2.6 on 2021-08-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extenciones', '0009_alter_dirextencion_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirextencion',
            name='pin',
            field=models.CharField(max_length=4),
        ),
    ]
