"""
Script para corregir usuarios existentes sin vinculación a Cliente/Técnico/Proveedor

Este script busca perfiles de usuarios que tienen tipo_usuario definido pero no tienen
el registro correspondiente en las tablas de Cliente, Técnico o Proveedor, y los crea.

Ejecutar con:
python manage.py shell < corregir_usuarios_existentes.py

o

python manage.py runscript corregir_usuarios_existentes
"""

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from clientes.models import Cliente
from tecnicos.models import Tecnico
from proveedores.models import Proveedor


def corregir_usuarios_existentes():
    """Corrige usuarios existentes creando los registros faltantes"""

    print("=" * 80)
    print("CORRECCIÓN DE USUARIOS EXISTENTES")
    print("=" * 80)
    print()

    # Contadores
    clientes_creados = 0
    tecnicos_creados = 0
    proveedores_creados = 0
    administradores_actualizados = 0
    errores = 0

    # Obtener todos los perfiles
    perfiles = PerfilUsuario.objects.select_related('user').all()

    print(f"Total de perfiles a revisar: {perfiles.count()}")
    print()

    for perfil in perfiles:
        user = perfil.user
        tipo = perfil.tipo_usuario

        try:
            # CLIENTES sin registro en tabla clientes
            if tipo == 'CLIENTE' and not perfil.cliente:
                print(f"📋 Creando Cliente para: {user.username} ({user.first_name} {user.last_name})")

                # Verificar si ya existe un cliente con ese correo
                cliente_existente = Cliente.objects.filter(correo=user.email).first()

                if cliente_existente:
                    print(f"   ⚠️  Ya existe un cliente con ese correo, vinculando...")
                    perfil.cliente = cliente_existente
                    perfil.save()
                else:
                    # Crear nuevo cliente
                    cliente = Cliente.objects.create(
                        nombres=user.first_name or 'Sin nombre',
                        apellidos=user.last_name or 'Sin apellido',
                        numero_documento=perfil.documento or '',
                        telefono=perfil.telefono or '',
                        correo=user.email,
                        direccion=perfil.direccion or '',
                        activo=user.is_active
                    )

                    # Vincular
                    perfil.cliente = cliente
                    perfil.save()

                    clientes_creados += 1
                    print(f"   ✅ Cliente creado y vinculado: ID {cliente.id}")

            # TÉCNICOS sin registro en tabla tecnicos
            elif tipo == 'TECNICO' and not perfil.tecnico:
                print(f"🔧 Creando Técnico para: {user.username} ({user.first_name} {user.last_name})")

                # Verificar si ya existe un técnico con ese correo
                tecnico_existente = Tecnico.objects.filter(correo=user.email).first()

                if tecnico_existente:
                    print(f"   ⚠️  Ya existe un técnico con ese correo, vinculando...")
                    perfil.tecnico = tecnico_existente
                    perfil.save()
                else:
                    # Crear nuevo técnico
                    tecnico = Tecnico.objects.create(
                        nombres=user.first_name or 'Sin nombre',
                        apellidos=user.last_name or 'Sin apellido',
                        numero_documento=perfil.documento or '',
                        telefono=perfil.telefono or '',
                        correo=user.email,
                        profesion='Técnico General',  # Valor por defecto
                        activo=user.is_active
                    )

                    # Vincular
                    perfil.tecnico = tecnico
                    perfil.save()

                    tecnicos_creados += 1
                    print(f"   ✅ Técnico creado y vinculado: ID {tecnico.id}")

            # PROVEEDORES sin registro en tabla proveedores
            elif tipo == 'PROVEEDOR':
                print(f"🏢 Creando Proveedor para: {user.username} ({user.first_name} {user.last_name})")

                # Verificar si ya existe un proveedor con ese correo
                proveedor_existente = Proveedor.objects.filter(correo=user.email).first()

                if proveedor_existente:
                    print(f"   ⚠️  Ya existe un proveedor con ese correo")
                    print(f"   ℹ️  Proveedor existente: {proveedor_existente.nombre_empresa}")
                else:
                    # Crear nuevo proveedor
                    nombre_empresa = f"{user.first_name} {user.last_name}".strip() or user.username

                    proveedor = Proveedor.objects.create(
                        nombre_empresa=nombre_empresa,
                        nombre_contacto=f"{user.first_name} {user.last_name}".strip() or user.username,
                        telefono=perfil.telefono or '',
                        correo=user.email,
                        direccion=perfil.direccion or '',
                        activo=user.is_active
                    )

                    proveedores_creados += 1
                    print(f"   ✅ Proveedor creado: ID {proveedor.id}")

            # ADMINISTRADORES: asegurar permisos
            elif tipo == 'ADMIN':
                if not user.is_staff or not user.is_superuser:
                    print(f"👑 Actualizando permisos de Administrador: {user.username}")
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    administradores_actualizados += 1
                    print(f"   ✅ Permisos de administrador actualizados")

        except Exception as e:
            errores += 1
            print(f"   ❌ Error al procesar {user.username}: {str(e)}")
            print()

    # Resumen
    print()
    print("=" * 80)
    print("RESUMEN DE CORRECCIONES")
    print("=" * 80)
    print(f"✅ Clientes creados: {clientes_creados}")
    print(f"✅ Técnicos creados: {tecnicos_creados}")
    print(f"✅ Proveedores creados: {proveedores_creados}")
    print(f"✅ Administradores actualizados: {administradores_actualizados}")
    print(f"❌ Errores: {errores}")
    print()
    print(f"Total de correcciones: {clientes_creados + tecnicos_creados + proveedores_creados + administradores_actualizados}")
    print("=" * 80)


def verificar_usuarios():
    """Verifica el estado actual de los usuarios"""

    print("\n" + "=" * 80)
    print("VERIFICACIÓN DE USUARIOS")
    print("=" * 80 + "\n")

    # Contar por tipo
    total_usuarios = User.objects.count()
    total_perfiles = PerfilUsuario.objects.count()

    clientes = PerfilUsuario.objects.filter(tipo_usuario='CLIENTE')
    tecnicos = PerfilUsuario.objects.filter(tipo_usuario='TECNICO')
    proveedores = PerfilUsuario.objects.filter(tipo_usuario='PROVEEDOR')
    admins = PerfilUsuario.objects.filter(tipo_usuario='ADMIN')

    print(f"Total de usuarios: {total_usuarios}")
    print(f"Total de perfiles: {total_perfiles}")
    print()

    # Clientes
    clientes_con_registro = clientes.filter(cliente__isnull=False).count()
    clientes_sin_registro = clientes.filter(cliente__isnull=True).count()
    print(f"📋 CLIENTES:")
    print(f"   Total: {clientes.count()}")
    print(f"   Con registro en tabla clientes: {clientes_con_registro} ✅")
    print(f"   Sin registro en tabla clientes: {clientes_sin_registro} {'❌' if clientes_sin_registro > 0 else '✅'}")
    print()

    # Técnicos
    tecnicos_con_registro = tecnicos.filter(tecnico__isnull=False).count()
    tecnicos_sin_registro = tecnicos.filter(tecnico__isnull=True).count()
    print(f"🔧 TÉCNICOS:")
    print(f"   Total: {tecnicos.count()}")
    print(f"   Con registro en tabla tecnicos: {tecnicos_con_registro} ✅")
    print(f"   Sin registro en tabla tecnicos: {tecnicos_sin_registro} {'❌' if tecnicos_sin_registro > 0 else '✅'}")
    print()

    # Proveedores
    print(f"🏢 PROVEEDORES:")
    print(f"   Total de perfiles: {proveedores.count()}")
    print(f"   Total en tabla proveedores: {Proveedor.objects.count()}")
    print()

    # Administradores
    admins_con_permisos = User.objects.filter(
        perfil__tipo_usuario='ADMIN',
        is_staff=True,
        is_superuser=True
    ).count()
    admins_sin_permisos = admins.count() - admins_con_permisos
    print(f"👑 ADMINISTRADORES:")
    print(f"   Total: {admins.count()}")
    print(f"   Con permisos correctos: {admins_con_permisos} ✅")
    print(f"   Sin permisos correctos: {admins_sin_permisos} {'❌' if admins_sin_permisos > 0 else '✅'}")
    print()

    # Usuarios sin vincular
    usuarios_problema = []

    if clientes_sin_registro > 0:
        usuarios_problema.append(f"{clientes_sin_registro} clientes sin registro")
    if tecnicos_sin_registro > 0:
        usuarios_problema.append(f"{tecnicos_sin_registro} técnicos sin registro")
    if admins_sin_permisos > 0:
        usuarios_problema.append(f"{admins_sin_permisos} admins sin permisos")

    if usuarios_problema:
        print("⚠️  USUARIOS CON PROBLEMAS:")
        for problema in usuarios_problema:
            print(f"   • {problema}")
        print()
        print("💡 Ejecuta corregir_usuarios_existentes() para arreglarlos")
    else:
        print("✅ ¡Todos los usuarios están correctamente configurados!")

    print("=" * 80 + "\n")


if __name__ == '__main__':
    print("\n🔍 Verificando estado actual...")
    verificar_usuarios()

    respuesta = input("\n¿Deseas corregir los usuarios con problemas? (s/n): ")

    if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        print("\n🔧 Iniciando correcciones...\n")
        corregir_usuarios_existentes()

        print("\n🔍 Verificando resultado...\n")
        verificar_usuarios()
    else:
        print("\n❌ Corrección cancelada")
        print("\nPuedes ejecutar la corrección en cualquier momento con:")
        print("python manage.py shell < corregir_usuarios_existentes.py")

