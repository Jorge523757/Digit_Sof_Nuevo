# 🧪 GUÍA DE PRUEBAS - VALIDACIONES EN ESPAÑOL
## Sistema DIGITSOFT

---

## 🎯 OBJETIVO
Verificar que todas las validaciones funcionen correctamente y muestren mensajes en español.

---

## 📝 INSTRUCCIONES GENERALES

1. Ejecutar el servidor: `VERIFICAR_VALIDACIONES.bat`
2. Abrir el navegador en: http://localhost:8000
3. Seguir las pruebas en orden
4. Anotar cualquier error encontrado

---

## 🔐 MÓDULO 1: LOGIN Y REGISTRO

### A. PRUEBAS DE LOGIN

#### ✅ Caso 1: Login Exitoso
**Pasos:**
1. Ir a http://localhost:8000/usuarios/login/
2. Ingresar usuario: `admin`
3. Ingresar contraseña: (tu contraseña de admin)
4. Hacer clic en "Iniciar Sesión"

**Resultado esperado:** Redirige al panel y muestra mensaje de bienvenida

---

#### ❌ Caso 2: Usuario Incorrecto
**Pasos:**
1. Ir a http://localhost:8000/usuarios/login/
2. Ingresar usuario: `usuarionoexiste`
3. Ingresar contraseña: `cualquiercontraseña`
4. Hacer clic en "Iniciar Sesión"

**Resultado esperado:** 
- Mensaje: "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."
- En español ✅

---

#### ❌ Caso 3: Campos Vacíos
**Pasos:**
1. Ir a http://localhost:8000/usuarios/login/
2. Dejar campos vacíos
3. Hacer clic en "Iniciar Sesión"

**Resultado esperado:** 
- El navegador muestra mensajes de validación HTML5
- Los campos se marcan como obligatorios

---

### B. PRUEBAS DE REGISTRO

#### ❌ Caso 1: Email Duplicado
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Usar un email ya registrado
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "Este correo electrónico ya está registrado. Por favor, usa otro correo o inicia sesión."
- En español ✅

---

#### ❌ Caso 2: Usuario Corto
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Ingresar usuario con menos de 4 caracteres (ej: "abc")
3. Llenar demás campos
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "El nombre de usuario debe tener al menos 4 caracteres."
- En español ✅

---

#### ❌ Caso 3: Contraseñas No Coinciden
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Contraseña: "MiPassword123"
4. Confirmar contraseña: "OtraPassword456"
5. Enviar formulario

**Resultado esperado:**
- Mensaje: "Las contraseñas no coinciden. Por favor, verifica e inténtalo de nuevo."
- En español ✅

---

#### ❌ Caso 4: Contraseña Muy Corta
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Contraseña: "abc123" (menos de 8 caracteres)
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "La contraseña debe tener al menos 8 caracteres."
- En español ✅

---

#### ❌ Caso 5: Contraseña Solo Números
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Contraseña: "12345678"
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "Esta contraseña es completamente numérica. Debe contener letras y otros caracteres."
- En español ✅

---

#### ❌ Caso 6: Teléfono Inválido
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Teléfono: "123" (menos de 10 dígitos)
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "El teléfono debe tener al menos 10 dígitos."
- En español ✅

---

#### ❌ Caso 7: Documento Duplicado
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos
3. Usar un documento ya registrado
4. Enviar formulario

**Resultado esperado:**
- Mensaje: "Este documento ya está registrado. Si ya tienes una cuenta, inicia sesión."
- En español ✅

---

#### ✅ Caso 8: Registro Exitoso
**Pasos:**
1. Ir a http://localhost:8000/usuarios/registro/
2. Llenar todos los campos correctamente:
   - Usuario: mínimo 4 caracteres, único
   - Email: formato válido, único
   - Nombres: mínimo 2 caracteres
   - Apellidos: mínimo 2 caracteres
   - Teléfono: mínimo 10 dígitos
   - Dirección: mínimo 10 caracteres
   - Documento: mínimo 5 caracteres, único
   - Contraseña: mínimo 8 caracteres, con letras y números
3. Enviar formulario

**Resultado esperado:**
- Mensaje: "¡Registro exitoso! Tu cuenta ha sido creada. Ahora puedes iniciar sesión."
- Redirige a login
- En español ✅

---

## 📦 MÓDULO 2: PRODUCTOS

### Acceso: Login → Productos → Nuevo Producto

#### ❌ Caso 1: SKU Duplicado
**Pasos:**
1. Crear producto con SKU existente
2. Llenar demás campos
3. Guardar

**Resultado esperado:**
- Mensaje: "Ya existe un producto con este código SKU. Por favor, usa un código diferente."
- En español ✅

---

#### ❌ Caso 2: Precio de Venta Menor que Compra
**Pasos:**
1. Precio de compra: $1000
2. Precio de venta: $800
3. Guardar

**Resultado esperado:**
- Mensaje: "El precio de venta debe ser mayor al precio de compra para tener ganancia."
- En español ✅

---

#### ❌ Caso 3: Stock Mínimo Mayor que Máximo
**Pasos:**
1. Stock mínimo: 50
2. Stock máximo: 30
3. Guardar

**Resultado esperado:**
- Mensaje: "El stock mínimo no puede ser mayor al stock máximo."
- En español ✅

---

#### ❌ Caso 4: Garantía Sin Meses
**Pasos:**
1. Marcar "Tiene garantía"
2. Dejar "Meses de garantía" vacío o en 0
3. Guardar

**Resultado esperado:**
- Mensaje: "Si el producto tiene garantía, debes especificar los meses de garantía."
- En español ✅

---

#### ✅ Caso 5: Producto Exitoso
**Pasos:**
1. Llenar todos los campos correctamente
2. SKU único, mínimo 3 caracteres
3. Nombre mínimo 3 caracteres
4. Precio compra < precio venta
5. Stock válido
6. Guardar

**Resultado esperado:**
- Producto creado exitosamente
- Mensaje de confirmación en español

---

## 💰 MÓDULO 3: VENTAS

### Acceso: Login → Ventas → Nueva Venta

#### ❌ Caso 1: Sin Cliente
**Pasos:**
1. No seleccionar cliente
2. Agregar productos
3. Guardar

**Resultado esperado:**
- Mensaje: "Debes seleccionar un cliente para la venta."
- En español ✅

---

#### ❌ Caso 2: Cantidad Mayor al Stock
**Pasos:**
1. Seleccionar producto con stock de 5 unidades
2. Ingresar cantidad: 10
3. Guardar

**Resultado esperado:**
- Mensaje: "Stock insuficiente. Solo hay 5 unidades disponibles."
- En español ✅

---

#### ❌ Caso 3: Descuento Mayor al 100%
**Pasos:**
1. Llenar venta
2. Descuento: 150%
3. Guardar

**Resultado esperado:**
- Mensaje: "El descuento no puede ser mayor al 100%."
- En español ✅

---

#### ❌ Caso 4: Entrega Sin Dirección
**Pasos:**
1. Marcar "Requiere entrega"
2. No llenar dirección de entrega
3. Guardar

**Resultado esperado:**
- Mensaje: "Si la venta requiere entrega, debes proporcionar la dirección."
- En español ✅

---

#### ✅ Caso 5: Venta Exitosa
**Pasos:**
1. Seleccionar cliente
2. Agregar productos con stock disponible
3. Cantidades válidas
4. Guardar

**Resultado esperado:**
- Venta registrada
- Stock actualizado
- Factura generada

---

## 👥 MÓDULO 4: CLIENTES

### Acceso: Login → Clientes → Nuevo Cliente

#### ❌ Caso 1: Nombres con Números
**Pasos:**
1. Nombres: "Juan123"
2. Llenar demás campos
3. Guardar

**Resultado esperado:**
- Mensaje: "Los nombres solo pueden contener letras y espacios."
- En español ✅

---

#### ❌ Caso 2: Documento Inválido
**Pasos:**
1. Documento: "abc" (menos de 5 dígitos o no numérico)
2. Guardar

**Resultado esperado:**
- Mensaje: "El documento debe contener entre 5 y 20 dígitos."
- En español ✅

---

#### ❌ Caso 3: Email Inválido
**Pasos:**
1. Email: "correosinformato"
2. Guardar

**Resultado esperado:**
- Mensaje: "Ingrese un correo electrónico válido."
- En español ✅

---

#### ❌ Caso 4: Dirección Muy Corta
**Pasos:**
1. Dirección: "Calle 1" (menos de 10 caracteres)
2. Guardar

**Resultado esperado:**
- Mensaje: "La dirección debe tener al menos 10 caracteres."
- En español ✅

---

#### ✅ Caso 5: Cliente Exitoso
**Pasos:**
1. Llenar todos los campos correctamente
2. Nombres y apellidos solo con letras
3. Documento numérico único
4. Email válido
5. Teléfono mínimo 7 dígitos
6. Dirección mínimo 10 caracteres
7. Guardar

**Resultado esperado:**
- Cliente creado exitosamente
- Datos capitalizados automáticamente

---

## 🛒 MÓDULO 5: COMPRAS

### Acceso: Login → Compras → Nueva Compra

#### ❌ Caso 1: Sin Proveedor
**Pasos:**
1. No seleccionar proveedor
2. Guardar

**Resultado esperado:**
- Mensaje: "Debes seleccionar un proveedor para la compra."
- En español ✅

---

#### ❌ Caso 2: Fecha de Entrega Pasada
**Pasos:**
1. Fecha de entrega: fecha anterior a hoy
2. Guardar

**Resultado esperado:**
- Mensaje: "La fecha de entrega no puede ser anterior a hoy."
- En español ✅

---

#### ❌ Caso 3: Descuento Inválido
**Pasos:**
1. Descuento: 150% o negativo
2. Guardar

**Resultado esperado:**
- Mensaje: "El descuento no puede ser mayor al 100%." o "El descuento no puede ser negativo."
- En español ✅

---

#### ✅ Caso 4: Compra Exitosa
**Pasos:**
1. Seleccionar proveedor activo
2. Fecha válida
3. Agregar productos
4. Descuentos e impuestos válidos
5. Guardar

**Resultado esperado:**
- Compra registrada
- Stock actualizado al recibir

---

## 📊 CHECKLIST FINAL

### Validaciones Generales
- [ ] Todos los mensajes están en español
- [ ] Los campos obligatorios están marcados
- [ ] Los formatos se validan correctamente
- [ ] Los límites se respetan

### Experiencia de Usuario
- [ ] Los mensajes son claros y útiles
- [ ] Las validaciones no bloquean el sistema
- [ ] Los errores se muestran en el lugar correcto
- [ ] La capitalización automática funciona

### Funcionalidad
- [ ] El login funciona correctamente
- [ ] El registro crea usuarios válidos
- [ ] Los productos se crean con datos válidos
- [ ] Las ventas actualizan el stock
- [ ] Los clientes se registran correctamente
- [ ] Las compras se procesan bien

---

## 🐛 REPORTE DE ERRORES

Si encuentras algún error, anota:

1. **Módulo:** (Login, Productos, etc.)
2. **Pasos:** (Qué hiciste)
3. **Error:** (Mensaje o comportamiento)
4. **Esperado:** (Qué debería pasar)

---

## ✅ CONCLUSIÓN

Todas las validaciones deben:
- ✅ Estar en español
- ✅ Ser claras y útiles
- ✅ Prevenir errores comunes
- ✅ Guiar al usuario correctamente

---

**Fecha de pruebas:** _________________
**Realizado por:** _________________
**Resultado:** [ ] Aprobado  [ ] Con observaciones

