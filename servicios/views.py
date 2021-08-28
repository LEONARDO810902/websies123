from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from servicios.models import ServiciosModel, ClasesServicioModel
from servicios.forms import CrearServiciosForm


# Create your views here.

class LisServiciosView(ListView):
    model = ServiciosModel
    template_name = 'servicios/ListadoServicios.html'
    queryset = ServiciosModel.objects.all().order_by('fecha').reverse()

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(
                fecha__icontains=query)
        else:
            object_list = self.model.objects.all().order_by('fecha').reverse()
        return object_list

    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LisServiciosViewHome(ListView):
    model = ServiciosModel
    template_name = 'servicios/ServiciosConsulta.html'
    queryset = ServiciosModel.objects.all().order_by('fecha').reverse()

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(
                fecha__icontains=query)
        else:
            object_list = self.model.objects.all().order_by('fecha').reverse()
        return object_list

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Vista para crear los servicios del dia


class CrearServiciosView(CreateView):
    model = ServiciosModel
    form_class = CrearServiciosForm
    template_name = 'servicios/CrearServiciosNuevo.html'
    success_url = reverse_lazy('Ser_nuevo')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ServicioUpdateview(UpdateView):
    model = ServiciosModel
    form_class = CrearServiciosForm
    template_name = 'servicios/CrearServiciosNuevo.html'
    success_url = reverse_lazy('Ser_listado')
    queryset = ServiciosModel.objects.all()

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
