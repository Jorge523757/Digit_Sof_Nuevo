"""
Script para verificar si el técnico Oscar Alvarez fue creado correctamente
"""

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from tecnicos.models import Tecnico

print("=" * 80)
print("VERIFICACIÓN DE OSCAR ALVAREZ")
print("=" * 80)

# Buscar el usuario
try:
    usuario = User.objects.get(first_name="Oscar", last_name="Alvarez")
    print(f"\n✅ Usuario encontrado: {usuario.username}")
    print(f"   ID: {usuario.id}")
    print(f"   Email: {usuario.email}")

    # Ver su perfil
    perfil = usuario.perfil
    print(f"\n📋 Perfil:")
    print(f"   Tipo: {perfil.tipo_usuario} ({perfil.get_tipo_usuario_display()})")
    print(f"   Documento: {perfil.documento}")
    print(f"   Teléfono: {perfil.telefono}")

    # Ver si tiene técnico vinculado
    print(f"\n🔧 Técnico vinculado en perfil:")
    if perfil.tecnico:
        print(f"   ✅ SÍ - ID: {perfil.tecnico.id}")
        print(f"   Nombre: {perfil.tecnico.nombres} {perfil.tecnico.apellidos}")
        print(f"   Profesión: {perfil.tecnico.profesion}")
        print(f"   Correo: {perfil.tecnico.correo}")
    else:
        print(f"   ❌ NO tiene técnico vinculado (perfil.tecnico = NULL)")

    # Buscar en la tabla de técnicos
    print(f"\n🔍 Búsqueda en tabla de técnicos:")
    tecnicos = Tecnico.objects.filter(correo=usuario.email)
    if tecnicos.exists():
        print(f"   ✅ Encontrado {tecnicos.count()} técnico(s) con ese correo:")
        for tec in tecnicos:
            print(f"   - ID: {tec.id}")
            print(f"     Nombre: {tec.nombres} {tec.apellidos}")
            print(f"     Profesión: {tec.profesion}")
            print(f"     Activo: {tec.activo}")
    else:
        print(f"   ❌ NO hay técnicos con el correo: {usuario.email}")

    # Buscar por nombres
    tecnicos_por_nombre = Tecnico.objects.filter(nombres__icontains="Oscar", apellidos__icontains="Alvarez")
    if tecnicos_por_nombre.exists():
        print(f"\n   📌 Técnicos encontrados por nombre:")
        for tec in tecnicos_por_nombre:
            print(f"   - ID: {tec.id}")
            print(f"     Correo: {tec.correo}")
            print(f"     Profesión: {tec.profesion}")

    print("\n" + "=" * 80)
    print("DIAGNÓSTICO:")
    print("=" * 80)

    if perfil.tipo_usuario == 'TECNICO':
        print("✅ El perfil tiene tipo_usuario = 'TECNICO'")
    else:
        print(f"❌ El perfil NO tiene tipo TECNICO (actual: {perfil.tipo_usuario})")

    if perfil.tecnico:
        print("✅ El perfil tiene técnico vinculado")
    else:
        print("❌ El perfil NO tiene técnico vinculado")

        # Verificar si existe técnico sin vincular
        tecnicos_sin_vincular = Tecnico.objects.filter(correo=usuario.email)
        if tecnicos_sin_vincular.exists():
            print("\n⚠️  PROBLEMA: Existe técnico en la tabla pero NO está vinculado al perfil")
            print("   Solución: Ejecutar script de corrección")
        else:
            print("\n⚠️  PROBLEMA: No existe técnico en la tabla")
            print("   Solución: La vista de edición no creó el técnico correctamente")

except User.DoesNotExist:
    print("\n❌ Usuario Oscar Alvarez NO encontrado en la base de datos")
    print("   Por favor verifica el nombre exacto del usuario")

print("\n" + "=" * 80)

