from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from mebuc import models

from mebuc.foms import MebucForm
from mebuc.models import directoriomebuc

# Create your views here.


def inicios(request):
    return render(request, "mebuc/inicio.html")


def directorio_view(request):
    if request.method == 'POST':
        form = MebucForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    else:
        form = MebucForm()
    return render(request, 'mebuc/mebuc_forms.html', {'form': form})


def mebuc_listado_dir(request):
    Directoriomebuc = directoriomebuc.objects.all().order_by('cai')
    contexto = {'Directoriomebuc': Directoriomebuc}
    return render(request, 'mebuc/mebuc_listadodir.html', contexto)


def mebuc_edit(request, id_directoriomebuc):
    Directoriomebuc = directoriomebuc.objects.get(id=id_directoriomebuc)
    if request.method == 'GET':
        form = MebucForm(instance=Directoriomebuc)
    else:
        form = MebucForm(request.POST, instance=Directoriomebuc)
        if form.is_valid():
            form.save()
        return redirect('listado')
    return render(request, 'mebuc/mebuc_forms.html', {'form': form})


def mebuc_delete(request, id_directoriomebuc):
    Directoriomebuc = directoriomebuc.objects.get(id=id_directoriomebuc)
    if request.method == 'POST':
        Directoriomebuc.delete()
        return redirect('listado')
    return render(request, 'mebuc/mebuc_delete.html', {' Directoriomebuc':  Directoriomebuc})


class mebuclistado(ListView):
    model = directoriomebuc
    template_name = 'mebuc/mebuc_listadodir.html'
    queryset = directoriomebuc.objects.all().order_by('dependencia')

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(cai__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class mebuclistadoconsulta(ListView):
    model = directoriomebuc
    template_name = 'mebuc/mebuc_listadoconsulta.html'
    queryset = directoriomebuc.objects.all().order_by('dependencia')

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        if query:
            object_list = self.model.objects.filter(cai__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class MebucCreate(CreateView):
    model = directoriomebuc
    form_class = MebucForm
    template_name = 'mebuc/mebuc_forms.html'
    success_url = reverse_lazy('listado')

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MebucUpdate(UpdateView):
    models = directoriomebuc
    form_class = MebucForm
    template_name = 'mebuc/mebuc_forms.html'
    success_url = reverse_lazy('listado')
    queryset = directoriomebuc.objects.all()

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MebucDelete(DeleteView):
    models = directoriomebuc
    template_name = 'mebuc/mebuc_delete.html'
    success_url = reverse_lazy('listado')
    queryset = directoriomebuc.objects.all()

    @ method_decorator(csrf_exempt)
    @ method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
