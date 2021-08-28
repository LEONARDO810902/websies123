from dependencias.models import Dependencia
from django.contrib import admin
from .models import Dependencia

# Register your models here.


class DependenciaAdmin(admin.ModelAdmin):
    search_fields = ['dependencia']
    readonly_fields = ('created', 'updated')
    ordering = ['dependencia']


admin.site.register(Dependencia, DependenciaAdmin)
