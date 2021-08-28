from django.urls import path
from . import views

from servicios.views import LisServiciosView, LisServiciosViewHome, CrearServiciosView, ServicioUpdateview

urlpatterns = [
    # paths del servicios

    path('servicios/listado', LisServiciosView.as_view(), name="Ser_listado"),
    path('servicios/home', LisServiciosViewHome.as_view(), name="Ser_listado_home"),
    path('servicios/nuevo', CrearServiciosView.as_view(), name="Ser_nuevo"),
    path('servicios/editar/<int:pk>',
         ServicioUpdateview.as_view(), name="Ser_editar"),

]
