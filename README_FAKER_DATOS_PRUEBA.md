# 📊 Generador de Datos de Prueba con Faker - DIGIT SOFT

## 🎯 Descripción

Este módulo implementa **Faker** para generar datos de prueba realistas en la base de datos del sistema DIGIT SOFT, sin afectar ningún dato existente.

## ✨ Características

### ✅ Seguro y No Destructivo
- No elimina ni modifica datos existentes
- Solicita confirmación antes de generar datos
- Manejo de errores robusto

### 📦 Datos Generados

El script genera automáticamente:

| Tipo de Dato | Cantidad | Descripción |
|-------------|----------|-------------|
| **Clientes** | 20 | Clientes con nombres, documentos, teléfonos y direcciones realistas en español |
| **Categorías** | 5 | Categorías de productos (Laptops, Smartphones, Tablets, Accesorios, Componentes) |
| **Productos** | 30 | Productos con especificaciones técnicas, precios y stock |
| **Ventas** | 15 | Ventas completas con detalles, pagos y estados |

### 🎲 Datos Realistas

- **Nombres y Direcciones**: Generados con Faker en español (es_ES)
- **Documentos**: Números de documento únicos de 10 dígitos
- **Precios**: Rangos realistas con márgenes de ganancia
- **Stock**: Cantidades variables de inventario
- **Estados**: Distribución realista de estados de ventas
- **Métodos de Pago**: Efectivo, Tarjeta, Transferencia, PSE
- **Canales**: Tienda física, Web, Teléfono, WhatsApp

## 🚀 Uso

### Opción 1: Ejecutar con archivo BAT (Recomendado)

1. Doble clic en `GENERAR_DATOS_PRUEBA.bat`
2. Leer la información presentada
3. Confirmar con "si" o "s"
4. Esperar a que se generen los datos

### Opción 2: Ejecutar manualmente

```bash
python generar_datos_prueba.py
```

### Opción 3: Desde Django shell

```python
python manage.py shell
>>> from generar_datos_prueba import main
>>> main()
```

## 📋 Ejemplo de Salida

```
==================================================
  GENERADOR DE DATOS DE PRUEBA - DIGIT SOFT
==================================================

Este script generará datos de prueba sin afectar datos existentes.

¿Qué se va a crear?
  • 20 Clientes
  • 5 Categorías de Productos
  • 30 Productos
  • 15 Ventas con sus detalles

==================================================

¿Deseas continuar? (si/no): si

🚀 Iniciando generación de datos de prueba...

📋 Generando 20 clientes...
  ✅ 20 clientes creados exitosamente

📦 Generando categorías de productos...
  ✅ Categoría 'Laptops' creada
  ✅ Categoría 'Smartphones' creada
  ...

🛍️  Generando 30 productos...
  ✅ 30 productos creados exitosamente

💰 Generando 15 ventas...
  ✅ 15 ventas creadas exitosamente

==================================================
  RESUMEN DE DATOS GENERADOS
==================================================

📊 Estadísticas:
  • Total de clientes: 20
  • Total de categorías: 5
  • Total de productos: 30
  • Total de ventas: 15
  • Total en ventas generadas: $45,750,000.00 COP

==================================================
  ✅ DATOS DE PRUEBA GENERADOS EXITOSAMENTE
==================================================

💡 Puedes ver los datos en el panel de administración:
   http://127.0.0.1:8000/admin/

💡 O en la tienda online:
   http://127.0.0.1:8000/tienda/

==================================================
```

## 🔧 Personalización

### Cambiar la cantidad de datos

Edita el archivo `generar_datos_prueba.py` en la función `main()`:

```python
def main():
    # ...
    clientes = generar_clientes(50)  # Cambia 20 a 50
    productos = generar_productos(categorias, 100)  # Cambia 30 a 100
    ventas = generar_ventas(clientes, productos, 50)  # Cambia 15 a 50
```

### Cambiar el idioma de Faker

Cambia la línea de inicialización:

```python
# Español de España
fake = Faker('es_ES')

# Español de México
fake = Faker('es_MX')

# Español de Colombia
fake = Faker('es_CO')

# Inglés
fake = Faker('en_US')
```

### Agregar más categorías

Edita la lista `categorias_data` en la función `generar_categorias()`:

```python
categorias_data = [
    # ...existentes...
    {
        'nombre': 'Periféricos',
        'descripcion': 'Mouse, teclados, monitores'
    },
]
```

## 🔍 Verificación de Datos

### En el Admin de Django
1. Inicia el servidor: `python manage.py runserver`
2. Ve a: http://127.0.0.1:8000/admin/
3. Login con tu superusuario
4. Navega por las secciones: Clientes, Productos, Ventas

### En la Tienda Online
1. Ve a: http://127.0.0.1:8000/tienda/
2. Verás los productos generados
3. Puedes probar el proceso de compra

### Desde Django Shell
```python
python manage.py shell

>>> from clientes.models import Cliente
>>> Cliente.objects.count()
20

>>> from productos.models import Producto
>>> Producto.objects.filter(disponible_web=True).count()
22

>>> from ventas.models import Venta
>>> Venta.objects.filter(estado='COMPLETADA').count()
10
```

## 📦 Dependencias

El script requiere:
- ✅ **Faker** - Ya instalado (versión 30.8.2)
- ✅ **Django** - Framework principal
- ✅ **Python 3.x** - Lenguaje de programación

## 🛡️ Seguridad

- El script es **completamente seguro**
- No elimina datos existentes
- Cada ejecución genera datos nuevos con identificadores únicos
- En caso de error, se muestra el mensaje pero no afecta la base de datos

## 🔄 Limpiar Datos de Prueba

Si deseas eliminar SOLO los datos generados por Faker:

### ⚠️ PRECAUCIÓN: Esto eliminará datos

```python
python manage.py shell

>>> from clientes.models import Cliente
>>> from productos.models import Producto
>>> from ventas.models import Venta

# Verificar cuántos hay
>>> Cliente.objects.count()
>>> Producto.objects.count()
>>> Venta.objects.count()

# Eliminar TODOS (cuidado)
>>> Cliente.objects.all().delete()
>>> Producto.objects.all().delete()
>>> Venta.objects.all().delete()
```

**Mejor opción**: Crear un script de limpieza selectivo basado en fechas o etiquetas.

## 💡 Casos de Uso

### 1. Desarrollo
- Probar funcionalidades con datos realistas
- Validar interfaz de usuario con contenido real
- Testing de búsquedas y filtros

### 2. Demostraciones
- Presentar el sistema a clientes
- Capacitaciones de usuarios
- Videos y tutoriales

### 3. Testing
- Pruebas de carga
- Pruebas de rendimiento
- Validación de reportes

### 4. Desarrollo de Reportes
- Crear dashboards con datos
- Probar gráficos y estadísticas
- Validar cálculos

## 🆘 Solución de Problemas

### Error: "No module named 'faker'"
```bash
pip install faker
```

### Error: "DJANGO_SETTINGS_MODULE"
Verifica que el archivo se ejecute desde la raíz del proyecto donde está `manage.py`

### Error al crear ventas
Verifica que existan clientes y productos primero. El script los crea en orden.

### Datos no aparecen
1. Verifica que no haya errores en la consola
2. Refresca el navegador (Ctrl+F5)
3. Verifica en el admin de Django

## 📝 Notas Adicionales

- Los SKU son únicos y se generan automáticamente
- Los números de documento son únicos por cliente
- Las ventas respetan el stock disponible (si está configurado)
- Los precios tienen márgenes realistas (30-80%)
- El 75% de productos están disponibles en web
- El 25% de productos son destacados

## 🔗 Recursos

- [Documentación de Faker](https://faker.readthedocs.io/)
- [Faker en GitHub](https://github.com/joke2k/faker)
- [Proveedores de Faker](https://faker.readthedocs.io/en/master/providers.html)

## ✅ Checklist de Implementación

- [x] Faker instalado
- [x] Script de generación creado
- [x] Archivo BAT para ejecución rápida
- [x] Confirmación de usuario implementada
- [x] Manejo de errores robusto
- [x] Generación de clientes
- [x] Generación de categorías
- [x] Generación de productos con especificaciones
- [x] Generación de ventas con detalles
- [x] Actualización automática de stock
- [x] Cálculo de totales
- [x] Documentación completa

---

**Desarrollado para DIGIT SOFT** 🚀  
*Sistema de Gestión Integral con E-commerce*

