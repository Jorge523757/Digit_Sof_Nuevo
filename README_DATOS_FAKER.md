- Números de orden únicos
- Equipos con fallas reportadas
- Técnicos asignados
- Diagnósticos y soluciones
- Repuestos utilizados
- Estados del proceso
- Prioridades (baja, media, alta, urgente)
- Costos de mano de obra

### 📜 Garantías
- Productos con garantía
- Compradores y sus datos
- Fechas de compra y vencimiento
- Estados (activa, vencida, en revisión)
- Reclamaciones y problemas
- Soluciones aplicadas
- Números de factura

### 📦 Compras
- Compras a proveedores
- Múltiples productos por compra (1-8 items)
- Cantidades mayoristas (5-50 unidades)
- Cálculo de totales con IVA
- Fechas de entrega esperadas y reales
- Estados del pedido
- Métodos de pago
- Números de factura

### 🎓 Capacitaciones
- Cursos y entrenamientos
- Técnicos inscritos
- Fechas de inicio y fin
- Duración en horas
- Modalidades (presencial, virtual, híbrida)
- Calificaciones de participantes
- Certificados
- Costos

## 🎯 Características Especiales

### Coherencia de Datos
- Las fechas de venta son anteriores a las actuales
- Las garantías tienen fechas coherentes con las compras
- Los precios de venta son mayores que los de compra
- Los stocks son positivos
- Las relaciones entre modelos son válidas

### Variedad
- 75% de registros activos, 25% inactivos
- Estados variados para simular operación real
- Algunos campos opcionales se rellenan aleatoriamente
- Datos en español para mayor realismo local

### Detalles
- Cada venta tiene de 1 a 5 productos
- Cada orden puede tener de 0 a 3 repuestos
- Cada compra tiene de 1 a 8 productos
- Cada capacitación tiene de 3 a 30 participantes

## 📈 Resultados

Al finalizar, verás un resumen como:

```
✅ GENERACIÓN COMPLETADA EXITOSAMENTE
════════════════════════════════════════════════════════════════════

📊 RESUMEN DE DATOS GENERADOS:
   • 30 Clientes
   • 10 Categorías de Productos
   • 50 Productos
   • 15 Proveedores
   • 25 Equipos
   • 10 Técnicos
   • 40 Ventas
   • 120 Detalles de Venta
   • 30 Órdenes de Servicio
   • 45 Detalles de Orden
   • 25 Garantías
   • 20 Compras
   • 95 Detalles de Compra
   • 15 Capacitaciones
   • 78 Participantes en Capacitaciones

🎉 ¡Todos los módulos han sido poblados con datos de prueba!
```

## 🛠️ Solución de Problemas

### Error: "No module named 'faker'"
```bash
pip install faker
```

### Error: "DJANGO_SETTINGS_MODULE"
Asegúrate de ejecutar el script desde la carpeta raíz del proyecto.

### Error: "RelatedObjectDoesNotExist"
Algunos modelos pueden tener dependencias. El script las maneja automáticamente.

### Datos duplicados
Usa la opción de limpieza al inicio del script.

## 📝 Notas Importantes

- ⚠️ **Entorno de Desarrollo**: Este script es solo para desarrollo/pruebas
- 🔒 **No usar en producción**: Los datos son falsos
- 💾 **Backup**: Haz respaldo antes de limpiar datos existentes
- 🔄 **Múltiples ejecuciones**: Puedes ejecutarlo varias veces

## 📞 Soporte

Si encuentras algún problema:
1. Verifica que todas las migraciones estén aplicadas: `python manage.py migrate`
2. Verifica que Faker esté instalado: `pip list | findstr faker`
3. Revisa los mensajes de error en la consola

## 🎉 ¡Listo!

Ahora tu sistema tiene datos de prueba completos y realistas en todos los módulos.

---

**Fecha de creación**: Diciembre 2025  
**Autor**: Sistema de Generación Automática  
**Versión**: 1.0
# 🎲 Generador de Datos de Prueba con Faker - DIGIT SOFT

## 📋 Descripción

Este script genera datos falsos realistas para **TODOS** los módulos del sistema DIGIT SOFT utilizando la librería **Faker**.

## ✨ Características

### Módulos Incluidos

- ✅ **Clientes** (30 registros)
- ✅ **Categorías de Productos** (10 categorías)
- ✅ **Productos** (50 productos con especificaciones técnicas)
- ✅ **Proveedores** (15 proveedores)
- ✅ **Equipos** (25 equipos de la empresa)
- ✅ **Técnicos** (10 técnicos)
- ✅ **Ventas** (40 ventas con detalles)
- ✅ **Órdenes de Servicio** (30 órdenes con repuestos)
- ✅ **Garantías** (25 garantías)
- ✅ **Compras** (20 compras a proveedores)
- ✅ **Capacitaciones** (15 capacitaciones con participantes)

### Datos Generados

- 📝 Nombres, direcciones, teléfonos y correos en español
- 💰 Precios realistas con decimales
- 📅 Fechas coherentes entre sí
- 🔢 Códigos únicos (SKU, órdenes, ventas, etc.)
- 📊 Relaciones entre modelos correctamente establecidas
- 🎯 Estados y opciones variadas

## 🚀 Uso

### Opción 1: Usar el archivo .bat (Recomendado)

```bash
GENERAR_DATOS_FAKER.bat
```

Este archivo:
1. Verifica si Faker está instalado
2. Lo instala automáticamente si es necesario
3. Ejecuta el script de generación

### Opción 2: Ejecutar manualmente

```bash
# Instalar Faker (si no está instalado)
pip install faker

# Ejecutar el script
python generar_datos_faker.py
```

## 📦 Instalación de Dependencias

Si Faker no está instalado:

```bash
pip install faker
```

## ⚙️ Configuración

### Cantidad de Datos

Puedes modificar las cantidades en el archivo `generar_datos_faker.py`:

```python
clientes = crear_clientes(30)          # Cambiar 30 por la cantidad deseada
productos = crear_productos(categorias, 50)  # Cambiar 50 por la cantidad deseada
ventas = crear_ventas(clientes, productos, 40)  # etc...
```

### Idioma

El script usa Faker en español (`es_ES`). Para cambiar el idioma, modifica:

```python
fake = Faker('es_ES')  # Cambiar a 'en_US', 'fr_FR', etc.
```

## 🔄 Limpieza de Datos

Al ejecutar el script, se te preguntará:

```
¿Desea limpiar los datos existentes? (s/n):
```

- **s (Sí)**: Elimina todos los datos existentes antes de generar nuevos
- **n (No)**: Agrega datos nuevos a los existentes (puede causar duplicados)

⚠️ **ADVERTENCIA**: La limpieza eliminará TODOS los datos de los módulos listados.

## 📊 Datos Generados por Módulo

### 👥 Clientes
- Nombres y apellidos realistas
- Documentos únicos (10 dígitos)
- Teléfonos, correos, direcciones
- Estado activo/inactivo
- Observaciones aleatorias

### 💻 Productos
- Nombres de productos con marcas (Dell, HP, Lenovo, etc.)
- Códigos SKU únicos
- Especificaciones técnicas (procesador, RAM, almacenamiento)
- Precios con margen realista (20-80%)
- Stock, imágenes, garantías
- Clasificación por categorías

### 🏢 Proveedores
- Empresas con NIT válido
- Contactos, teléfonos, correos
- Condiciones de pago y entrega
- Calificaciones (1-5 estrellas)
- Productos/servicios que ofrecen

### 🖥️ Equipos
- Equipos de la empresa (computadores, laptops, servidores)
- Códigos únicos, marcas, modelos
- Especificaciones técnicas
- Estados (operativo, en reparación, etc.)
- Valores de adquisición
- Ubicaciones y responsables

### 👨‍🔧 Técnicos
- Nombres completos
- Documentos únicos
- Profesiones (Ingeniero de Sistemas, Técnico, etc.)
- Contactos
- Estado activo/inactivo

### 🛒 Ventas
- Números de venta únicos
- Clientes asociados
- Múltiples productos por venta (1-5 items)
- Cálculo automático de totales
- Descuentos e impuestos (IVA 19%)
- Estados (pendiente, completada, etc.)
- Canales de venta (tienda, web, teléfono)
- Métodos de pago variados

### 🔧 Órdenes de Servicio

