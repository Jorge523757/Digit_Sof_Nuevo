"""
Script para crear el técnico Oscar Alvarez manualmente
"""

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from tecnicos.models import Tecnico

print("=" * 80)
print("CREACIÓN MANUAL DE TÉCNICO PARA OSCAR ALVAREZ")
print("=" * 80)

try:
    # Buscar el usuario
    usuario = User.objects.get(first_name="Oscar", last_name="Alvarez")
    print(f"\n✅ Usuario encontrado: {usuario.username}")
    print(f"   Email: {usuario.email}")

    perfil = usuario.perfil
    print(f"\n📋 Perfil: {perfil.get_tipo_usuario_display()}")

    if perfil.tipo_usuario == 'TECNICO':
        if not perfil.tecnico:
            print("\n🔧 Creando técnico...")

            # Crear el técnico
            tecnico = Tecnico.objects.create(
                nombres=usuario.first_name,
                apellidos=usuario.last_name,
                numero_documento=perfil.documento or '',
                telefono=perfil.telefono or '',
                correo=usuario.email,
                profesion='Técnico en Reparación de PC',  # Valor por defecto
                activo=True
            )

            print(f"✅ Técnico creado con ID: {tecnico.id}")
            print(f"   Nombre: {tecnico.nombres} {tecnico.apellidos}")
            print(f"   Correo: {tecnico.correo}")
            print(f"   Profesión: {tecnico.profesion}")

            # Vincular con el perfil
            perfil.tecnico = tecnico
            perfil.save()

            print(f"\n✅ Técnico vinculado al perfil exitosamente")
            print(f"   perfil.tecnico.id = {perfil.tecnico.id}")

            print("\n" + "=" * 80)
            print("✅ OSCAR ALVAREZ AHORA DEBERÍA APARECER EN /tecnicos/")
            print("=" * 80)
        else:
            print("\n⚠️  El perfil ya tiene un técnico vinculado:")
            print(f"   ID: {perfil.tecnico.id}")
            print(f"   Nombre: {perfil.tecnico.nombres} {perfil.tecnico.apellidos}")
    else:
        print(f"\n❌ El usuario NO es de tipo TECNICO (actual: {perfil.tipo_usuario})")
        print("   Primero cambia el tipo de usuario a TECNICO desde el panel")

except User.DoesNotExist:
    print("\n❌ Usuario Oscar Alvarez NO encontrado")
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()

print()

