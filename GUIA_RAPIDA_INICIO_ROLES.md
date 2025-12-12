# 🚀 GUÍA RÁPIDA DE INICIO - SISTEMA DE ROLES

## ⚡ INICIO EN 5 MINUTOS

### 👤 PARA ADMINISTRADORES

```
1. Iniciar sesión como Admin
   └─> URL: /usuarios/login/

2. Acceder al Dashboard
   └─> Ver órdenes pendientes, métricas clave
   └─> Revisar notificaciones críticas

3. Asignar técnico a orden
   └─> Ir a: Órdenes de Servicio
   └─> Seleccionar orden sin asignar
   └─> Click "Asignar Técnico"
   └─> Elegir técnico disponible
   └─> Guardar

4. Aprobar garantía
   └─> Ir a: Garantías
   └─> Revisar solicitud
   └─> Ver informe técnico
   └─> Aprobar o rechazar con justificación

Tiempo promedio: 5-10 minutos por acción
```

### 🔧 PARA TÉCNICOS

```
1. Iniciar sesión como Técnico
   └─> URL: /usuarios/login/

2. Ver "Mis Órdenes"
   └─> Órdenes ordenadas por prioridad
   └─> Ver detalles de cada una

3. Actualizar estado de orden
   └─> Seleccionar orden
   └─> Click "Actualizar Estado"
   └─> Elegir nuevo estado
   └─> Agregar observaciones
   └─> Guardar

4. Completar orden
   └─> Estado: REPARADA
   └─> Documentar solución aplicada
   └─> Notificar administrador
   └─> Esperar facturación

Tiempo promedio: 3-5 minutos por actualización
```

### 👨‍💼 PARA CLIENTES

```
1. Registrarse o iniciar sesión
   └─> URL: /usuarios/registro/ (si es nuevo)
   └─> URL: /usuarios/login/ (si tiene cuenta)

2. Solicitar servicio
   └─> Describir problema
   └─> Proporcionar datos del equipo
   └─> Esperar asignación de técnico

3. Comprar producto
   └─> Explorar catálogo
   └─> Agregar al carrito
   └─> Checkout
   └─> Confirmar pedido

4. Solicitar garantía
   └─> Ir a: Mis Compras
   └─> Seleccionar producto
   └─> Click "Solicitar Garantía"
   └─> Describir problema + adjuntar evidencias
   └─> Enviar solicitud

Tiempo promedio: 10-15 minutos
```

### 📦 PARA PROVEEDORES

```
1. Iniciar sesión como Proveedor
   └─> URL: /usuarios/login/

2. Ver pedidos pendientes
   └─> Dashboard → Pedidos Pendientes
   └─> Priorizar por urgencia

3. Procesar pedido
   └─> Seleccionar pedido
   └─> Verificar inventario
   └─> Preparar despacho
   └─> Actualizar estado

4. Gestionar inventario
   └─> Ir a: Mis Productos
   └─> Actualizar stock
   └─> Revisar alertas de stock crítico

Tiempo promedio: 5-10 minutos por pedido
```

---

## 📊 MATRIZ RÁPIDA DE PERMISOS

| Acción | Admin | Técnico | Cliente | Proveedor |
|--------|-------|---------|---------|-----------|
| **Ver todas las órdenes** | ✅ | ❌ | ❌ | ❌ |
| **Ver órdenes asignadas** | ✅ | ✅ | ❌ | ❌ |
| **Ver órdenes propias** | ✅ | ✅ | ✅ | ❌ |
| **Asignar técnicos** | ✅ | ❌ | ❌ | ❌ |
| **Actualizar órdenes** | ✅ | ✅* | ❌ | ❌ |
| **Ver todos los clientes** | ✅ | ⚠️ | ❌ | ❌ |
| **Registrar clientes** | ✅ | ✅ | ❌ | ❌ |
| **Gestionar garantías** | ✅ | ⚠️ | ❌ | ❌ |
| **Solicitar garantías** | ✅ | ❌ | ✅ | ❌ |
| **Ver catálogo completo** | ✅ | ✅ | ✅ | ⚠️ |
| **Gestionar productos** | ✅ | ❌ | ❌ | ✅** |
| **Procesar ventas** | ✅ | ❌ | ✅*** | ✅** |
| **Ver reportes globales** | ✅ | ❌ | ❌ | ❌ |
| **Ver reportes propios** | ✅ | ✅ | ✅ | ✅ |

**Leyenda:**
- ✅ Sí, completo
- ⚠️ Sí, limitado
- ❌ No
- \* Solo sus órdenes asignadas
- \** Solo sus propios productos
- \*** Solo puede comprar

---

## 🔔 PRIORIDADES DE NOTIFICACIONES

```
🔴 CRÍTICA - Atención INMEDIATA
   • Sistema caído
   • Orden con problema grave
   • Cliente muy insatisfecho

⚠️ ALTA - Atender en < 4 horas
   • Nueva orden asignada (técnico)
   • Orden completada (admin)
   • Solicitud de garantía
   • Orden atrasada

📢 MEDIA - Atender en < 24 horas
   • Actualización de estado
   • Nueva venta
   • Stock bajo
   • Cliente consulta

📌 BAJA - Cuando sea posible
   • Recordatorios
   • Promociones
   • Newsletter
   • Backups completados
```

---

## 🔄 ESTADOS DE ORDEN DE SERVICIO

```
RECIBIDA
   ↓ (Admin registra y asigna)
ASIGNADA
   ↓ (Técnico inicia trabajo)
EN_DIAGNOSTICO
   ↓ (Técnico completa diagnóstico)
DIAGNOSTICADA
   ↓ (Cliente aprueba presupuesto)
EN_REPARACION
   ↓ (Técnico repara)
REPARADA
   ↓ (Admin genera factura)
LISTA_ENTREGA
   ↓ (Cliente recoge)
ENTREGADA ✅

Estados especiales:
├─ EN_ESPERA_REPUESTOS (faltan partes)
├─ EN_ESPERA_CLIENTE (falta info)
└─ CANCELADA (cliente cancela)
```

---

## 🎯 ACCIONES RÁPIDAS POR ROL

### Administrador
```
✅ Asignar técnico: /ordenes/{id}/asignar/
✅ Aprobar garantía: /garantias/{id}/aprobar/
✅ Generar reporte: /reportes/crear/
✅ Gestionar usuarios: /usuarios/gestionar/
✅ Ver métricas: /dashboard/
```

### Técnico
```
✅ Actualizar orden: /ordenes/{id}/actualizar/
✅ Registrar cliente: /clientes/crear/
✅ Ver mis órdenes: /ordenes/mis-ordenes/
✅ Generar reporte: /reportes/tecnico/
✅ Mi rendimiento: /dashboard/rendimiento/
```

### Cliente
```
✅ Solicitar servicio: /ordenes/solicitar/
✅ Comprar producto: /tienda/
✅ Ver mis órdenes: /ordenes/mis-servicios/
✅ Solicitar garantía: /garantias/solicitar/
✅ Ver facturas: /facturas/
```

### Proveedor
```
✅ Ver pedidos: /ventas/mis-ventas/
✅ Gestionar productos: /productos/mis-productos/
✅ Actualizar inventario: /inventario/
✅ Ver reportes: /reportes/mis-ventas/
✅ Procesar despacho: /ventas/{id}/despachar/
```

---

## ⚙️ CONFIGURACIÓN INICIAL

### Primera Vez en el Sistema

1. **Cambiar contraseña por defecto**
   ```
   Usuario → Perfil → Cambiar Contraseña
   ```

2. **Actualizar información de perfil**
   ```
   Usuario → Perfil → Editar
   ├─ Foto de perfil
   ├─ Teléfono
   ├─ Dirección
   └─ Otros datos
   ```

3. **Configurar notificaciones**
   ```
   Usuario → Configuración → Notificaciones
   ├─ Habilitar/deshabilitar canales
   ├─ Definir frecuencia
   └─ Horario de No Molestar
   ```

4. **Explorar el dashboard**
   ```
   Familiarizarse con:
   ├─ Métricas principales
   ├─ Accesos rápidos
   ├─ Notificaciones
   └─ Menú de navegación
   ```

---

## 🆘 SOLUCIÓN RÁPIDA DE PROBLEMAS

### "No puedo ver una orden"

```
❓ Causa: No tienes permisos
✅ Solución:
   1. Verificar tu rol (Usuario → Perfil)
   2. Si eres técnico, solo ves órdenes asignadas
   3. Si eres cliente, solo ves tus órdenes
   4. Contactar admin si persiste
```

### "No puedo asignar técnico"

```
❓ Causa: No eres administrador
✅ Solución:
   1. Solo admins pueden asignar
   2. Contactar a tu administrador
   3. Solicitar cambio de rol si corresponde
```

### "No recibo notificaciones"

```
❓ Causa: Configuración desactivada
✅ Solución:
   1. Ir a: Usuario → Configuración → Notificaciones
   2. Verificar canales habilitados
   3. Revisar carpeta spam (si email)
   4. Actualizar preferencias
```

### "La orden no cambia de estado"

```
❓ Causa: Faltan datos requeridos
✅ Solución:
   1. Verificar campos obligatorios
   2. Agregar observaciones detalladas
   3. Si es diagnóstico, incluir costos
   4. Revisar permisos
```

---

## 📞 CONTACTO RÁPIDO

```
🆘 Soporte Técnico:
   • Email: soporte@digitsoft.com
   • Teléfono: +52 (XXX) XXX-XXXX
   • Chat: Disponible 9:00-18:00

📧 Consultas Comerciales:
   • Email: ventas@digitsoft.com
   • WhatsApp: +52 (XXX) XXX-XXXX

💼 Administración:
   • Email: admin@digitsoft.com
   • Interno: Ext. 100
```

---

## 📚 RECURSOS ADICIONALES

### Documentación Completa

```
📄 Índice Maestro:
   INDICE_MAESTRO_ESPECIFICACION_FUNCIONAL.md

📄 Resumen Ejecutivo:
   RESUMEN_EJECUTIVO_SISTEMA_ROLES.md

📄 Especificaciones:
   ├─ ESPECIFICACION_FUNCIONAL_ROLES_Y_PERMISOS.md
   ├─ ESPECIFICACION_FUNCIONAL_NOTIFICACIONES_Y_MODULOS.md
   └─ ESPECIFICACION_FUNCIONAL_IMPLEMENTACION_Y_CASOS_USO.md
```

### Videos Tutorial (Próximamente)

```
🎥 Introducción al Sistema (15 min)
🎥 Dashboard por Rol (4 videos × 10 min)
🎥 Gestión de Órdenes (20 min)
🎥 Sistema de Notificaciones (15 min)
```

---

## ✅ CHECKLIST DE INICIO

### Para Administradores

```
□ Iniciar sesión
□ Revisar dashboard
□ Ver órdenes pendientes
□ Asignar primera orden
□ Configurar notificaciones
□ Revisar métricas del sistema
□ Conocer el equipo técnico
```

### Para Técnicos

```
□ Iniciar sesión
□ Ver mis órdenes
□ Actualizar estado de una orden
□ Registrar un cliente de prueba
□ Configurar notificaciones
□ Revisar mi rendimiento
```

### Para Clientes

```
□ Registrarse/Iniciar sesión
□ Explorar catálogo
□ Ver productos disponibles
□ Revisar mis órdenes (si hay)
□ Configurar perfil
□ Entender sistema de garantías
```

### Para Proveedores

```
□ Iniciar sesión
□ Revisar dashboard
□ Ver mis productos
□ Actualizar inventario
□ Configurar alertas de stock
□ Revisar pedidos pendientes
```

---

## 🎓 TIPS Y MEJORES PRÁCTICAS

### General

```
✅ Mantén tu perfil actualizado
✅ Revisa notificaciones diariamente
✅ Usa filtros para encontrar información rápido
✅ Actualiza estados en tiempo real
✅ Documenta todo detalladamente
```

### Administradores

```
✅ Asigna técnicos considerando especialidad y carga
✅ Responde garantías en < 48 horas
✅ Genera reportes semanales
✅ Mantén comunicación con el equipo
✅ Revisa órdenes atrasadas diariamente
```

### Técnicos

```
✅ Actualiza órdenes al menos 2 veces al día
✅ Documenta diagnósticos detalladamente
✅ Notifica problemas inmediatamente
✅ Mantén calidad consistente
✅ Comunícate claramente
```

### Clientes

```
✅ Proporciona información completa al solicitar servicio
✅ Revisa presupuestos cuidadosamente
✅ Guarda tu factura para garantías
✅ Califica el servicio recibido
✅ Contacta soporte ante dudas
```

### Proveedores

```
✅ Mantén inventario actualizado
✅ Procesa pedidos en < 24 horas
✅ Responde consultas rápidamente
✅ Documenta entregas
✅ Revisa reportes de ventas semanalmente
```

---

**Última actualización:** Diciembre 2024  
**Versión:** 1.0  
**Tiempo de lectura:** 10 minutos

