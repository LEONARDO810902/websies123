from django.db import models
from django.db.models.fields import CharField

from dependencias.models import Dependencia

# Create your models here.


class directoriomebuc(models.Model):
    dependencia = models.ForeignKey(
        Dependencia, null=True, blank=True, on_delete=models.CASCADE)
    cai = models.CharField(max_length=60)
    cuadrante = models.CharField(max_length=40)
    patrulla = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Mebuc"
        verbose_name_plural = "Mebuc"

    def __str__(self):
        return (self.cuadrante)
