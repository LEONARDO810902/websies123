from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


from dependencias.models import Dependencia
from dependencias.forms import DependenciaForms

# Create your views here.


class DependenciasListado(ListView):
    model = Dependencia
    template_name = 'dependencia/listadoDependencias.html'
    queryset = Dependencia.objects.all().order_by('dependencia')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DependenciaConsulta(ListView):
    model = Dependencia
    template_name = 'dependencia/listadoDepConsulta.html'
    queryset = Dependencia.objects.all().order_by('dependencia')

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(
                dependencia__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class DependenciaCreate(CreateView):
    model = Dependencia
    form_class = DependenciaForms
    template_name = 'dependencia/dependencia_forms.html'
    success_url = reverse_lazy('dep_listado')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DependenciaUpdate(UpdateView):
    models = Dependencia
    form_class = DependenciaForms
    template_name = 'dependencia/dependencia_forms.html'
    success_url = reverse_lazy('dep_listado')
    queryset = Dependencia.objects.all()

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
