# Generated by Django 3.2.6 on 2021-08-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clasesserviciomodel',
            old_name='servicio',
            new_name='servicios',
        ),
    ]
