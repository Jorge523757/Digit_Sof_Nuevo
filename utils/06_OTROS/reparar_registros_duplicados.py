#!/usr/bin/env python
"""
SCRIPT DE REPARACIÓN - REGISTROS DUPLICADOS
Limpia registros duplicados en la base de datos
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from django.db.models import Count
from clientes.models import Cliente
from usuarios.models import PerfilUsuario
from django.contrib.auth.models import User


def limpiar_clientes_duplicados():
    """Elimina clientes duplicados manteniendo el más reciente"""
    print("\n" + "="*70)
    print("🔧 LIMPIANDO CLIENTES DUPLICADOS")
    print("="*70 + "\n")

    # Encontrar documentos duplicados
    duplicados = Cliente.objects.values('numero_documento').annotate(
        count=Count('id')
    ).filter(count__gt=1)

    if not duplicados.exists():
        print("✅ No se encontraron clientes duplicados\n")
        return

    print(f"⚠️  Se encontraron {duplicados.count()} documentos duplicados\n")

    for dup in duplicados:
        documento = dup['numero_documento']
        clientes = Cliente.objects.filter(numero_documento=documento).order_by('fecha_registro')

        print(f"📋 Documento: {documento}")
        print(f"   Total registros: {clientes.count()}")

        # Mantener el más reciente, eliminar los demás
        clientes_a_eliminar = list(clientes[:-1])
        cliente_a_mantener = clientes.last()

        for cliente in clientes_a_eliminar:
            # Verificar si tiene perfiles vinculados
            perfiles = PerfilUsuario.objects.filter(cliente=cliente)

            if perfiles.exists():
                print(f"   ⚠️  El cliente ID {cliente.id} tiene {perfiles.count()} perfil(es) vinculado(s)")
                # Reasignar perfiles al cliente que mantenemos
                for perfil in perfiles:
                    perfil.cliente = cliente_a_mantener
                    perfil.save()
                    print(f"      ✅ Perfil de {perfil.user.username} reasignado")

            cliente.delete()
            print(f"   🗑️  Cliente ID {cliente.id} eliminado")

        print(f"   ✅ Mantenido cliente ID {cliente_a_mantener.id}\n")

    print("✅ Limpieza de clientes duplicados completada\n")


def limpiar_correos_duplicados():
    """Limpia correos duplicados en clientes"""
    print("\n" + "="*70)
    print("🔧 LIMPIANDO CORREOS DUPLICADOS")
    print("="*70 + "\n")

    # Encontrar correos duplicados
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT correo, COUNT(*) as count 
            FROM clientes 
            GROUP BY correo 
            HAVING count > 1
        """)
        duplicados = cursor.fetchall()

    if not duplicados:
        print("✅ No se encontraron correos duplicados\n")
        return

    print(f"⚠️  Se encontraron {len(duplicados)} correos duplicados\n")

    for correo, count in duplicados:
        clientes = Cliente.objects.filter(correo=correo).order_by('fecha_registro')

        print(f"📧 Correo: {correo}")
        print(f"   Total registros: {count}")

        # Mantener el más reciente
        cliente_principal = clientes.last()
        clientes_a_eliminar = list(clientes[:-1])

        for cliente in clientes_a_eliminar:
            # Reasignar perfiles
            perfiles = PerfilUsuario.objects.filter(cliente=cliente)
            for perfil in perfiles:
                perfil.cliente = cliente_principal
                perfil.save()

            cliente.delete()
            print(f"   🗑️  Cliente ID {cliente.id} eliminado")

        print(f"   ✅ Mantenido cliente ID {cliente_principal.id}\n")

    print("✅ Limpieza de correos duplicados completada\n")


def verificar_perfiles_sin_cliente():
    """Verifica y repara perfiles sin cliente asociado"""
    print("\n" + "="*70)
    print("🔧 VERIFICANDO PERFILES SIN CLIENTE")
    print("="*70 + "\n")

    perfiles_sin_cliente = PerfilUsuario.objects.filter(
        tipo_usuario='CLIENTE',
        cliente__isnull=True
    )

    if not perfiles_sin_cliente.exists():
        print("✅ Todos los perfiles de cliente tienen un cliente asociado\n")
        return

    print(f"⚠️  Se encontraron {perfiles_sin_cliente.count()} perfiles sin cliente\n")

    for perfil in perfiles_sin_cliente:
        user = perfil.user

        print(f"👤 Usuario: {user.username} ({user.email})")

        # Buscar si existe un cliente con el mismo email
        cliente = Cliente.objects.filter(correo=user.email).first()

        if cliente:
            print(f"   ✅ Cliente encontrado: {cliente.nombre_completo}")
            perfil.cliente = cliente
            perfil.save()
        else:
            # Crear nuevo cliente
            print(f"   ⚠️  Creando nuevo cliente...")

            # Generar número de documento único
            documento = perfil.documento or f'USER-{user.id}'

            # Verificar que no exista
            counter = 1
            documento_original = documento
            while Cliente.objects.filter(numero_documento=documento).exists():
                documento = f'{documento_original}-{counter}'
                counter += 1

            cliente = Cliente.objects.create(
                nombres=user.first_name or 'Usuario',
                apellidos=user.last_name or user.username,
                numero_documento=documento,
                telefono=perfil.telefono or '0000000000',
                correo=user.email,
                direccion=perfil.direccion or 'Dirección pendiente',
                activo=True
            )

            perfil.cliente = cliente
            perfil.documento = documento
            perfil.save()

            print(f"   ✅ Cliente creado: {cliente.numero_documento}")

        print()

    print("✅ Verificación de perfiles completada\n")


def estadisticas():
    """Muestra estadísticas de la base de datos"""
    print("\n" + "="*70)
    print("📊 ESTADÍSTICAS DE LA BASE DE DATOS")
    print("="*70 + "\n")

    print(f"👥 Usuarios:        {User.objects.count()}")
    print(f"📋 Perfiles:        {PerfilUsuario.objects.count()}")
    print(f"👤 Clientes:        {Cliente.objects.count()}")

    perfiles_cliente = PerfilUsuario.objects.filter(tipo_usuario='CLIENTE').count()
    perfiles_tecnico = PerfilUsuario.objects.filter(tipo_usuario='TECNICO').count()
    perfiles_admin = PerfilUsuario.objects.filter(tipo_usuario='ADMIN').count()

    print(f"\n📊 Tipos de perfil:")
    print(f"   Clientes:        {perfiles_cliente}")
    print(f"   Técnicos:        {perfiles_tecnico}")
    print(f"   Administradores: {perfiles_admin}")

    perfiles_sin_cliente = PerfilUsuario.objects.filter(
        tipo_usuario='CLIENTE',
        cliente__isnull=True
    ).count()

    if perfiles_sin_cliente > 0:
        print(f"\n⚠️  Perfiles de cliente sin cliente asociado: {perfiles_sin_cliente}")

    print("\n" + "="*70 + "\n")


def main():
    """Función principal"""
    print("\n" + "="*70)
    print("🔧 SCRIPT DE REPARACIÓN DE BASE DE DATOS")
    print("="*70)

    print("\nEste script:")
    print("  1. Elimina clientes duplicados")
    print("  2. Limpia correos duplicados")
    print("  3. Repara perfiles sin cliente")
    print("  4. Muestra estadísticas")

    respuesta = input("\n¿Deseas continuar? (si/no): ")

    if respuesta.lower() != 'si':
        print("\n❌ Operación cancelada\n")
        return

    try:
        limpiar_clientes_duplicados()
        limpiar_correos_duplicados()
        verificar_perfiles_sin_cliente()
        estadisticas()

        print("="*70)
        print("✅ REPARACIÓN COMPLETADA EXITOSAMENTE")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n❌ Error durante la reparación: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

