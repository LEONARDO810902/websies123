from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from django.forms.fields import DateField
from django.contrib import admin
from django.db.models import fields
from django.forms import widgets

from servicios.models import ServiciosModel, ClasesServicioModel


class CrearServiciosForm(forms.ModelForm):
    class Meta:
        model = ServiciosModel

        fields = [
            'grado',
            'apellidos',
            'nombres',
            'celular',
            'servicios',
            'fecha',
            'fechaNotificacion'
        ]
        labels = {
            'grado': 'Grado',
            'apellidos': 'Apellidos',
            'nombres': 'Nombres',
            'celular': 'Celular',
            'servicios': 'Servicios',
            'fecha': 'Fecha',
            'fechaNotificacion': 'FechaNotificacion',
        }
        widgets = {
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'servicios': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'fechaNotificacion': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'})
        }


class CrearClaseServicioForms(forms.ModelForm):
    class Meta:
        model = ClasesServicioModel

        fields = [
            'codigo',
            'servicios',

        ]
        labels = {
            'codigo': 'codigo',
            'servicios': 'Servicios'

        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'servicios': forms.TextInput(attrs={'class': 'form-control'})

        }
