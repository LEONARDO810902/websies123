from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from extenciones.models import DirExtencion, NumExtension
from extenciones.forms import DirExtenxionesForm, CrearExtensionForms

# Create your views here.


class ExtensionListadoView(ListView):
    model = DirExtencion
    template_name = 'extenciones/ConExtensionEditar.html'
    queryset = DirExtencion.objects.all().order_by('extension')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ExtensionListadoViewConsulta(ListView):
    model = DirExtencion
    template_name = 'extenciones/ConExtensionConsulta.html'
    queryset = DirExtencion.objects.all().order_by('extension')

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(
                extension__extension__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    @ method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ExtensionCreateView(CreateView):
    model = DirExtencion
    form_class = DirExtenxionesForm
    template_name = 'extenciones/CreExtensioncrea.html'
    success_url = reverse_lazy('ext_listado')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Crear la extension de numero


class ExtensionView(CreateView):
    model = NumExtension
    form_class = CrearExtensionForms
    template_name = 'extenciones/ConExtensionCrearNueva.html'
    success_url = reverse_lazy('ext_nuevo')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ExtensionUpdateview(UpdateView):
    model = DirExtencion
    form_class = DirExtenxionesForm
    template_name = 'extenciones/CreExtensioncrea.html'
    success_url = reverse_lazy('ext_listado')
    queryset = DirExtencion.objects.all()

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
