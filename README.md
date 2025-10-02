# 🚀 DIGIT SOFT - Sistema de Gestión Empresarial

## 📋 Descripción
Sistema completo de gestión empresarial desarrollado en Django para DIGIT SOFT, especializado en soluciones tecnológicas. Incluye módulos interrelacionados para administración, ventas, compras, servicios técnicos y más.

## ✨ Características Principales

### 🎨 Interfaz Moderna
- **Modo Oscuro/Claro**: Toggle dinámico para cambio de tema
- **Diseño Responsive**: Adaptable a dispositivos móviles
- **Animaciones Suaves**: Efectos visuales elegantes
- **Colores Intuitivos**: Esquema de colores profesional

### 📊 Módulos Disponibles

#### 🏠 **Panel Principal** (`/`)
- Página de inicio con información de la empresa
- Navegación hacia todos los módulos
- Diseño corporativo moderno

#### 👨‍💼 **Panel de Administración** (`/administrador/`)
- Dashboard con estadísticas generales
- Resumen de actividad del sistema
- Métricas de rendimiento
- Órdenes y ventas recientes

#### 👥 **Gestión de Clientes** (`/gestion-clientes/`)
- Lista completa de clientes
- Órdenes de servicio relacionadas
- Historial de ventas
- Información de contacto
- Servicios técnicos vinculados

#### 📦 **Gestión de Productos** (`/gestion-productos/`)
- Inventario completo
- Control de stock
- Historial de compras y ventas por producto
- Información de marcas
- Alertas de stock bajo

#### 🚛 **Gestión de Proveedores** (`/gestion-proveedores/`)
- Directorio de proveedores
- Historial de compras por proveedor
- Productos suministrados
- Información de contacto

#### 🛒 **Gestión de Compras** (`/gestion-compras/`)
- Registro de compras de mercancía
- Relación con proveedores y productos
- Fechas y cantidades
- Administradores responsables

#### 💰 **Gestión de Ventas** (`/gestion-ventas/`)
- Historial completo de ventas
- Relación cliente-producto
- Valores y cantidades vendidas
- Fechas de transacciones

#### 🔧 **Gestión de Técnicos** (`/gestion-tecnicos/`)
- Personal técnico especializado
- Órdenes asignadas por técnico
- Especialidades y tipos
- Servicios realizados

#### 📋 **Órdenes de Servicio** (`/orden-servicio/`)
- Gestión completa de órdenes
- Estados: Pendiente/Completada
- Asignación de técnicos
- Relación con facturación

#### 🛠️ **Servicio Técnico** (`/servicio-tecnico/`)
- Servicios técnicos realizados
- Vinculación con órdenes y clientes
- Seguimiento de técnicos

#### 🛡️ **Gestión de Garantías** (`/gestion-garantias/`)
- Control de garantías
- Referencias a facturación
- Estados de garantía

## 🗄️ Base de Datos

### Modelos Implementados
- **Cliente**: Información completa de clientes
- **Proveedor**: Datos de proveedores
- **Técnico**: Personal especializado
- **Administrador**: Usuarios del sistema
- **Marca**: Marcas de productos
- **Producto**: Inventario con stock
- **OrdenServicio**: Órdenes de trabajo
- **ServicioTecnico**: Servicios realizados
- **Ventas**: Transacciones de venta
- **ComprasMercancia**: Compras a proveedores
- **Garantias**: Control de garantías
- **Facturacion**: Facturación del sistema

### Relaciones Implementadas
- Cliente → OrdenServicio (1:N)
- Cliente → Ventas (1:N)
- Técnico → OrdenServicio (1:N)
- Producto → Ventas (1:N)
- Proveedor → ComprasMercancia (1:N)
- Marca → Producto (1:N)

## 🔧 Funcionalidades Técnicas

### Backend (Django)
- **Modelos ORM**: Relaciones complejas entre entidades
- **Vistas basadas en funciones**: Lógica de negocio optimizada
- **Paginación**: Manejo eficiente de grandes datasets
- **Consultas optimizadas**: Select_related para mejor rendimiento

### Frontend
- **Templates responsivos**: Bootstrap-like grid system
- **CSS Variables**: Fácil personalización de temas
- **JavaScript vanilla**: Sin dependencias externas
- **LocalStorage**: Persistencia de preferencias de usuario

### UI/UX
- **Tarjetas estadísticas**: Métricas visuales atractivas
- **Tablas interactivas**: Datos relacionados expandibles
- **Botones de acción**: Interfaces intuitivas
- **Estados de loading**: Animaciones durante cargas

## 🚀 URLs del Sistema

### Principales
- `/` - Página de inicio
- `/administrador/` - Panel de administración
- `/servicios/` - Página de servicios

### Módulos de Gestión
- `/gestion-clientes/` - Gestión de clientes
- `/gestion-productos/` - Gestión de productos
- `/gestion-proveedores/` - Gestión de proveedores
- `/gestion-compras/` - Gestión de compras
- `/gestion-ventas/` - Gestión de ventas
- `/gestion-tecnicos/` - Gestión de técnicos
- `/orden-servicio/` - Órdenes de servicio
- `/servicio-tecnico/` - Servicios técnicos
- `/gestion-garantias/` - Gestión de garantías

### APIs
- `/api/contact/` - Formulario de contacto
- `/api/login/` - Sistema de login

## 📊 Datos de Prueba Incluidos

### Marcas
- HP, Dell, Lenovo, Canon, Epson

### Clientes
- Carlos Mendoza, Ana Rodríguez, Luis Martínez

### Productos
- Laptop HP Pavilion
- Impresora Canon PIXMA
- Desktop Dell OptiPlex

### Técnicos
- Roberto Silva (Senior - Hardware)
- Sandra López (Junior - Software)

### Proveedores
- TecnoSupplies Ltda
- CompuWorld S.A.S

## 🎨 Temas Disponibles

### Modo Claro
- Fondos blancos y grises claros
- Texto oscuro para legibilidad
- Sombras sutiles

### Modo Oscuro
- Fondos oscuros elegantes
- Texto claro optimizado
- Contraste mejorado

## 🔄 Cómo Usar

1. **Iniciar el servidor**: `python manage.py runserver`
2. **Acceder al sistema**: `http://127.0.0.1:8000/`
3. **Navegar por módulos**: Usar el menú lateral
4. **Cambiar tema**: Botón en la esquina superior derecha
5. **Ver datos relacionados**: Expandir información en tablas

## 📱 Compatibilidad
- ✅ Desktop (Chrome, Firefox, Edge, Safari)
- ✅ Tablet (iPad, Android tablets)
- ✅ Móvil (iOS, Android)
- ✅ Modos claro y oscuro en todos los dispositivos

## 🏆 Características Destacadas
- **Datos interrelacionados**: Cada módulo muestra información conectada
- **Navegación intuitiva**: Fácil acceso a todas las funcionalidades
- **Performance optimizado**: Consultas eficientes y paginación
- **Diseño profesional**: Interfaz moderna y atractiva
- **Escalabilidad**: Arquitectura preparada para crecimiento

---

**Desarrollado para DIGIT SOFT - Soluciones Tecnológicas**
*Sistema completo de gestión empresarial con base de datos interrelacionada*