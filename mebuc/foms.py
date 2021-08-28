from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from django.forms import fields, widgets

from mebuc.models import directoriomebuc


class MebucForm(forms.ModelForm):

    class Meta:
        model = directoriomebuc

        fields = [
            'dependencia',
            'cai',
            'cuadrante',
            'patrulla',
            'telefono',
            'celular',
        ]
        labels = {
            'dependencia': 'Nombre',
            'cai': 'Nombre de Cai',
            'cuadrate': 'Codigo de Cuadrante',
            'patrulla': 'Patrulla',
            'telefono': 'Telefono Cai',
            'celular': 'Celular del cuadrante'
        }
        widgets = {
            'dependencia': forms.Select(attrs={'class': 'form-control'}),
            # 'dependencia': AutocompleteSelect(directoriomebuc._meta.get_field('dependencia').remote_field, admin.site, attrs={'class': 'form-control'},),
            'cai': forms.TextInput(attrs={'class': 'form-control'}),
            'cuadrante': forms.TextInput(attrs={'class': 'form-control'}),
            'patrulla': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }
