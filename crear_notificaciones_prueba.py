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
from django.utils import timezone

def crear_notificaciones_prueba():
    """Crea notificaciones de prueba para el usuario admin"""

    # Obtener usuario admin
    try:
        user = User.objects.get(username='admin')
    except User.DoesNotExist:
        # Si no existe admin, usar el primer usuario
        user = User.objects.first()
        if not user:
            print("❌ No hay usuarios en el sistema")
            return

    print(f"✅ Creando notificaciones para el usuario: {user.username}")

    # Limpiar notificaciones anteriores
    Notificacion.objects.filter(usuario=user).delete()
    print("🗑️  Notificaciones anteriores eliminadas")

    # Crear notificaciones de diferentes tipos
    notificaciones = [
        {
            'titulo': '¡Bienvenido a DIGITSOFT!',
            'mensaje': 'Gracias por usar nuestro sistema de gestión empresarial. Explora todas las funcionalidades desde el menú lateral.',
            'tipo': 'SUCCESS',
            'url': '/dashboard/'
        },
        {
            'titulo': 'Nueva venta registrada',
            'mensaje': 'Se ha registrado una nueva venta por $1,250,000 COP. El cliente está satisfecho con el servicio.',
            'tipo': 'VENTA',
            'url': '/ventas/'
        },
        {
            'titulo': 'Orden de servicio pendiente',
            'mensaje': 'La orden #OS-000123 está esperando asignación de técnico. Por favor revisa y asigna un técnico disponible.',
            'tipo': 'ORDEN',
            'url': '/ordenes/'
        },
        {
            'titulo': 'Stock bajo en productos',
            'mensaje': 'Hay 5 productos con stock por debajo del mínimo. Revisa el inventario y realiza nuevas compras.',
            'tipo': 'WARNING',
            'url': '/productos/'
        },
        {
            'titulo': 'Compra recibida',
            'mensaje': 'La compra #COMP-00045 ha sido recibida exitosamente del proveedor. Total: $3,500,000 COP',
            'tipo': 'COMPRA',
            'url': '/compras/'
        },
        {
            'titulo': 'Actualización del sistema',
            'mensaje': 'El sistema se actualizará esta noche a las 2:00 AM. Duración estimada: 30 minutos.',
            'tipo': 'SISTEMA',
            'icono': 'fa-cog',
            'color': 'info'
        },
        {
            'titulo': 'Garantía por vencer',
            'mensaje': 'La garantía del producto "Laptop Dell Inspiron" vence en 5 días. Cliente: Juan Pérez.',
            'tipo': 'WARNING',
            'url': '/garantias/'
        },
        {
            'titulo': 'Nueva capacitación disponible',
            'mensaje': 'Se ha programado una capacitación sobre "Reparación de Laptops Avanzada" para el próximo lunes.',
            'tipo': 'INFO',
            'url': '/capacitaciones/'
        },
        {
            'titulo': 'Error en sincronización',
            'mensaje': 'Hubo un error al sincronizar los datos con el servidor remoto. Por favor contacta a soporte técnico.',
            'tipo': 'ERROR',
            'icono': 'fa-exclamation-triangle'
        },
        {
            'titulo': 'Cliente nuevo registrado',
            'mensaje': 'María González se ha registrado como nuevo cliente en el sistema. Revisa su perfil.',
            'tipo': 'INFO',
            'url': '/clientes/'
        }
    ]

    count = 0
    for notif_data in notificaciones:
        Notificacion.objects.create(
            usuario=user,
            titulo=notif_data['titulo'],
            mensaje=notif_data['mensaje'],
            tipo=notif_data['tipo'],
            url=notif_data.get('url', ''),
            icono=notif_data.get('icono', ''),
            color=notif_data.get('color', ''),
            fecha_creacion=timezone.now()
        )
        count += 1
        print(f"   ✓ {notif_data['titulo']}")

    print(f"\n✅ {count} notificaciones creadas exitosamente")
    print(f"\n🎉 ¡Listo! Ahora puedes ver las notificaciones en:")
    print(f"   - El icono de campana en el header")
    print(f"   - La página: http://127.0.0.1:8000/usuarios/notificaciones/")

if __name__ == '__main__':
    try:
        crear_notificaciones_prueba()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

