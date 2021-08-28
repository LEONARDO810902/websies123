from django.db import models


# Create your models here.


class Dependencia(models.Model):
    dependencia = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=80)
    municipio = models.CharField(max_length=50)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Dependencia"
        verbose_name_plural = "Dependencias"

    def __str__(self):
        return (self.dependencia)
