from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from apps.usuario.forms import InsertForm

# Create your views here.
class UsuarioIndex(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = ('auth.view_encuesta')
    model = User
    template_name = "usuario/index.html"

class UsuarioInsert(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = ('auth.add_user')
    model = User
    form_class = InsertForm
    template_name = "usuario/insert.html"
    success_url = "/usuario"
