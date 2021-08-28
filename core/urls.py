from django.urls import path
from . import views


urlpatterns = [
    # paths del core

    path('', views.home, name="home"),
]
