from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('servicios/', views.servicios, name='servicios'),
    
    # URLs de autenticación
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/register/<str:role>/', views.register_user_view, name='register_user'),
    path('auth/forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('auth/reset-password/', views.reset_password_view, name='reset_password'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/profile/', views.profile_view, name='profile'),
    path('admin-panel/', views.admin_panel_view, name='admin_panel'),
    path('auth/history/', views.history_view, name='history'),
    path('test-carrito/', views.test_carrito_view, name='test_carrito'),
    
    # Contacto
    path('contact/', views.contact_view, name='contact'),
    
    # OAuth Social Login
    path('auth/google/', views.google_oauth_login, name='google_oauth2_login'),
    path('auth/microsoft/', views.microsoft_oauth_login, name='microsoft_oauth2_login'),
    path('auth/google/callback/', views.google_oauth_callback, name='google_oauth_callback'),
    path('auth/microsoft/callback/', views.microsoft_oauth_callback, name='microsoft_oauth_callback'),
    
    # APIs (mantenidas para compatibilidad)
    path('api/contact/', views.contact_form, name='contact_form'),
    path('api/login/', views.login_form, name='login_form'),
    
    # URLs de los módulos de gestión
    path('admin-panel/', include('main.admin_panel.urls')),
    path('gestion-clientes/', include('main.gestion_clientes.urls')),
    path('gestion-productos/', include('main.gestion_productos.urls')),
    path('gestion-proveedores/', include('main.gestion_proveedores.urls')),
    path('gestion-compras/', include('main.gestion_compras.urls')),
    path('gestion-ventas/', include('main.gestion_ventas.urls')),
    path('carrito/', include('main.carrito.urls')),
    path('gestion-tecnicos/', include('main.gestion_tecnicos.urls')),
    path('servicio-tecnico/', include('main.servicio_tecnico.urls')),
    path('orden-servicio/', include('main.orden_servicio.urls')),
    path('gestion-garantias/', include('main.gestion_garantias.urls')),
    path('facturacion/', include('main.facturacion.urls')),
    path('productos/', include('main.productos.urls')),
]