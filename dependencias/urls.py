from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from dependencias.views import DependenciasListado, DependenciaCreate, DependenciaUpdate, DependenciaConsulta


urlpatterns = [
    # paths del dependencia

    path('dependencia/listado/',
         DependenciasListado.as_view(), name="dep_listado"),
    path('dependencia/nuevo/', DependenciaCreate.as_view(), name="dep_nuevo"),
    path('dependencia/editar/<int:pk>',
         DependenciaUpdate.as_view(), name="dep_editar"),
    path('dependencia/consultalistado',
         DependenciaConsulta.as_view(), name='dep_consulta')
]
