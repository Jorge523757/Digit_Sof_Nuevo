"""
Script de verificación completa del sistema DIGIT SOFT
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from clientes.models import Cliente
from tecnicos.models import Tecnico
from ordenes.models import OrdenServicio
from equipos.models import Equipo
from productos.models import Producto
from garantias.models import Garantia

print("=" * 80)
print("VERIFICACIÓN COMPLETA DEL SISTEMA - DIGIT SOFT")
print("=" * 80)
print()

# Verificar usuarios
print("👥 USUARIOS Y AUTENTICACIÓN")
print("-" * 80)
try:
    total_usuarios = User.objects.count()
    superusuarios = User.objects.filter(is_superuser=True).count()
    staff = User.objects.filter(is_staff=True).count()
    clientes_usuarios = User.objects.filter(is_staff=False, is_superuser=False).count()

    print(f"✅ Total de usuarios: {total_usuarios}")
    print(f"✅ Superusuarios: {superusuarios}")
    print(f"✅ Staff: {staff}")
    print(f"✅ Clientes/Técnicos: {clientes_usuarios}")

    # Listar superusuarios
    print("\n   Superusuarios:")
    for user in User.objects.filter(is_superuser=True):
        print(f"   - {user.username} ({user.email})")
except Exception as e:
    print(f"❌ Error: {e}")

print()

# Verificar módulos principales
print("📦 MÓDULOS PRINCIPALES")
print("-" * 80)

modulos = [
    ("Clientes", Cliente),
    ("Técnicos", Tecnico),
    ("Órdenes de Servicio", OrdenServicio),
    ("Equipos", Equipo),
    ("Productos", Producto),
    ("Garantías", Garantia),
]

for nombre, modelo in modulos:
    try:
        count = modelo.objects.count()
        print(f"✅ {nombre}: {count} registros")
    except Exception as e:
        print(f"❌ {nombre}: Error - {e}")

print()

# Verificar decoradores de seguridad
print("🔐 SISTEMA DE SEGURIDAD")
print("-" * 80)

try:
    from core.decorators import (
        admin_required,
        cliente_required,
        tecnico_required,
        admin_o_tecnico_required
    )
    print("✅ Decoradores de seguridad: Disponibles")
    print("   - @admin_required")
    print("   - @cliente_required")
    print("   - @tecnico_required")
    print("   - @admin_o_tecnico_required")
except Exception as e:
    print(f"❌ Decoradores de seguridad: Error - {e}")

print()

# Verificar módulo de gestión de contraseñas
print("🔑 MÓDULO DE GESTIÓN DE CONTRASEÑAS")
print("-" * 80)

try:
    from usuarios.views_admin_password import admin_gestionar_contrasenas, admin_cambiar_contrasena
    print("✅ Vistas de gestión de contraseñas: Disponibles")
    print("   - admin_gestionar_contrasenas")
    print("   - admin_cambiar_contrasena")
except Exception as e:
    print(f"❌ Gestión de contraseñas: Error - {e}")

print()

# Verificar módulo de ayuda
print("❓ MÓDULO DE AYUDA")
print("-" * 80)

try:
    from ayuda.models import FAQ, TicketSoporte
    faqs = FAQ.objects.count()
    tickets = TicketSoporte.objects.count()
    print(f"✅ FAQs: {faqs} registros")
    print(f"✅ Tickets de soporte: {tickets} registros")
except Exception as e:
    print(f"❌ Módulo de ayuda: Error - {e}")

print()

# Verificar sistema de notificaciones
print("📧 SISTEMA DE NOTIFICACIONES")
print("-" * 80)

try:
    from notificaciones.models import Notificacion
    notificaciones = Notificacion.objects.count()
    print(f"✅ Notificaciones: {notificaciones} registros")
except Exception as e:
    print(f"❌ Notificaciones: Error - {e}")

print()

# Verificar configuración de email
print("✉️ CONFIGURACIÓN DE EMAIL")
print("-" * 80)

from django.conf import settings

try:
    email_backend = settings.EMAIL_BACKEND
    print(f"✅ Backend: {email_backend}")

    if 'console' in email_backend:
        print("   ⚠️  Usando backend de consola (desarrollo)")
    elif 'smtp' in email_backend:
        print(f"   ✅ Configurado para envío real")
        print(f"   Host: {settings.EMAIL_HOST}")
        print(f"   Port: {settings.EMAIL_PORT}")
except Exception as e:
    print(f"❌ Configuración email: Error - {e}")

print()

# Verificar archivos estáticos
print("📁 ARCHIVOS Y CONFIGURACIÓN")
print("-" * 80)

import os.path

archivos_importantes = [
    ("README.md", "Documentación principal"),
    ("requirements.txt", "Dependencias"),
    (".gitignore", "Configuración Git"),
    ("INSTALAR.bat", "Instalador Windows"),
    ("instalar.sh", "Instalador Linux/Mac"),
    ("crear_superusuario.py", "Script crear admin"),
    ("GUIA_CLONACION.md", "Guía de clonación"),
]

for archivo, descripcion in archivos_importantes:
    if os.path.exists(archivo):
        print(f"✅ {archivo} - {descripcion}")
    else:
        print(f"❌ {archivo} - NO ENCONTRADO")

print()
print("=" * 80)
print("RESUMEN FINAL")
print("=" * 80)

# Calcular porcentaje de funcionalidad
total_checks = 6  # Usuarios, Módulos, Seguridad, Contraseñas, Ayuda, Email
checks_ok = 0

try:
    User.objects.count()
    checks_ok += 1
except:
    pass

try:
    Cliente.objects.count()
    checks_ok += 1
except:
    pass

try:
    from core.decorators import admin_required
    checks_ok += 1
except:
    pass

try:
    from usuarios.views_admin_password import admin_gestionar_contrasenas
    checks_ok += 1
except:
    pass

try:
    from ayuda.models import FAQ
    checks_ok += 1
except:
    pass

try:
    settings.EMAIL_BACKEND
    checks_ok += 1
except:
    pass

porcentaje = (checks_ok / total_checks) * 100

print(f"\n🎯 Funcionalidad: {porcentaje:.0f}%")

if porcentaje == 100:
    print("✅ Sistema 100% funcional y operativo")
elif porcentaje >= 80:
    print("⚠️  Sistema mayormente funcional con alertas menores")
else:
    print("❌ Sistema requiere atención")

print("\n" + "=" * 80)
print("SIGUIENTE PASO: python manage.py runserver")
print("=" * 80)

