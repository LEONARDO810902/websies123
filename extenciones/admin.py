from django.contrib import admin
from extenciones.models import Estado, NumExtension, DirExtencion

# Register your models here.


class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['estado']
    readonly_fields = ('created', 'updated')


class NumExtensionAdmin(admin.ModelAdmin):
    search_fields = ['extension']
    readonly_fields = ('created', 'updated')
    ordering = ['extension']


class DirExtensionAdmin(admin.ModelAdmin):
    #search_fields = ('nombre', 'apellidos', 'extension', 'estado')
    list_display = ('nombre', 'apellidos', 'extension', 'estado')
    autocomplete_fields = ['estado']
    autocomplete_fields = ['extension']
    readonly_fields = ('created', 'updated')


admin.site.register(Estado, EstadoAdmin)
admin.site.register(NumExtension, NumExtensionAdmin)
admin.site.register(DirExtencion, DirExtensionAdmin)
