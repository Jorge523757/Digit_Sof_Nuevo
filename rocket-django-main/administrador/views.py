from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Administrador
from .forms import AdministradorForm

# Listar
class AdministradorListView(ListView):
    model = Administrador
    template_name = "categoria/listar_administrador.html"
    context_object_name = "administradores"

# Crear
class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "categoria/administrador_form.html"
    success_url = reverse_lazy('administrador_listar')

# Editar
class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "categoria/administrador_form.html"
    success_url = reverse_lazy('administrador_listar')

# Eliminar
class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = "categoria/administrador_confirm_delete.html"
    success_url = reverse_lazy('administrador_listar')
