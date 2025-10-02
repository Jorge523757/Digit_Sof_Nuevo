from django.urls import path
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
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('gestion-clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('gestion-productos/', views.gestion_productos, name='gestion_productos'),
    path('gestion-proveedores/', views.gestion_proveedores, name='gestion_proveedores'),
    path('gestion-compras/', views.gestion_compras, name='gestion_compras'),
    path('gestion-ventas/', views.gestion_ventas, name='gestion_ventas'),
    path('carrito/', views.carrito, name='carrito'),
    path('gestion-tecnicos/', views.gestion_tecnicos, name='gestion_tecnicos'),
    path('servicio-tecnico/', views.servicio_tecnico, name='servicio_tecnico'),
    path('orden-servicio/', views.orden_servicio, name='orden_servicio'),
    path('gestion-garantias/', views.gestion_garantias, name='gestion_garantias'),
    
    # URLs del sistema de productos y e-commerce
    path('productos/', views.products_view, name='products'),
    path('productos/categoria/<slug:category_slug>/', views.category_products_view, name='category_products'),
    path('producto/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('api/cart/add/', views.add_to_cart_view, name='add_to_cart'),
    path('api/cart/remove/', views.remove_from_cart_view, name='remove_from_cart'),
    path('carrito-compras/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('factura/<int:invoice_id>/', views.invoice_detail_view, name='invoice_detail'),
    path('factura/<int:invoice_id>/pdf/', views.invoice_pdf_view, name='invoice_pdf'),
]