from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Página principal

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
    path('facturacion/', include('facturacion.urls')),
    path('equipos/', include('equipos.urls')),
    path('capacitaciones/', include('capacitaciones.urls')),
]

admin.site.site_header = "DIGT SOFT - Sistema de Gestión"
admin.site.site_title = "DIGT SOFT Admin"
admin.site.index_title = "Panel de Administración"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)