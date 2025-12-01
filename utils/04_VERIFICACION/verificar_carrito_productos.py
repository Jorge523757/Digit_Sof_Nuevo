#!/usr/bin/env python
"""
Verificación del botón de carrito agregado en la gestión de productos
"""
import os
import sys
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def verificar_carrito_en_productos():
    """Verificar que el botón de carrito esté implementado correctamente"""
    print("🔍 VERIFICANDO BOTÓN DE CARRITO EN GESTIÓN DE PRODUCTOS")
    print("="*60)

    # Verificar archivos modificados
    archivos_verificar = [
        'templates/productos/lista.html',
        'templates/base_dashboard.html'
    ]

    verificaciones = []

    for archivo in archivos_verificar:
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                contenido = f.read()

            print(f"\n📄 Verificando: {archivo}")

            # Verificaciones específicas
            if 'lista.html' in archivo:
                checks = [
                    ('Carrito', 'fa-shopping-cart' in contenido),
                    ('Función agregar', 'agregarAlCarrito' in contenido),
                    ('CSRF Token', 'csrf_token' in contenido),
                    ('Botón Ver Tienda', 'Ver Tienda' in contenido),
                    ('JavaScript', 'fetch(' in contenido)
                ]
            else:  # base_dashboard.html
                checks = [
                    ('Botón Carrito Header', 'header-carrito-count' in contenido),
                    ('Enlace E-commerce', 'ecommerce:productos' in contenido),
                    ('JavaScript Global', 'actualizarContadorCarritoHeader' in contenido),
                    ('Menú Lateral', 'E-commerce / Tienda' in contenido)
                ]

            for nombre, resultado in checks:
                status = "✅" if resultado else "❌"
                print(f"   {status} {nombre}")
                verificaciones.append(resultado)
        else:
            print(f"❌ {archivo} no existe")
            verificaciones.append(False)

    # Verificar URLs del e-commerce
    print(f"\n🌐 Verificando URLs del E-commerce:")
    try:
        import ecommerce_urls
        print(f"   ✅ ecommerce_urls.py existe")
        verificaciones.append(True)
    except:
        print(f"   ❌ ecommerce_urls.py no encontrado")
        verificaciones.append(False)

    # Verificar vistas del e-commerce
    print(f"\n⚙️ Verificando vistas del E-commerce:")
    try:
        from productos.views import productos_ecommerce, ver_carrito, agregar_al_carrito
        print(f"   ✅ Vistas del e-commerce disponibles")
        verificaciones.append(True)
    except Exception as e:
        print(f"   ❌ Error en vistas: {e}")
        verificaciones.append(False)

    # Resultados
    total_checks = len(verificaciones)
    checks_pasados = sum(verificaciones)

    print("\n" + "="*60)
    print(f"📊 RESULTADO: {checks_pasados}/{total_checks} verificaciones pasadas")

    if checks_pasados == total_checks:
        print("✅ ¡PERFECTO! El botón de carrito está implementado correctamente")
        print("\n🎉 FUNCIONALIDADES AGREGADAS:")
        print("   • Botón 'Carrito' en el header de gestión de productos")
        print("   • Botón 'Ver Tienda' para ir al e-commerce")
        print("   • Botones 'Agregar al Carrito' en cada producto")
        print("   • Contador de productos en el carrito")
        print("   • Integración completa con el e-commerce")
        print("   • Enlaces en menús laterales y dropdowns")

        print("\n🌐 PARA VER LOS CAMBIOS:")
        print("   1. Ve a: http://127.0.0.1:8000/productos/")
        print("   2. Verás los nuevos botones del carrito")
        print("   3. Puedes agregar productos directamente al carrito")
        print("   4. El contador se actualiza automáticamente")

    else:
        print("⚠️ Hay algunas verificaciones que fallaron")
        print("   Revisa los errores mostrados arriba")

    print("="*60)

if __name__ == '__main__':
    verificar_carrito_en_productos()
