from django.urls import path
from .views import (
    AdministradorListView,
    AdministradorCreateView,
    AdministradorUpdateView,
    AdministradorDeleteView,
)

urlpatterns = [
    path('administradores/', AdministradorListView.as_view(), name='administrador_listar'),
    path('administradores/nuevo/', AdministradorCreateView.as_view(), name='administrador_crear'),
    path('administradores/editar/<int:pk>/', AdministradorUpdateView.as_view(), name='administrador_editar'),
    path('administradores/eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),
]
