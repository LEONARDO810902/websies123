from django.db import models
from django.forms import ModelForm

# Create your models here.


class Estado(models.Model):
    estado = models.CharField(max_length=30)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return (self.estado)


class NumExtension(models.Model):
    extension = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "NumExtension"
        verbose_name_plural = "NumExtensiones"

    def __str__(self):
        return (self.extension)


class DirExtencion(models.Model):
    grado = models.CharField(max_length=6)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    sigla = models.CharField(max_length=20)
    extension = models.OneToOneField(
        NumExtension, null=True, blank=True, unique=True, on_delete=models.CASCADE)
    pin = models.CharField(max_length=4)
    estado = models.ForeignKey(
        Estado, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "DirExtencione"
        verbose_name_plural = "DirExtenciones"

    def __str__(self):
        cadena = self.apellidos+"  "+self.nombre
        return cadena
