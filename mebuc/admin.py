from django.contrib import admin
from .models import directoriomebuc

# Register your models here.


class MebucAdmin(admin.ModelAdmin):
    search_fields = ('cai', 'cuadrante',
                     'patrulla', 'telefono', 'celular')
    list_display = ('dependencia', 'cai', 'cuadrante',
                    'patrulla', 'telefono', 'celular')
    readonly_fields = ('created', 'updated')
    autocomplete_fields = ['dependencia']


admin.site.register(directoriomebuc, MebucAdmin)
