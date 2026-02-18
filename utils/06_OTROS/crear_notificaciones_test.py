"""
Script para crear notificaciones de prueba
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import Notificacion

def crear_notificaciones_prueba():
    """Crea notificaciones de prueba para todos los usuarios"""

    usuarios = User.objects.all()

    if not usuarios.exists():
        print("❌ No hay usuarios en el sistema.")
        print("   Crea un usuario primero con: python manage.py createsuperuser")
        return

    print(f"✅ Encontrados {usuarios.count()} usuario(s)")
    print()

    tipos_notificaciones = [
        {
            'titulo': '¡Bienvenido a DIGITSOFT!',
            'mensaje': 'Tu cuenta ha sido configurada exitosamente. Explora todas las funcionalidades del sistema.',
            'tipo': 'SUCCESS',
        },
        {
            'titulo': 'Nueva Venta Registrada',
            'mensaje': 'Se ha registrado una nueva venta por $1,250.00 MXN al cliente Juan Pérez.',
            'tipo': 'VENTA',
            'url': '/ventas/',
        },
        {
            'titulo': 'Orden de Servicio Pendiente',
            'mensaje': 'Tienes una orden de servicio pendiente asignada para hoy. Revisa los detalles.',
            'tipo': 'ORDEN',
            'url': '/ordenes/',
        },
        {
            'titulo': 'Stock Bajo en Productos',
            'mensaje': 'El producto "Laptop HP Pavilion" tiene solo 3 unidades en stock. Considera hacer un pedido.',
            'tipo': 'WARNING',
            'url': '/productos/',
        },
        {
            'titulo': 'Compra Completada',
            'mensaje': 'Se ha registrado una nueva compra de mercancía del proveedor TechSupply por $5,000.00 MXN.',
            'tipo': 'COMPRA',
            'url': '/compras/',
        },
        {
            'titulo': 'Actualización del Sistema',
            'mensaje': 'El sistema ha sido actualizado con nuevas funcionalidades. Revisa las notas de la versión.',
            'tipo': 'SISTEMA',
        },
        {
            'titulo': 'Pago Pendiente',
            'mensaje': 'Tienes un pago pendiente de factura #FAC-00123. Vence en 3 días.',
            'tipo': 'WARNING',
            'url': '/facturacion/',
        },
        {
            'titulo': 'Cliente Nuevo Registrado',
            'mensaje': 'El cliente "María González" se ha registrado en el sistema. Revisa su perfil.',
            'tipo': 'INFO',
            'url': '/clientes/',
        },
    ]

    for usuario in usuarios:
        print(f"Creando notificaciones para: {usuario.username}")

        for notif_data in tipos_notificaciones:
            notif, created = Notificacion.objects.get_or_create(
                usuario=usuario,
                titulo=notif_data['titulo'],
                defaults={
                    'mensaje': notif_data['mensaje'],
                    'tipo': notif_data['tipo'],
                    'url': notif_data.get('url', ''),
                    'leida': False
                }
            )

            if created:
                print(f"  ✅ {notif_data['titulo']}")
            else:
                print(f"  ⏭️  {notif_data['titulo']} (ya existe)")

        print()

    total = Notificacion.objects.count()
    no_leidas = Notificacion.objects.filter(leida=False).count()

    print("="*60)
    print(f"✅ Proceso completado")
    print(f"📊 Total de notificaciones: {total}")
    print(f"📬 Notificaciones no leídas: {no_leidas}")
    print("="*60)

if __name__ == "__main__":
    print("="*60)
    print("DIGITSOFT - Crear Notificaciones de Prueba")
    print("="*60)
    print()

    try:
        crear_notificaciones_prueba()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

