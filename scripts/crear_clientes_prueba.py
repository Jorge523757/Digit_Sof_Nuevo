"""
Script para crear clientes de prueba en el sistema
Ejecutar desde el shell de Django: python manage.py shell < crear_clientes_prueba.py
"""

from clientes.models import Cliente

# Lista de clientes de prueba
clientes_prueba = [
    {
        'nombres': 'Juan Carlos',
        'apellidos': 'Pérez González',
        'numero_documento': '1234567890',
        'telefono': '+57 3201234567',
        'correo': 'juan.perez@example.com',
        'direccion': 'Calle 10 # 15-20, Duitama',
        'activo': True
    },
    {
        'nombres': 'María Fernanda',
        'apellidos': 'Rodríguez López',
        'numero_documento': '9876543210',
        'telefono': '+57 3109876543',
        'correo': 'maria.rodriguez@example.com',
        'direccion': 'Carrera 5 # 8-30, Sogamoso',
        'activo': True
    },
    {
        'nombres': 'Carlos Alberto',
        'apellidos': 'Martínez Silva',
        'numero_documento': '5551234567',
        'telefono': '+57 3155551234',
        'correo': 'carlos.martinez@example.com',
        'direccion': 'Avenida Central # 25-10, Tunja',
        'activo': True
    },
    {
        'nombres': 'Laura Cristina',
        'apellidos': 'Gómez Ramírez',
        'numero_documento': '7778889990',
        'telefono': '+57 3207778889',
        'correo': 'laura.gomez@example.com',
        'direccion': 'Calle 20 # 12-45, Duitama',
        'activo': True
    },
    {
        'nombres': 'Andrés Felipe',
        'apellidos': 'Torres Medina',
        'numero_documento': '4445556667',
        'telefono': '+57 3144445556',
        'correo': 'andres.torres@example.com',
        'direccion': 'Carrera 8 # 15-32, Paipa',
        'activo': False
    },
]

# Crear clientes
clientes_creados = 0
clientes_existentes = 0

print("=" * 60)
print("CREANDO CLIENTES DE PRUEBA")
print("=" * 60)

for datos_cliente in clientes_prueba:
    try:
        # Verificar si ya existe
        if Cliente.objects.filter(numero_documento=datos_cliente['numero_documento']).exists():
            print(f"❌ Cliente {datos_cliente['nombres']} {datos_cliente['apellidos']} ya existe")
            clientes_existentes += 1
        else:
            # Crear el cliente
            cliente = Cliente.objects.create(**datos_cliente)
            print(f"✅ Cliente creado: {cliente.nombre_completo} - Doc: {cliente.numero_documento}")
            clientes_creados += 1
    except Exception as e:
        print(f"❌ Error al crear {datos_cliente['nombres']}: {str(e)}")

print("\n" + "=" * 60)
print(f"RESUMEN:")
print(f"✅ Clientes creados: {clientes_creados}")
print(f"⚠️  Clientes que ya existían: {clientes_existentes}")
print(f"📊 Total de clientes en BD: {Cliente.objects.count()}")
print("=" * 60)

