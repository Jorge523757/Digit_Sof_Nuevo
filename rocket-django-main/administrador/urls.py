from django.urls import path
from administrador.views import *

app_name = 'administrador'

urlpatterns = [
 
 # URLs para Administrador
 path('administrador/listar/', AdministradorListView.as_view() , name='administrador_listar'),
 path('administrador/crear/', AdministradorCreateView.as_view(), name='administrador_crear'),
 path('administrador/editar/<int:pk>/', AdministradorUpdateView.as_view(), name='administrador_editar'),
 path('administrador/eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),
 
 # URLs para Facturacion
 path('facturacion/listar/', FacturacionListView.as_view() , name='facturacion_listar'),
 path('facturacion/crear/', FacturacionCreateView.as_view(), name='facturacion_crear'),
 path('facturacion/editar/<int:pk>/', FacturacionUpdateView.as_view(), name='facturacion_editar'),
 path('facturacion/eliminar/<int:pk>/', FacturacionDeleteView.as_view(), name='facturacion_eliminar'),

 # URLs para Cliente
 path('cliente/listar/', ClienteListView.as_view(), name='cliente_listar'),
 path('cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
 path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
 path('cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
 
 # URLs para Marca
 path('marca/listar/', MarcaListView.as_view(), name='marca_listar'),
 path('marca/crear/', MarcaCreateView.as_view(), name='marca_crear'),
 path('marca/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marca_editar'),
 path('marca/eliminar/<int:pk>/', MarcaDeleteView.as_view(), name='marca_eliminar'),
 
 # URLs para Proveedor
 path('proveedor/listar/', ProveedorListView.as_view(), name='proveedor_listar'),
 path('proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
 path('proveedor/editar/<str:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
 path('proveedor/eliminar/<str:pk>/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),

 # URLs para Producto
 path('producto/listar/', ProductoListView.as_view(), name='producto_listar'),
 path('producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
 path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
 path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),

 # URLs para Equipo
 path('equipo/listar/', EquipoListView.as_view(), name='equipo_listar'),
 path('equipo/crear/', EquipoCreateView.as_view(), name='equipo_crear'),
 path('equipo/editar/<int:pk>/', EquipoUpdateView.as_view(), name='equipo_editar'),
 path('equipo/eliminar/<int:pk>/', EquipoDeleteView.as_view(), name='equipo_eliminar'),

 # URLs para Tecnico
 # URLs para Tecnico
 path('tecnico/listar/', TecnicoListView.as_view(), name='tecnico_listar'),
 path('tecnico/crear/', TecnicoCreateView.as_view(), name='tecnico_crear'),
 path('tecnico/editar/<int:pk>/', TecnicoUpdateView.as_view(), name='tecnico_editar'),
 path('tecnico/eliminar/<int:pk>/', TecnicoDeleteView.as_view(), name='tecnico_eliminar'), 

 # URLs para OrdenServicio
 path('ordenservicio/listar/', OrdenServicioListView.as_view(), name='ordenservicio_listar'),
 path('ordenservicio/crear/', OrdenServicioCreateView.as_view(), name='ordenservicio_crear'),
 path('ordenservicio/editar/<int:pk>/', OrdenServicioUpdateView.as_view(), name='ordenservicio_editar'),
 path('ordenservicio/eliminar/<int:pk>/', OrdenServicioDeleteView.as_view(), name='ordenservicio_eliminar'),

 # URLs para ServicioTecnico
 path('serviciotecnico/listar/', ServicioTecnicoListView.as_view(), name='serviciotecnico_listar'),
 path('serviciotecnico/crear/', ServicioTecnicoCreateView.as_view(), name='serviciotecnico_crear'),
 path('serviciotecnico/editar/<int:pk>/', ServicioTecnicoUpdateView.as_view(), name='serviciotecnico_editar'),
 path('serviciotecnico/eliminar/<int:pk>/', ServicioTecnicoDeleteView.as_view(), name='serviciotecnico_eliminar'),

 # URLs para Venta
 path('venta/listar/', VentaListView.as_view(), name='venta_listar'),
 path('venta/crear/', VentaCreateView.as_view(), name='venta_crear'),
 path('venta/editar/<int:pk>/', VentaUpdateView.as_view(), name='venta_editar'),
 path('venta/eliminar/<int:pk>/', VentaDeleteView.as_view(), name='venta_eliminar'),

 # URLs para ComprasMercancia
 path('comprasmercancia/listar/', ComprasMercanciaListView.as_view(), name='comprasmercancia_listar'),
 path('comprasmercancia/crear/', ComprasMercanciaCreateView.as_view(), name='comprasmercancia_crear'),
 path('comprasmercancia/editar/<int:pk>/', ComprasMercanciaUpdateView.as_view(), name='comprasmercancia_editar'),
 path('comprasmercancia/eliminar/<int:pk>/', ComprasMercanciaDeleteView.as_view(), name='comprasmercancia_eliminar'),

 # URLs para Garantias
 path('garantias/listar/', GarantiasListView.as_view(), name='garantias_listar'),
 path('garantias/crear/', GarantiasCreateView.as_view(), name='garantias_crear'),
 path('garantias/editar/<int:pk>/', GarantiasUpdateView.as_view(), name='garantias_editar'),
 path('garantias/eliminar/<int:pk>/', GarantiasDeleteView.as_view(), name='garantias_eliminar'),
]