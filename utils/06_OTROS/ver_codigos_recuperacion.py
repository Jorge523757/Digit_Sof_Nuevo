#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para ver códigos de recuperación activos
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from usuarios.models_tokens import TokenRecuperacion
from django.utils import timezone
from datetime import timedelta


def mostrar_codigos():
    """Muestra todos los códigos de recuperación activos"""

    print("\n" + "=" * 80)
    print("🔍 CÓDIGOS DE RECUPERACIÓN ACTIVOS")
    print("=" * 80)
    print()

    # Obtener tokens de las últimas 2 horas
    hace_2_horas = timezone.now() - timedelta(hours=2)
    tokens = TokenRecuperacion.objects.filter(
        fecha_creacion__gte=hace_2_horas
    ).order_by('-fecha_creacion')

    if not tokens.exists():
        print("❌ No hay códigos de recuperación recientes (últimas 2 horas)")
        print()
        print("💡 Solicita un nuevo código desde la página de recuperación")
        print("=" * 80)
        return

    print(f"📊 Encontrados {tokens.count()} códigos recientes:\n")

    for i, token in enumerate(tokens, 1):
        estado = "❌ EXPIRADO" if token.esta_expirado else "✅ VÁLIDO"
        if token.usado:
            estado = "🔒 USADO"

        tiempo_restante = ""
        if not token.usado and not token.esta_expirado:
            minutos = int((token.fecha_expiracion - timezone.now()).total_seconds() / 60)
            tiempo_restante = f" ({minutos} min restantes)"

        print(f"{i}. {'-' * 70}")
        print(f"   Email: {token.email}")
        print(f"   Usuario: {token.usuario.username}")
        print(f"   🔢 CÓDIGO: {token.codigo}")
        print(f"   Estado: {estado}{tiempo_restante}")
        print(f"   Creado: {token.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Expira: {token.fecha_expiracion.strftime('%Y-%m-%d %H:%M:%S')}")
        print()

    print("=" * 80)
    print()

    # Mostrar códigos válidos resaltados
    codigos_validos = [t for t in tokens if t.es_valido]
    if codigos_validos:
        print("✅ CÓDIGOS VÁLIDOS PARA USAR AHORA:")
        print("-" * 80)
        for token in codigos_validos:
            print(f"   {token.email} → CÓDIGO: {token.codigo}")
        print("-" * 80)
    else:
        print("⚠️  No hay códigos válidos activos.")
        print("   Solicita uno nuevo desde la página de recuperación.")

    print()
    print("=" * 80)
    print()


def limpiar_tokens_expirados():
    """Limpia tokens expirados antiguos"""
    hace_24_horas = timezone.now() - timedelta(hours=24)
    tokens_antiguos = TokenRecuperacion.objects.filter(
        fecha_creacion__lt=hace_24_horas
    )

    cantidad = tokens_antiguos.count()
    if cantidad > 0:
        tokens_antiguos.delete()
        print(f"🗑️  Eliminados {cantidad} tokens expirados (más de 24 horas)")
        print()


def menu():
    """Menú interactivo"""
    while True:
        print("\n" + "=" * 80)
        print("🔐 GESTOR DE CÓDIGOS DE RECUPERACIÓN")
        print("=" * 80)
        print()
        print("1. Ver códigos activos")
        print("2. Limpiar tokens expirados")
        print("3. Generar nuevo código para un email")
        print("4. Salir")
        print()

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == '1':
            mostrar_codigos()
        elif opcion == '2':
            limpiar_tokens_expirados()
            print("✅ Limpieza completada")
        elif opcion == '3':
            generar_codigo_manual()
        elif opcion == '4':
            print("\n👋 ¡Hasta luego!\n")
            break
        else:
            print("❌ Opción inválida")


def generar_codigo_manual():
    """Genera un código de recuperación manual"""
    from django.contrib.auth.models import User

    print("\n" + "=" * 80)
    print("📧 GENERAR NUEVO CÓDIGO")
    print("=" * 80)
    print()

    email = input("Email del usuario: ").strip()

    if not email:
        print("❌ Email vacío")
        return

    try:
        usuario = User.objects.get(email=email)

        # Crear token
        token = TokenRecuperacion.crear_token(usuario, email)

        print()
        print("✅ Código generado exitosamente")
        print("-" * 80)
        print(f"Email: {email}")
        print(f"Usuario: {usuario.username}")
        print(f"🔢 CÓDIGO: {token.codigo}")
        print(f"Válido por: 30 minutos")
        print(f"Expira: {token.fecha_expiracion.strftime('%H:%M:%S')}")
        print("-" * 80)
        print()
        print("💡 Usa este código en la página de recuperación")
        print()

    except User.DoesNotExist:
        print(f"❌ No existe usuario con email: {email}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == '__main__':
    try:
        import sys

        if len(sys.argv) > 1:
            if sys.argv[1] == '--ver':
                mostrar_codigos()
            elif sys.argv[1] == '--limpiar':
                limpiar_tokens_expirados()
            elif sys.argv[1] == '--generar':
                generar_codigo_manual()
            else:
                print("Uso: python ver_codigos_recuperacion.py [--ver|--limpiar|--generar]")
        else:
            # Modo simple: solo mostrar códigos
            mostrar_codigos()

            print("💡 OPCIONES:")
            print("   python ver_codigos_recuperacion.py --ver      → Ver códigos")
            print("   python ver_codigos_recuperacion.py --limpiar  → Limpiar expirados")
            print("   python ver_codigos_recuperacion.py --generar  → Generar nuevo código")
            print()

    except KeyboardInterrupt:
        print("\n\n👋 Cancelado\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)

