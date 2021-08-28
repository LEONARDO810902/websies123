from mebuc import models
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django.db.models import fields
from extenciones.models import Estado, NumExtension, DirExtencion


class DirExtenxionesForm(forms.ModelForm):
    class Meta:
        model = DirExtencion

        fields = [
            'grado',
            'cedula',
            'nombre',
            'apellidos',
            'sigla',
            'extension',
            'pin',
            'estado',
        ]
        labels = {
            'grado': 'Grado',
            'cedula': 'Cedula',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'sigla': 'Sigla',
            'extension': 'Extension',
            'pin': 'Pin',
            'estado': 'Estado',
        }
        wigets = {
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'extension': forms.Select(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


class CrearExtensionForms(forms.ModelForm):
    class Meta:
        model = NumExtension

        fields = [
            'extension',
        ]
        labels = {
            'extension': 'Extension'
        }
        wigets = {
            'extension': forms.TextInput(attrs={'class': 'form-control'})
        }
