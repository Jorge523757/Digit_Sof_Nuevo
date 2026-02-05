"""
Script para asignar equipos existentes a clientes
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from equipos.models import Equipo
from clientes.models import Cliente

def asignar_equipos_a_clientes():
    """Asigna equipos sin cliente al primer cliente disponible"""

    # Obtener equipos sin cliente
    equipos_sin_cliente = Equipo.objects.filter(cliente__isnull=True)

    # Obtener el primer cliente
    cliente = Cliente.objects.first()

    if not cliente:
        print("❌ No hay clientes en la base de datos.")
        print("   Crea al menos un cliente primero.")
        return

    if not equipos_sin_cliente.exists():
        print("✅ Todos los equipos ya tienen cliente asignado.")
        return

    # Asignar equipos al cliente
    count = 0
    for equipo in equipos_sin_cliente:
        equipo.cliente = cliente
        equipo.save()
        count += 1
        print(f"✅ Equipo {equipo.codigo_equipo} asignado a {cliente.nombres} {cliente.apellidos}")

    print(f"\n✅ Total: {count} equipos asignados a {cliente.nombres} {cliente.apellidos}")

if __name__ == '__main__':
    print("=== Asignación de Equipos a Clientes ===\n")
    asignar_equipos_a_clientes()

