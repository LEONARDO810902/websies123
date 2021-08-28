from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from mebuc.views import mebuc_edit, mebuclistado, MebucCreate, MebucUpdate, MebucDelete, mebuclistadoconsulta


urlpatterns = [
    # paths del mebuc

    path('inicio/', views.inicios, name="inicio"),
    path('nuevo/', MebucCreate.as_view(), name="nuevo"),
    path('listado/', mebuclistado.as_view(), name="listado"),
    path('editar/<int:pk>', MebucUpdate.as_view(), name="editar"),
    path('eliminar/<int:pk>', MebucDelete.as_view(), name="eliminar"),
    path('mebuc/listadoconsulta',
         mebuclistadoconsulta.as_view(), name="mebuc_consulta"),
]
