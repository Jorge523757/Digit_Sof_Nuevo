"""
Script para crear técnicos de prueba
Ejecutar con: python manage.py shell < crear_tecnicos_prueba.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tecnicos.models import Tecnico

# Datos de técnicos de prueba
tecnicos_data = [
    {
        'nombres': 'Carlos Andrés',
        'apellidos': 'Ramírez González',
        'numero_documento': '1234567890',
        'telefono': '3001234567',
        'correo': 'carlos.ramirez@digtsoft.com',
        'profesion': 'Ingeniero de Sistemas',
        'activo': True
    },
    {
        'nombres': 'María Fernanda',
        'apellidos': 'López Martínez',
        'numero_documento': '1234567891',
        'telefono': '3002345678',
        'correo': 'maria.lopez@digtsoft.com',
        'profesion': 'Técnica en Electrónica',
        'activo': True
    },
    {
        'nombres': 'Juan Pablo',
        'apellidos': 'Rodríguez Silva',
        'numero_documento': '1234567892',
        'telefono': '3003456789',
        'correo': 'juan.rodriguez@digtsoft.com',
        'profesion': 'Técnico en Redes',
        'activo': True
    },
    {
        'nombres': 'Ana Isabel',
        'apellidos': 'García Torres',
        'numero_documento': '1234567893',
        'telefono': '3004567890',
        'correo': 'ana.garcia@digtsoft.com',
        'profesion': 'Ingeniera Electrónica',
        'activo': True
    },
    {
        'nombres': 'Luis Fernando',
        'apellidos': 'Hernández Pérez',
        'numero_documento': '1234567894',
        'telefono': '3005678901',
        'correo': 'luis.hernandez@digtsoft.com',
        'profesion': 'Técnico en Computación',
        'activo': False
    },
    {
        'nombres': 'Sandra Patricia',
        'apellidos': 'Moreno Castro',
        'numero_documento': '1234567895',
        'telefono': '3006789012',
        'correo': 'sandra.moreno@digtsoft.com',
        'profesion': 'Ingeniera en Software',
        'activo': True
    },
    {
        'nombres': 'Diego Alejandro',
        'apellidos': 'Vargas Ruiz',
        'numero_documento': '1234567896',
        'telefono': '3007890123',
        'correo': 'diego.vargas@digtsoft.com',
        'profesion': 'Técnico en Telecomunicaciones',
        'activo': True
    },
    {
        'nombres': 'Laura Cristina',
        'apellidos': 'Sánchez Jiménez',
        'numero_documento': '1234567897',
        'telefono': '3008901234',
        'correo': 'laura.sanchez@digtsoft.com',
        'profesion': 'Ingeniera en Telecomunicaciones',
        'activo': True
    },
    {
        'nombres': 'Oscar Mauricio',
        'apellidos': 'Gutiérrez Medina',
        'numero_documento': '1234567898',
        'telefono': '3009012345',
        'correo': 'oscar.gutierrez@digtsoft.com',
        'profesion': 'Técnico en Mantenimiento',
        'activo': False
    },
    {
        'nombres': 'Paola Andrea',
        'apellidos': 'Rojas Mendoza',
        'numero_documento': '1234567899',
        'telefono': '3000123456',
        'correo': 'paola.rojas@digtsoft.com',
        'profesion': 'Ingeniera en Electrónica',
        'activo': True
    }
]

print("=" * 60)
print("CREANDO TÉCNICOS DE PRUEBA")
print("=" * 60)

creados = 0
existentes = 0

for data in tecnicos_data:
    try:
        # Verificar si ya existe
        if Tecnico.objects.filter(numero_documento=data['numero_documento']).exists():
            print(f"⚠️  Técnico con documento {data['numero_documento']} ya existe")
            existentes += 1
            continue
        
        # Crear técnico
        tecnico = Tecnico.objects.create(**data)
        print(f"✅ Técnico creado: {tecnico.nombre_completo} - {tecnico.profesion}")
        creados += 1
    except Exception as e:
        print(f"❌ Error al crear técnico {data['nombres']}: {str(e)}")

print("=" * 60)
print(f"📊 RESUMEN:")
print(f"   ✅ Técnicos creados: {creados}")
print(f"   ⚠️  Técnicos existentes: {existentes}")
print(f"   📈 Total en sistema: {Tecnico.objects.count()}")
print(f"   🟢 Activos: {Tecnico.objects.filter(activo=True).count()}")
print(f"   🔴 Inactivos: {Tecnico.objects.filter(activo=False).count()}")
print("=" * 60)
print("✅ Proceso completado exitosamente")
print("=" * 60)

