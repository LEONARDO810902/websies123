from django.urls import path

from extenciones.views import ExtensionListadoView, ExtensionCreateView, ExtensionUpdateview, ExtensionListadoViewConsulta, ExtensionView

urlpatterns = [
    # paths del dependencia

    path('extension/listado/', ExtensionListadoView.as_view(), name="ext_listado"),
    path('extension/crear/', ExtensionView.as_view(), name="ext_extcrear"),
    path('extension/consulta/',
         ExtensionListadoViewConsulta.as_view(), name="ext_consulta"),
    path('extension/nuevo/', ExtensionCreateView.as_view(), name="ext_nuevo"),
    path('extension/editar/<int:pk>',
         ExtensionUpdateview.as_view(), name="ext_editar"),

]
