# 🚀 GUÍA RÁPIDA DE INICIO - DIGITSOFT

## ✅ PROBLEMA RESUELTO
Las tablas y módulos ahora se visualizan correctamente. Todos los problemas de z-index y JavaScript han sido corregidos.

## 🎯 INICIO RÁPIDO (3 PASOS)

### Paso 1: Iniciar el Servidor
Haz doble clic en el archivo:
```
INICIAR_SERVIDOR_CORREGIDO.bat
```

O ejecuta manualmente:
```bash
python manage.py runserver
```

### Paso 2: Acceder al Sistema
Abre tu navegador en:
```
http://127.0.0.1:8000
```

### Paso 3: Probar los Módulos
- Dashboard: http://127.0.0.1:8000/dashboard/
- Clientes: http://127.0.0.1:8000/clientes/
- Productos: http://127.0.0.1:8000/productos/
- Tienda: http://127.0.0.1:8000/tienda/

## ✅ VERIFICACIÓN DE CORRECCIONES

### 1. Tablas Visibles ✅
- Ve a "Gestión de Clientes"
- La tabla debe mostrarse con 72 clientes
- Todas las columnas deben ser visibles
- Los botones de acción (👁️ ✏️ 🗑️) funcionan

### 2. Panel de Accesibilidad ✅
- Click en el botón verde (♿) abajo a la derecha
- El panel se abre SIN tapar la tabla
- Todas las opciones funcionan:
  - Aumentar/Reducir texto
  - Alto contraste
  - Modo lectura
  - Escala de grises
  - Subrayar enlaces

### 3. Botón WhatsApp ✅
- Click en el botón verde de WhatsApp
- Te redirige correctamente
- NO tapa el contenido

### 4. Sidebar Responsive ✅
- Click en el botón de hamburguesa (☰)
- El sidebar se abre desde la izquierda
- Click fuera para cerrarlo
- En móvil funciona correctamente

## 🎨 FUNCIONALIDADES DISPONIBLES

### Gestión de Clientes
- ✅ Registrar nuevo cliente
- ✅ Buscar por nombre/documento
- ✅ Filtrar por estado
- ✅ Ver detalles (ojo azul)
- ✅ Editar (lápiz amarillo)
- ✅ Eliminar (basura roja)
- ✅ Reportes PDF/Excel

### Gestión de Productos
- ✅ Registrar producto
- ✅ Buscar productos
- ✅ Filtrar por categoría
- ✅ Gestionar stock
- ✅ Reportes

### Gestión de Ventas
- ✅ Crear venta
- ✅ Buscar ventas
- ✅ Ver detalles
- ✅ Reportes

### Tienda Online
- ✅ Ver productos
- ✅ Agregar al carrito
- ✅ Realizar checkout
- ✅ Ver historial de pedidos

## 📱 RESPONSIVE

El sistema es totalmente responsive:

### Desktop (1920px+)
- ✅ Todas las columnas visibles
- ✅ Widgets flotantes en esquina inferior derecha
- ✅ Sidebar lateral

### Tablet (768px - 1365px)
- ✅ Tabla con scroll horizontal
- ✅ Widgets ajustados
- ✅ Sidebar tipo overlay

### Móvil (320px - 767px)
- ✅ Tabla responsive con scroll
- ✅ Botones de acción apilados
- ✅ Widgets más pequeños
- ✅ Sidebar ocupando pantalla completa

## 🔧 SOLUCIÓN DE PROBLEMAS

### ❌ Las tablas no se ven
**Solución**:
1. Presiona F5 para recargar
2. Limpia caché: Ctrl + Shift + Delete
3. Abre la consola (F12) y busca errores

### ❌ Los widgets tapan el contenido
**Solución**:
1. Verifica que `z-index-fix.css` esté cargado
2. Inspecciona el elemento (F12)
3. Verifica z-index en consola

### ❌ El sidebar no abre
**Solución**:
1. Verifica la consola (F12)
2. Busca errores en `responsive.js`
3. Recarga la página (F5)

### ❌ Error 404 en archivos CSS
**Solución**:
```bash
python manage.py collectstatic --noinput
```

## 📊 DATOS DE PRUEBA

El sistema ya incluye datos de prueba:
- 📋 72 Clientes
- 📦 111 Productos
- 🛒 75 Ventas
- 👨‍💼 Técnicos
- 🔧 Órdenes de servicio
- Y más...

## 🎯 ACCIONES PRINCIPALES

### 1. Registrar un Cliente
```
1. Click en "Gestión de Clientes"
2. Click en "Registrar Nuevo Cliente"
3. Llenar formulario
4. Guardar
```

### 2. Buscar un Cliente
```
1. En "Gestión de Clientes"
2. Usar la caja de búsqueda
3. Buscar por nombre o documento
4. Los resultados se filtran automáticamente
```

### 3. Generar Reporte
```
1. Ir a cualquier módulo
2. Aplicar filtros si deseas
3. Click en "PDF" o "Excel"
4. El reporte se descarga automáticamente
```

### 4. Realizar una Venta
```
1. Click en "Gestión de Ventas"
2. Click en "Nueva Venta"
3. Seleccionar cliente
4. Agregar productos
5. Finalizar venta
```

### 5. Usar la Tienda
```
1. Click en "Tienda" en el header
2. Explorar productos
3. Agregar al carrito
4. Ver carrito
5. Realizar checkout
```

## 🎨 PERSONALIZACIÓN

### Cambiar Tema
- Click en el botón de accesibilidad (♿)
- Seleccionar opciones de visualización
- Los cambios se aplican instantáneamente

### Ajustar Tamaño de Texto
- Panel de accesibilidad
- "Aumentar Texto" o "Reducir Texto"
- 5 niveles disponibles

### Alto Contraste
- Panel de accesibilidad
- "Alto Contraste"
- Mejora visibilidad para usuarios con problemas visuales

## ⌨️ ATAJOS DE TECLADO

- **ESC**: Cerrar sidebar
- **Ctrl + F**: Buscar en tabla
- **Tab**: Navegar entre campos
- **Enter**: Enviar formulario

## 📱 PROBAR EN MÓVIL

### Opción 1: Responsive del Navegador
```
1. Presiona F12
2. Click en icono de móvil (arriba izquierda)
3. Selecciona dispositivo (iPhone, Samsung, etc.)
4. Prueba la interfaz
```

### Opción 2: Dispositivo Real
```
1. Encuentra la IP de tu PC: ipconfig
2. En el móvil: http://[TU_IP]:8000
3. Ejemplo: http://192.168.1.100:8000
```

## 🔐 USUARIOS DE PRUEBA

### Administrador
```
Usuario: admin
Contraseña: [tu contraseña]
```

Si no tienes usuario, crear uno:
```bash
python manage.py createsuperuser
```

## ✅ CHECKLIST DE VERIFICACIÓN

Marca cada ítem después de probar:

### Visualización
- [ ] Las tablas se muestran correctamente
- [ ] Los widgets no tapan contenido
- [ ] El sidebar abre y cierra correctamente
- [ ] Los botones de acción funcionan

### Funcionalidad
- [ ] Puedo registrar un cliente
- [ ] Puedo buscar clientes
- [ ] Puedo editar un cliente
- [ ] Puedo eliminar un cliente
- [ ] Los reportes se generan

### Responsive
- [ ] Funciona en desktop
- [ ] Funciona en tablet (F12 → responsive)
- [ ] Funciona en móvil (F12 → responsive)
- [ ] Los widgets se ajustan al tamaño

### Accesibilidad
- [ ] El panel de accesibilidad abre
- [ ] Puedo aumentar el texto
- [ ] El alto contraste funciona
- [ ] Puedo navegar con teclado

## 🎉 ¡LISTO PARA USAR!

Tu sistema DIGITSOFT está completamente funcional y corregido. Todos los módulos están operativos y listos para usar.

### Próximos Pasos Sugeridos:
1. ✅ Familiarízate con cada módulo
2. ✅ Prueba las funcionalidades principales
3. ✅ Genera algunos reportes
4. ✅ Prueba la tienda online
5. ✅ Explora las opciones de accesibilidad

## 📞 SOPORTE

Si encuentras algún problema:
1. Revisa la consola del navegador (F12)
2. Verifica que todos los archivos CSS/JS carguen
3. Consulta `CORRECCION_VISUALIZACION_COMPLETA.md`

## 🌟 CARACTERÍSTICAS DESTACADAS

- ✅ **100% Responsive**: Funciona en todos los dispositivos
- ✅ **Accesibilidad WCAG**: Cumple estándares internacionales
- ✅ **Sin errores**: Sistema completamente funcional
- ✅ **Reportes**: PDF y Excel en todos los módulos
- ✅ **Búsqueda dinámica**: Resultados instantáneos
- ✅ **Interfaz moderna**: Diseño profesional y atractivo

---

**Versión**: 1.0 - Corregida
**Fecha**: 2025-01-05
**Estado**: ✅ COMPLETAMENTE FUNCIONAL

