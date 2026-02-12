"""
Script para crear datos iniciales del módulo de ayuda
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from ayuda.models import CategoriaAyuda, FAQ

print("=" * 80)
print("📚 CREANDO DATOS INICIALES DEL MÓDULO DE AYUDA")
print("=" * 80)
print()

# Crear categorías
categorias_data = [
    {'nombre': 'Cuenta y Acceso', 'icono': 'fa-user', 'orden': 1, 'descripcion': 'Problemas con inicio de sesión, registro y recuperación de contraseña'},
    {'nombre': 'Productos', 'icono': 'fa-shopping-bag', 'orden': 2, 'descripcion': 'Consultas sobre productos, stock y precios'},
    {'nombre': 'Pedidos', 'icono': 'fa-shopping-cart', 'orden': 3, 'descripcion': 'Estado de pedidos, envíos y devoluciones'},
    {'nombre': 'Pagos', 'icono': 'fa-credit-card', 'orden': 4, 'descripcion': 'Métodos de pago, facturación y recibos'},
    {'nombre': 'Técnico', 'icono': 'fa-cog', 'orden': 5, 'descripcion': 'Errores del sistema, bugs y problemas técnicos'},
    {'nombre': 'Otros', 'icono': 'fa-question-circle', 'orden': 6, 'descripcion': 'Consultas generales y sugerencias'},
]

print("📂 Creando categorías...")
categorias_creadas = 0

for cat_data in categorias_data:
    categoria, created = CategoriaAyuda.objects.get_or_create(
        nombre=cat_data['nombre'],
        defaults=cat_data
    )
    if created:
        print(f"   ✅ {categoria.nombre}")
        categorias_creadas += 1
    else:
        print(f"   ⚠️  {categoria.nombre} (ya existe)")

print(f"\n✅ {categorias_creadas} categorías creadas")
print()

# Crear FAQs
faqs_data = [
    {
        'categoria': 'Cuenta y Acceso',
        'pregunta': '¿Cómo recupero mi contraseña?',
        'respuesta': '''Para recuperar tu contraseña:

1. Ve a la página de inicio de sesión
2. Haz clic en "¿Olvidaste tu contraseña?"
3. Ingresa tu email registrado
4. Recibirás un código de 6 dígitos por email
5. Ingresa el código en la página de verificación
6. Crea tu nueva contraseña

El código expira en 30 minutos. Si no lo recibes, revisa tu carpeta de SPAM.''',
        'orden': 1
    },
    {
        'categoria': 'Cuenta y Acceso',
        'pregunta': '¿Cómo creo una cuenta?',
        'respuesta': '''Para crear una cuenta en DIGIT SOFT:

1. Haz clic en "Registrarse" en la página de inicio
2. Completa el formulario con:
   - Nombre de usuario
   - Email
   - Contraseña segura
3. Acepta los términos y condiciones
4. Haz clic en "Registrar"

También puedes registrarte con tu cuenta de Google haciendo clic en "Continuar con Google".''',
        'orden': 2
    },
    {
        'categoria': 'Productos',
        'pregunta': '¿Cómo busco un producto?',
        'respuesta': '''Puedes buscar productos de varias formas:

1. **Barra de búsqueda**: Escribe el nombre del producto en la parte superior
2. **Categorías**: Navega por las categorías en el menú
3. **Filtros**: Usa los filtros de precio, marca, etc.

La búsqueda es inteligente y muestra resultados mientras escribes.''',
        'orden': 3
    },
    {
        'categoria': 'Pedidos',
        'pregunta': '¿Cómo hago un pedido?',
        'respuesta': '''Para realizar un pedido:

1. Busca el producto que deseas
2. Haz clic en "Agregar al carrito"
3. Ve al carrito haciendo clic en el ícono del carrito
4. Revisa tu pedido y cantidades
5. Haz clic en "Proceder al pago"
6. Completa la información de envío
7. Selecciona el método de pago
8. Confirma tu pedido

Recibirás un email de confirmación con el número de pedido.''',
        'orden': 4
    },
    {
        'categoria': 'Pedidos',
        'pregunta': '¿Cómo rastreo mi pedido?',
        'respuesta': '''Para rastrear tu pedido:

1. Inicia sesión en tu cuenta
2. Ve a "Mis Pedidos" en el menú de usuario
3. Busca tu pedido en la lista
4. Haz clic en "Ver detalles"
5. Verás el estado actual del pedido

También recibirás notificaciones por email cuando el estado cambie.''',
        'orden': 5
    },
    {
        'categoria': 'Pagos',
        'pregunta': '¿Qué métodos de pago aceptan?',
        'respuesta': '''Aceptamos los siguientes métodos de pago:

- **Tarjetas de crédito/débito**: Visa, Mastercard, American Express
- **Transferencia bancaria**
- **Pago contra entrega** (en algunas zonas)
- **PayPal** (próximamente)

Todos los pagos son procesados de forma segura con encriptación SSL.''',
        'orden': 6
    },
    {
        'categoria': 'Técnico',
        'pregunta': '¿Qué navegadores son compatibles?',
        'respuesta': '''DIGIT SOFT es compatible con:

- **Google Chrome** (recomendado) - versión 90+
- **Mozilla Firefox** - versión 88+
- **Microsoft Edge** - versión 90+
- **Safari** - versión 14+

Para la mejor experiencia, recomendamos mantener tu navegador actualizado.''',
        'orden': 7
    },
    {
        'categoria': 'Técnico',
        'pregunta': 'Encuentro un error en la página',
        'respuesta': '''Si encuentras un error:

1. Intenta recargar la página (F5)
2. Limpia la caché del navegador
3. Prueba en modo incógnito
4. Si persiste, crea un ticket de soporte con:
   - Descripción del error
   - Captura de pantalla
   - Navegador y versión que usas
   - Pasos para reproducir el error

Nuestro equipo lo revisará lo antes posible.''',
        'orden': 8
    },
    {
        'categoria': 'Otros',
        'pregunta': '¿Cómo contacto con soporte?',
        'respuesta': '''Puedes contactarnos de varias formas:

1. **Tickets de ayuda**: Crea un ticket desde el centro de ayuda (respuesta en 24-48h)
2. **Email**: davidcristancho160@gmail.com
3. **Centro de ayuda**: Revisa las preguntas frecuentes

Para consultas urgentes, marca el ticket como "Urgente".''',
        'orden': 9
    },
    {
        'categoria': 'Otros',
        'pregunta': '¿Puedo dar sugerencias?',
        'respuesta': '''¡Por supuesto! Valoramos tus sugerencias:

1. Crea un ticket en la categoría "Otros"
2. Marca el asunto como "Sugerencia: [tu idea]"
3. Describe detalladamente tu propuesta

Revisamos todas las sugerencias y las consideramos para futuras actualizaciones.''',
        'orden': 10
    },
]

print("📝 Creando FAQs...")
faqs_creadas = 0

for faq_data in faqs_data:
    # Buscar categoría
    categoria = CategoriaAyuda.objects.filter(nombre=faq_data['categoria']).first()

    if categoria:
        faq, created = FAQ.objects.get_or_create(
            pregunta=faq_data['pregunta'],
            defaults={
                'categoria': categoria,
                'respuesta': faq_data['respuesta'],
                'orden': faq_data['orden'],
                'activo': True
            }
        )
        if created:
            print(f"   ✅ {faq.pregunta}")
            faqs_creadas += 1
        else:
            print(f"   ⚠️  {faq.pregunta} (ya existe)")

print(f"\n✅ {faqs_creadas} FAQs creadas")
print()

print("=" * 80)
print("✅ DATOS INICIALES CREADOS EXITOSAMENTE")
print("=" * 80)
print()
print(f"📊 Resumen:")
print(f"   - Categorías: {CategoriaAyuda.objects.count()}")
print(f"   - FAQs: {FAQ.objects.count()}")
print()
print("🎉 El módulo de ayuda está listo para usar")
print()

