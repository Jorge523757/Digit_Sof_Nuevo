import os
import django
import sys

# Configurar Django
sys.path.append(r'C:\Users\jorge\OneDrive\Escritorio\DigitSoftAdelanto\Digit_Sof_Nuevo')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Digit_Sof_Nuevo.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import Notificacion

print("=" * 70)
print("DIAGNÓSTICO COMPLETO - SISTEMA DE NOTIFICACIONES")
print("=" * 70)
print()

# 1. Verificar usuarios
print("1️⃣  VERIFICANDO USUARIOS:")
usuarios = User.objects.all()
print(f"   Total de usuarios: {usuarios.count()}")
for user in usuarios:
    print(f"   - {user.username} (ID: {user.id}, Email: {user.email})")
print()

# 2. Verificar notificaciones
print("2️⃣  VERIFICANDO NOTIFICACIONES:")
notificaciones = Notificacion.objects.all()
print(f"   Total de notificaciones: {notificaciones.count()}")
print()

if notificaciones.exists():
    print("   📊 DESGLOSE POR USUARIO:")
    for user in usuarios:
        total = user.notificaciones.count()
        no_leidas = user.notificaciones.filter(leida=False).count()
        print(f"   - {user.username}: {total} total, {no_leidas} no leídas")
    print()
    
    print("   📋 ÚLTIMAS 5 NOTIFICACIONES:")
    for notif in notificaciones[:5]:
        leida_str = "✅ Leída" if notif.leida else "📬 No leída"
        print(f"   - {notif.titulo} ({leida_str}) - Usuario: {notif.usuario.username}")
else:
    print("   ⚠️  NO HAY NOTIFICACIONES EN LA BASE DE DATOS")
    print("   Ejecutando creación de notificaciones de prueba...")
    print()
    
    # Crear notificaciones de prueba
    admin_user = User.objects.filter(is_superuser=True).first()
    if admin_user:
        notificaciones_test = [
            {
                'titulo': 'Bienvenido a DIGITSOFT!',
                'mensaje': 'Tu cuenta ha sido creada exitosamente. Explora todas las funcionalidades del sistema.',
                'tipo': 'SUCCESS',
                'url': '/dashboard/'
            },
            {
                'titulo': 'Nueva Venta Registrada',
                'mensaje': 'Se ha registrado una nueva venta por valor de $250.000. Revisa los detalles.',
                'tipo': 'VENTA',
                'url': '/ventas/'
            },
            {
                'titulo': 'Stock Bajo en Productos',
                'mensaje': 'Hay 3 productos con stock bajo. Considera realizar una compra.',
                'tipo': 'WARNING',
                'url': '/productos/'
            },
        ]
        
        for notif_data in notificaciones_test:
            Notificacion.objects.create(
                usuario=admin_user,
                **notif_data
            )
        print(f"   ✅ Se crearon {len(notificaciones_test)} notificaciones para {admin_user.username}")
        notificaciones = Notificacion.objects.all()
        print(f"   Total ahora: {notificaciones.count()}")

print()
print("3️⃣  VERIFICANDO ARCHIVOS:")
archivos_check = [
    ('static/js/notificaciones.js', 'JavaScript de notificaciones'),
    ('static/css/click-fix-critical.css', 'CSS de corrección de clicks'),
    ('templates/base_dashboard.html', 'Template base'),
    ('usuarios/views_notificaciones.py', 'Views de notificaciones'),
    ('usuarios/urls.py', 'URLs de usuarios'),
]

for archivo, descripcion in archivos_check:
    ruta = os.path.join(r'C:\Users\jorge\OneDrive\Escritorio\DigitSoftAdelanto\Digit_Sof_Nuevo', archivo)
    existe = os.path.exists(ruta)
    icono = "✅" if existe else "❌"
    print(f"   {icono} {descripcion}: {archivo}")

print()
print("4️⃣  VERIFICANDO URLs:")
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

urls_test = [
    ('usuarios:notificaciones', 'Lista de notificaciones'),
    ('usuarios:notificaciones_json', 'API JSON de notificaciones'),
    ('usuarios:marcar_todas_leidas', 'Marcar todas como leídas'),
]

for url_name, descripcion in urls_test:
    try:
        url = reverse(url_name)
        print(f"   ✅ {descripcion}: {url}")
    except NoReverseMatch:
        print(f"   ❌ {descripcion}: NO ENCONTRADA")

print()
print("5️⃣  TEST DE API (simulado):")
print("   Para probar el API manualmente, visita:")
print("   http://127.0.0.1:8000/usuarios/notificaciones/json/")
print("   (Debes estar autenticado)")

print()
print("=" * 70)
print("DIAGNÓSTICO COMPLETO")
print("=" * 70)
print()
print("📝 RESUMEN:")
print(f"   Usuarios: {usuarios.count()}")
print(f"   Notificaciones: {Notificacion.objects.count()}")
print(f"   No leídas: {Notificacion.objects.filter(leida=False).count()}")
print()
print("🚀 PRÓXIMO PASO:")
print("   1. Ejecuta: python manage.py runserver")
print("   2. Abre: http://127.0.0.1:8000/dashboard/")
print("   3. Presiona F12 y busca mensajes [Notificaciones]")
print("   4. Haz clic en el botón de la campana")
print()
print("=" * 70)

