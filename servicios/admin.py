from django.contrib import admin
from servicios.models import ClasesServicioModel, ServiciosModel

# Register your models here.


class ClasesServiciosAdmin(admin.ModelAdmin):
    search_fields = ['servicios']
    list_display = ('codigo', 'servicios')
    readonly_fields = ('created', 'updated')


class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'servicios', 'fecha')
    autocomplete_fields = ['servicios']
    readonly_fields = ('created', 'updated')


admin.site.register(ClasesServicioModel, ClasesServiciosAdmin)
admin.site.register(ServiciosModel, ServiciosAdmin)
