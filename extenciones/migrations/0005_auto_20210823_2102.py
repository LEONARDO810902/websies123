# Generated by Django 3.2.6 on 2021-08-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extenciones', '0004_alter_numextension_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirextencion',
            name='cedula',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='dirextencion',
            name='pin',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='numextension',
            name='numero',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
