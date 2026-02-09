from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import views_recuperacion
from . import views_notificaciones

app_name = 'usuarios'

urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_cliente, name='registro'),

    # Recuperación de contraseña con código por email (NUEVO - 30 min)
    path('recuperar/', views_recuperacion.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('verificar-codigo/', views_recuperacion.verificar_codigo, name='verificar_codigo'),
    path('nueva-password/', views_recuperacion.nueva_password, name='nueva_password'),
    path('reenviar-codigo/', views_recuperacion.reenviar_codigo, name='reenviar_codigo'),

    # Recuperación de contraseña (antiguo - mantener por compatibilidad)
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

    # Admin - Gestión de contraseñas
    path('admin/gestionar-contrasenas/', views.admin_gestionar_contrasenas, name='admin_gestionar_contrasenas'),

    # Notificaciones
    path('notificaciones/', views_notificaciones.listar_notificaciones, name='notificaciones'),
    path('notificaciones/json/', views_notificaciones.notificaciones_json, name='notificaciones_json'),
    path('notificaciones/<int:notificacion_id>/marcar-leida/', views_notificaciones.marcar_notificacion_leida, name='marcar_notificacion_leida'),
    path('notificaciones/marcar-todas-leidas/', views_notificaciones.marcar_todas_leidas, name='marcar_todas_leidas'),
    path('notificaciones/<int:notificacion_id>/eliminar/', views_notificaciones.eliminar_notificacion, name='eliminar_notificacion'),

    # Debug
    path('notificaciones/debug/', views_notificaciones.debug_notificaciones, name='debug_notificaciones'),
]



