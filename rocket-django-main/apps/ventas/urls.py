from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:pk>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('venta/registrar/', views.registrar_venta, name='registrar_venta'),
    path('factura/<int:venta_id>/', views.factura, name='factura'),
    
    # URLs para sistema de pedidos - CLIENTES
    path('catalogo/', views.catalogo_publico, name='catalogo_publico'),
    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    
    # URLs para sistema de pedidos - ADMINISTRADORES
    path('admin/pedidos/', views.admin_pedidos, name='admin_pedidos'),
    path('admin/pedido/<int:pedido_id>/procesar/', views.procesar_pedido, name='procesar_pedido'),
    path('admin/pedido/<int:pedido_id>/facturar/', views.facturar_pedido, name='facturar_pedido'),
]