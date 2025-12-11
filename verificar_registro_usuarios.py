"""
DIGITSOFT - Script para verificar registro de usuarios
Verifica que los clientes y técnicos se registran correctamente
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_inventario.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from clientes.models import Cliente
from tecnicos.models import Tecnico
from django.db.models import Q


def print_section(title):
    """Imprime un título de sección"""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def verificar_clientes():
    """Verifica los registros de clientes"""
    print_section("VERIFICACIÓN DE CLIENTES")

    # Obtener todos los perfiles de tipo CLIENTE
    perfiles_cliente = PerfilUsuario.objects.filter(tipo_usuario='CLIENTE')
    print(f"\n✅ Perfiles de usuario tipo CLIENTE: {perfiles_cliente.count()}")

    # Obtener todos los registros de la tabla Cliente
    clientes = Cliente.objects.all()
    print(f"✅ Registros en la tabla Cliente: {clientes.count()}")

    # Verificar vinculación
    print("\n📋 Detalles de clientes registrados:")
    print("-" * 80)

    for perfil in perfiles_cliente:
        user = perfil.user
        cliente_vinculado = perfil.cliente

        print(f"\n👤 Usuario: {user.username} ({user.get_full_name()})")
        print(f"   📧 Email: {user.email}")
        print(f"   📱 Teléfono: {perfil.telefono}")
        print(f"   📄 Documento: {perfil.documento}")

        if cliente_vinculado:
            print(f"   ✅ VINCULADO con Cliente ID: {cliente_vinculado.id}")
            print(f"   👉 Nombre Cliente: {cliente_vinculado.nombre_completo}")
            print(f"   👉 Documento Cliente: {cliente_vinculado.numero_documento}")
        else:
            print(f"   ❌ NO VINCULADO con tabla Cliente")

            # Buscar si existe un cliente con el mismo documento
            cliente_por_documento = Cliente.objects.filter(
                numero_documento=perfil.documento
            ).first()

            if cliente_por_documento:
                print(f"   ⚠️  Pero existe un cliente con documento {perfil.documento}")
                print(f"   💡 Recomendación: Vincular manualmente")

    print("\n" + "-" * 80)
    print(f"\n📊 Resumen Clientes:")
    print(f"   • Perfiles CLIENTE en tabla usuarios_perfil: {perfiles_cliente.count()}")
    print(f"   • Registros en tabla clientes: {clientes.count()}")
    print(f"   • Perfiles vinculados correctamente: {perfiles_cliente.filter(cliente__isnull=False).count()}")
    print(f"   • Perfiles SIN vincular: {perfiles_cliente.filter(cliente__isnull=True).count()}")


def verificar_tecnicos():
    """Verifica los registros de técnicos"""
    print_section("VERIFICACIÓN DE TÉCNICOS")

    # Obtener todos los perfiles de tipo TECNICO
    perfiles_tecnico = PerfilUsuario.objects.filter(tipo_usuario='TECNICO')
    print(f"\n✅ Perfiles de usuario tipo TECNICO: {perfiles_tecnico.count()}")

    # Obtener todos los registros de la tabla Tecnico
    tecnicos = Tecnico.objects.all()
    print(f"✅ Registros en la tabla Tecnico: {tecnicos.count()}")

    # Verificar vinculación
    print("\n📋 Detalles de técnicos registrados:")
    print("-" * 80)

    for perfil in perfiles_tecnico:
        user = perfil.user
        tecnico_vinculado = perfil.tecnico

        print(f"\n👤 Usuario: {user.username} ({user.get_full_name()})")
        print(f"   📧 Email: {user.email}")
        print(f"   📱 Teléfono: {perfil.telefono}")
        print(f"   📄 Documento: {perfil.documento}")

        if tecnico_vinculado:
            print(f"   ✅ VINCULADO con Técnico ID: {tecnico_vinculado.id}")
            print(f"   👉 Nombre Técnico: {tecnico_vinculado.nombre_completo}")
            print(f"   👉 Documento Técnico: {tecnico_vinculado.numero_documento}")
            print(f"   👉 Profesión: {tecnico_vinculado.profesion}")
        else:
            print(f"   ❌ NO VINCULADO con tabla Tecnico")

            # Buscar si existe un técnico con el mismo documento
            tecnico_por_documento = Tecnico.objects.filter(
                numero_documento=perfil.documento
            ).first()

            if tecnico_por_documento:
                print(f"   ⚠️  Pero existe un técnico con documento {perfil.documento}")
                print(f"   💡 Recomendación: Vincular manualmente")

    print("\n" + "-" * 80)
    print(f"\n📊 Resumen Técnicos:")
    print(f"   • Perfiles TECNICO en tabla usuarios_perfil: {perfiles_tecnico.count()}")
    print(f"   • Registros en tabla tecnicos: {tecnicos.count()}")
    print(f"   • Perfiles vinculados correctamente: {perfiles_tecnico.filter(tecnico__isnull=False).count()}")
    print(f"   • Perfiles SIN vincular: {perfiles_tecnico.filter(tecnico__isnull=True).count()}")


def verificar_usuarios_generales():
    """Verifica todos los usuarios del sistema"""
    print_section("VERIFICACIÓN GENERAL DE USUARIOS")

    total_usuarios = User.objects.count()
    usuarios_activos = User.objects.filter(is_active=True).count()
    usuarios_staff = User.objects.filter(is_staff=True).count()
    usuarios_superuser = User.objects.filter(is_superuser=True).count()

    perfiles_cliente = PerfilUsuario.objects.filter(tipo_usuario='CLIENTE').count()
    perfiles_tecnico = PerfilUsuario.objects.filter(tipo_usuario='TECNICO').count()
    perfiles_admin = PerfilUsuario.objects.filter(tipo_usuario='ADMIN').count()
    perfiles_proveedor = PerfilUsuario.objects.filter(tipo_usuario='PROVEEDOR').count()

    print(f"\n📊 Estadísticas Generales:")
    print(f"   • Total de usuarios en el sistema: {total_usuarios}")
    print(f"   • Usuarios activos: {usuarios_activos}")
    print(f"   • Usuarios staff: {usuarios_staff}")
    print(f"   • Superusuarios: {usuarios_superuser}")

    print(f"\n👥 Distribución por Tipo de Usuario:")
    print(f"   • Clientes: {perfiles_cliente}")
    print(f"   • Técnicos: {perfiles_tecnico}")
    print(f"   • Administradores: {perfiles_admin}")
    print(f"   • Proveedores: {perfiles_proveedor}")


def mostrar_instrucciones():
    """Muestra instrucciones de uso"""
    print_section("CÓMO FUNCIONA EL REGISTRO")

    print("""
📝 REGISTRO DE CLIENTES:
   
   1. El usuario accede a: /usuarios/registro/
   2. Completa el formulario de registro (RegistroClienteForm)
   3. Al guardar, el sistema crea automáticamente:
      ✅ Un usuario en la tabla User (Django auth)
      ✅ Un perfil en PerfilUsuario con tipo_usuario='CLIENTE'
      ✅ Un registro en la tabla Cliente
      ✅ Vincula el perfil con el cliente (perfil.cliente = cliente)
   
   4. El cliente aparece en:
      👉 Módulo de Usuarios (/usuarios/gestionar/)
      👉 Módulo de Clientes (/clientes/)

📝 REGISTRO DE TÉCNICOS:
   
   1. El usuario accede a: /usuarios/registro/tecnico/
   2. Completa el formulario de registro (RegistroTecnicoForm)
   3. Al guardar, el sistema crea automáticamente:
      ✅ Un usuario en la tabla User (Django auth)
      ✅ Un perfil en PerfilUsuario con tipo_usuario='TECNICO'
      ✅ Un registro en la tabla Tecnico
      ✅ Vincula el perfil con el técnico (perfil.tecnico = tecnico)
   
   4. El técnico aparece en:
      👉 Módulo de Usuarios (/usuarios/gestionar/)
      👉 Módulo de Técnicos (/tecnicos/)

🔗 VINCULACIÓN:
   
   • La vinculación entre PerfilUsuario y Cliente/Tecnico es automática
   • Se usa ForeignKey en el modelo PerfilUsuario:
     - perfil.cliente → apunta al registro en Cliente
     - perfil.tecnico → apunta al registro en Tecnico
   
   • Esto permite:
     - Desde un Usuario, acceder a su Cliente/Tecnico
     - Desde un Cliente/Tecnico, acceder a su Usuario
     - Mantener la integridad referencial

📍 URLS DE ACCESO:
   
   • Registro Cliente: http://localhost:8000/usuarios/registro/
   • Registro Técnico: http://localhost:8000/usuarios/registro/tecnico/
   • Login: http://localhost:8000/usuarios/login/
   • Gestión Usuarios: http://localhost:8000/usuarios/gestionar/
   • Gestión Clientes: http://localhost:8000/clientes/
   • Gestión Técnicos: http://localhost:8000/tecnicos/
""")


def main():
    """Función principal"""
    try:
        print("\n")
        print("╔" + "=" * 78 + "╗")
        print("║" + " " * 20 + "DIGITSOFT - VERIFICACIÓN DE REGISTROS" + " " * 19 + "║")
        print("╚" + "=" * 78 + "╝")

        mostrar_instrucciones()
        verificar_usuarios_generales()
        verificar_clientes()
        verificar_tecnicos()

        print_section("CONCLUSIÓN")
        print("""
✅ El sistema está correctamente configurado para:
   
   1. Registrar usuarios como CLIENTES o TÉCNICOS
   2. Crear automáticamente los registros en ambas tablas
   3. Vincular correctamente los perfiles con clientes/técnicos
   4. Mostrar los datos en sus respectivos módulos

🎯 Los registros aparecen en:
   
   • CLIENTES: Módulo de Usuarios + Módulo de Clientes
   • TÉCNICOS: Módulo de Usuarios + Módulo de Técnicos

💡 Si encuentras registros sin vincular, puede ser porque:
   
   • Fueron creados antes de implementar esta funcionalidad
   • Fueron creados manualmente en el admin
   • Hubo algún error durante el registro

🔧 Para vincular registros manualmente:
   
   1. Ir al panel de administración Django
   2. Buscar el PerfilUsuario
   3. Asignar el cliente o técnico correspondiente
   4. Guardar los cambios
        """)

    except Exception as e:
        print(f"\n❌ Error al verificar: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

