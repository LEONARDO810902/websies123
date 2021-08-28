from django import forms
from django.forms import fields, widgets

from dependencias.models import Dependencia


class DependenciaForms(forms.ModelForm):

    class Meta:
        model = Dependencia

        fields = [
            'dependencia',
            'unidad',
            'telefono',
            'celular',
            'email',
            'direccion',
            'municipio',


        ]
        labels = {
            'dependencia': 'Dependencia',
            'unidad': 'Unidad',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'email': 'Correo',
            'direccion': 'Direccion',
            'municipio': 'Municipio',


        }
        widgets = {
            'dependencia': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),


        }
