"""websies123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

from django.conf import settings


urlpatterns = [


    # paths del core
    path('', include('core.urls')),

    # paths del mebuc
    path('', include('mebuc.urls')),

    # paths del usuario
    path('', include('usuario.urls')),

    # paths del extensiones
    path('', include('extenciones.urls')),

    # paths del dependencias
    path('', include('dependencias.urls')),


    # paths del servicios
    path('', include('servicios.urls')),



    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
