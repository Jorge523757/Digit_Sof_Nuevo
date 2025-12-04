from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_cliente, name='registro'),

    # Recuperación de contraseña
    path('recuperar-password/', views.recuperar_password, name='recuperar_password'),
    path('reset-password/<uuid:token>/', views.reset_password, name='reset_password'),

    # Perfil de usuario
    path('perfil/', views.perfil_view, name='perfil'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),

    # Gestión de usuarios (requiere permisos de admin)
    path('gestionar/', views.listar_usuarios, name='listar_usuarios'),
    path('gestionar/crear/', views.crear_usuario, name='crear_usuario'),
    path('gestionar/<int:user_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('gestionar/<int:user_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('gestionar/<int:user_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('gestionar/<int:user_id>/bloquear/', views.bloquear_usuario, name='bloquear_usuario'),
    path('gestionar/<int:user_id>/desbloquear/', views.desbloquear_usuario, name='desbloquear_usuario'),
    path('gestionar/<int:user_id>/toggle-staff/', views.toggle_staff, name='toggle_staff'),
]



