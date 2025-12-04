from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Página principal

    # E-commerce
    path('tienda/', include('ecommerce_urls')),  # URLs del e-commerce

    # Módulos
    path('usuarios/', include('usuarios.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('clientes/', include('clientes.urls')),
    path('tecnicos/', include('tecnicos.urls')),
    path('ordenes/', include('ordenes.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('productos/', include('productos.urls')),
    path('garantias/', include('garantias.urls')),
    path('compras/', include('compras.urls')),
    path('ventas/', include('ventas.urls')),
    path('checkout/', include('ventas.urls_checkout')),  # Checkout y facturación
    path('facturacion/', include('facturacion.urls')),
    path('equipos/', include('equipos.urls')),
    path('capacitaciones/', include('capacitaciones.urls')),
]

admin.site.site_header = "DIGIT SOFT - Sistema de Gestión"
admin.site.site_title = "DIGIT SOFT Admin"
admin.site.index_title = "Panel de Administración"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
