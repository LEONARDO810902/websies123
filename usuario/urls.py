
from django.urls import path
from usuario.views import LoginFornview, LogoutRedirectView


urlpatterns = [
    # paths del usuario

    path('login', LoginFornview.as_view(), name="login"),
    path('logout', LogoutRedirectView.as_view(), name="logout"),

]
