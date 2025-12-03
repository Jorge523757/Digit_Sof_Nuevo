"""
DIGIT SOFT - Script de Verificación Rápida del Sistema
Ejecutar: python verificar_sistema_rapido.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from clientes.models import Cliente
from tecnicos.models import Tecnico
from productos.models import Producto, CategoriaProducto
from proveedores.models import Proveedor

User = get_user_model()

print("=" * 70)
print("   🔍 VERIFICACIÓN DEL SISTEMA DIGIT SOFT")
print("=" * 70)

# Verificar Usuarios
print("\n👤 USUARIOS:")
total_users = User.objects.count()
superusers = User.objects.filter(is_superuser=True).count()
print(f"   Total de usuarios: {total_users}")
print(f"   Superusuarios: {superusers}")

if superusers > 0:
    admin = User.objects.filter(is_superuser=True).first()
    print(f"   ✓ Superusuario principal: {admin.username}")
    print(f"   ✓ Email: {admin.email}")
else:
    print("   ⚠️ NO hay superusuarios creados")

# Verificar Clientes
print("\n👥 CLIENTES:")
total_clientes = Cliente.objects.count()
clientes_activos = Cliente.objects.filter(activo=True).count()
print(f"   Total de clientes: {total_clientes}")
print(f"   Clientes activos: {clientes_activos}")
if total_clientes > 0:
    print("   ✓ Ejemplos:")
    for cliente in Cliente.objects.all()[:3]:
        print(f"      - {cliente.nombre_completo} ({cliente.numero_documento})")
else:
    print("   ⚠️ NO hay clientes en la base de datos")

# Verificar Técnicos
print("\n👷 TÉCNICOS:")
total_tecnicos = Tecnico.objects.count()
tecnicos_activos = Tecnico.objects.filter(activo=True).count()
print(f"   Total de técnicos: {total_tecnicos}")
print(f"   Técnicos activos: {tecnicos_activos}")
if total_tecnicos > 0:
    print("   ✓ Ejemplos:")
    for tecnico in Tecnico.objects.all()[:3]:
        print(f"      - {tecnico.nombres} {tecnico.apellidos} - {tecnico.profesion}")
else:
    print("   ⚠️ NO hay técnicos en la base de datos")

# Verificar Productos
print("\n📦 PRODUCTOS:")
total_productos = Producto.objects.count()
productos_activos = Producto.objects.filter(activo=True).count()
total_categorias = CategoriaProducto.objects.count()
print(f"   Total de productos: {total_productos}")
print(f"   Productos activos: {productos_activos}")
print(f"   Categorías: {total_categorias}")
if total_productos > 0:
    print("   ✓ Ejemplos:")
    for producto in Producto.objects.all()[:3]:
        print(f"      - {producto.nombre_producto} ({producto.codigo_sku}) - ${producto.precio_venta:,.0f}")
else:
    print("   ⚠️ NO hay productos en la base de datos")

# Verificar Proveedores
print("\n🏢 PROVEEDORES:")
total_proveedores = Proveedor.objects.count()
proveedores_activos = Proveedor.objects.filter(activo=True).count()
print(f"   Total de proveedores: {total_proveedores}")
print(f"   Proveedores activos: {proveedores_activos}")
if total_proveedores > 0:
    print("   ✓ Ejemplos:")
    for proveedor in Proveedor.objects.all()[:3]:
        estrellas = "⭐" * proveedor.calificacion
        print(f"      - {proveedor.nombre_empresa} {estrellas}")
else:
    print("   ⚠️ NO hay proveedores en la base de datos")

# Resumen
print("\n" + "=" * 70)
print("   📊 RESUMEN GENERAL")
print("=" * 70)

estado_general = "✅ SISTEMA LISTO" if (
    superusers > 0 and
    total_clientes > 0 and
    total_tecnicos > 0 and
    total_productos > 0 and
    total_proveedores > 0
) else "⚠️ FALTAN DATOS"

print(f"\n   Estado: {estado_general}")
print(f"\n   📋 Base de Datos:")
print(f"      - Usuarios: {total_users}")
print(f"      - Clientes: {total_clientes}")
print(f"      - Técnicos: {total_tecnicos}")
print(f"      - Productos: {total_productos}")
print(f"      - Proveedores: {total_proveedores}")

print("\n" + "=" * 70)
print("   🌐 ACCESOS AL SISTEMA")
print("=" * 70)
print("\n   Panel de Administración:")
print("      URL: http://127.0.0.1:8000/admin/")
print("      Usuario: admin")
print("      Contraseña: admin123")
print("\n   Aplicación Web:")
print("      URL: http://127.0.0.1:8000/")
print("\n" + "=" * 70)

if estado_general == "✅ SISTEMA LISTO":
    print("   ✨ ¡El sistema está completamente configurado y listo para usar! ✨")
else:
    print("   ⚠️ Ejecuta 'python agregar_datos_prueba_rapido.py' para agregar datos")

print("=" * 70)

