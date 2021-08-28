from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import FormView, RedirectView
from websies123 import settings


# Create your views here.


class LoginFornview(FormView):
    form_class = AuthenticationForm
    template_name = 'usuario/login.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar seccion'
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'home'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
