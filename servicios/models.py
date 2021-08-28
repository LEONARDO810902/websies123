from django.db import models

# Create your models here.


class ClasesServicioModel(models.Model):
    codigo = models.CharField(max_length=5, default=None)
    servicios = models.CharField(max_length=60)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = 'servicios'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return (self.servicios)


class ServiciosModel(models.Model):
    grado = models.CharField(max_length=6)
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    celular = models.CharField(max_length=15)
    servicios = models.ForeignKey(
        ClasesServicioModel, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Dia servicio")
    fechaNotificacion = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add="True", verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now="True", verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = 'ServicioModel'
        verbose_name_plural = 'ServiciosModels'

    def __str__(self):
        cadena = self.apellidos + " "+self.nombres + " "+self.celular
        return cadena
