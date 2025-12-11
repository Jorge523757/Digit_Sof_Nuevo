# 🧪 GUÍA DE PRUEBAS - SISTEMA DE LOGIN COMPLETO

## 🚀 INICIO RÁPIDO

### **Ejecutar el servidor:**
```powershell
# Opción 1: Usar el script
.\PROBAR_LOGIN_COMPLETO.bat

# Opción 2: Manual
python manage.py runserver
```

---

## ✅ PRUEBAS A REALIZAR

### **1. PROBAR LOGIN** 🔐

#### **Caso 1: Login Exitoso**
```
URL: http://127.0.0.1:8000/usuarios/login/

1. Ingresar username existente (ej: admin)
2. Ingresar contraseña correcta
3. Click en "Iniciar Sesión"

✅ RESULTADO ESPERADO:
- Redirecciona al dashboard
- Muestra mensaje: "¡Bienvenido, [nombre]!"
```

#### **Caso 2: Credenciales Incorrectas**
```
1. Ingresar username cualquiera
2. Ingresar contraseña incorrecta
3. Click en "Iniciar Sesión"

✅ RESULTADO ESPERADO:
- Permanece en login
- Muestra mensaje: "Usuario o contraseña incorrectos"
- El formulario se mantiene
```

#### **Caso 3: Campos Vacíos**
```
1. Dejar campos vacíos
2. Click en "Iniciar Sesión"

✅ RESULTADO ESPERADO:
- Validación HTML5 impide envío
- Muestra "Por favor, rellena este campo"
```

---

### **2. PROBAR REGISTRO** 📝

#### **Caso 1: Registro Exitoso**
```
URL: http://127.0.0.1:8000/usuarios/registro/

Datos de prueba:
- Nombres: Juan Carlos
- Apellidos: Pérez García
- Username: juanperez2024
- Email: juan.perez@ejemplo.com
- Documento: RFC123456789
- Teléfono: 5512345678
- Dirección: Calle Ejemplo 123, Col. Centro, CDMX
- Contraseña: MiPass123456
- Confirmar: MiPass123456

✅ RESULTADO ESPERADO:
- Redirecciona al login
- Muestra mensaje: "¡Registro exitoso! Tu cuenta ha sido creada"
- Se crea usuario en tabla User
- Se crea perfil en PerfilUsuario
- Se crea registro en Cliente
```

#### **Caso 2: Username Duplicado**
```
1. Usar un username que ya existe (ej: admin)
2. Llenar los demás campos
3. Click en "Registrarme"

✅ RESULTADO ESPERADO:
- Permanece en registro
- Muestra error en campo username
- Mensaje: "Este nombre de usuario ya está en uso"
```

#### **Caso 3: Email Duplicado**
```
1. Usar un email que ya existe
2. Llenar los demás campos
3. Click en "Registrarme"

✅ RESULTADO ESPERADO:
- Permanece en registro
- Muestra error en campo email
- Mensaje: "Este correo electrónico ya está registrado"
```

#### **Caso 4: Contraseñas No Coinciden**
```
1. Llenar todos los campos
2. Contraseña: MiPass123456
3. Confirmar: OtraPass789
4. Click en "Registrarme"

✅ RESULTADO ESPERADO:
- Permanece en registro
- Muestra error en confirmación
- Mensaje: "Las contraseñas no coinciden"
```

#### **Caso 5: Username Muy Corto**
```
1. Username: abc (3 caracteres)
2. Llenar demás campos
3. Click en "Registrarme"

✅ RESULTADO ESPERADO:
- Muestra error en username
- Mensaje: "El nombre de usuario debe tener al menos 4 caracteres"
```

#### **Caso 6: Contraseña Débil**
```
1. Contraseña: 12345 (solo 5 caracteres)
2. Llenar demás campos
3. Click en "Registrarme"

✅ RESULTADO ESPERADO:
- Muestra error en contraseña
- Mensaje: "La contraseña debe tener al menos 8 caracteres"
```

---

### **3. PROBAR RECUPERACIÓN DE CONTRASEÑA** 🔑

#### **Paso 1: Solicitar Recuperación**

**Caso 1: Email Existente**
```
URL: http://127.0.0.1:8000/usuarios/recuperar-password/

1. Ingresar email de usuario existente
2. Click en "Enviar Enlace de Recuperación"

✅ RESULTADO ESPERADO:
- Redirecciona al login
- Muestra mensaje de éxito
- En la consola del servidor aparece:
  =====================
  EMAIL DE RECUPERACIÓN
  =====================
  Para: email@ejemplo.com
  URL: http://127.0.0.1:8000/usuarios/reset-password/[UUID]/
  =====================
```

**Caso 2: Email No Existente**
```
1. Ingresar email que no existe
2. Click en "Enviar Enlace de Recuperación"

✅ RESULTADO ESPERADO:
- Permanece en la página
- Muestra error: "No existe ninguna cuenta con este correo electrónico"
```

#### **Paso 2: Establecer Nueva Contraseña**

**Caso 1: Token Válido**
```
1. Copiar la URL del token de la consola
2. Pegarla en el navegador
3. Se muestra página de reset con:
   - Avatar con inicial del usuario
   - Nombre completo
   - Email
   - Requisitos de contraseña

4. Ingresar nueva contraseña: NuevaPass12345
5. Confirmar: NuevaPass12345
6. Click en "Cambiar Contraseña"

✅ RESULTADO ESPERADO:
- Indicadores de requisitos se vuelven verdes ✓
- Redirecciona al login
- Mensaje: "Tu contraseña ha sido cambiada exitosamente"
- Puede iniciar sesión con la nueva contraseña
```

**Caso 2: Contraseñas No Coinciden**
```
1. Abrir URL con token válido
2. Nueva contraseña: Pass123456
3. Confirmar: Pass654321
4. Click en "Cambiar Contraseña"

✅ RESULTADO ESPERADO:
- Muestra error: "Las contraseñas no coinciden"
- Permanece en la página
- Puede corregir e intentar de nuevo
```

**Caso 3: Token Expirado**
```
1. Usar un token de hace más de 24 horas
2. Intentar abrir la URL

✅ RESULTADO ESPERADO:
- Redirecciona a recuperar-password
- Mensaje: "Este enlace ha expirado. Por favor solicita uno nuevo"
```

**Caso 4: Token Ya Usado**
```
1. Usar un token que ya se utilizó
2. Intentar abrir la URL

✅ RESULTADO ESPERADO:
- Redirecciona a recuperar-password
- Mensaje: "Este enlace ya fue usado. Por favor solicita uno nuevo"
```

---

## 🎨 PRUEBAS DE DISEÑO

### **Verificar en todas las páginas:**

1. **Responsive:**
   - Abrir en ventana completa ✓
   - Redimensionar a móvil ✓
   - Verificar que todo se vea bien ✓

2. **Animaciones:**
   - Página debe aparecer con animación suave ✓
   - Botones deben tener hover effect ✓
   - Campos deben resaltar al hacer focus ✓

3. **Iconos:**
   - Todos los iconos deben verse ✓
   - Los iconos de "ojo" para mostrar/ocultar contraseña funcionan ✓

4. **Colores:**
   - Fondo con gradiente morado ✓
   - Tarjeta blanca centrada ✓
   - Botones con gradiente ✓
   - Enlaces en color violeta ✓

---

## 🔍 VERIFICACIONES EN BASE DE DATOS

### **Después de registrar un usuario, verificar:**

```sql
-- En la tabla auth_user
SELECT id, username, email, first_name, last_name, is_active 
FROM auth_user 
WHERE username = 'juanperez2024';

-- En la tabla usuarios_perfil
SELECT id, user_id, tipo_usuario, telefono, documento 
FROM usuarios_perfil 
WHERE user_id = [ID_USUARIO];

-- En la tabla clientes_cliente
SELECT id, nombres, apellidos, correo, telefono, numero_documento 
FROM clientes_cliente 
WHERE correo = 'juan.perez@ejemplo.com';
```

✅ **RESULTADO ESPERADO:**
- Registro en auth_user existe
- Registro en usuarios_perfil existe y está vinculado
- Registro en clientes_cliente existe
- tipo_usuario = 'CLIENTE'
- Todos los datos coinciden

---

## 📊 CHECKLIST FINAL

### **Login:**
- [ ] Login con credenciales correctas funciona
- [ ] Login con credenciales incorrectas muestra error
- [ ] Login con campos vacíos no se envía
- [ ] Usuario bloqueado no puede entrar
- [ ] Redirección después de login funciona
- [ ] Botón "mostrar contraseña" funciona
- [ ] Link "¿Olvidaste tu contraseña?" lleva a recuperación
- [ ] Link "Regístrate aquí" lleva a registro

### **Registro:**
- [ ] Registro con datos correctos funciona
- [ ] Se crea usuario en tabla User
- [ ] Se crea perfil en PerfilUsuario
- [ ] Se crea registro en Cliente
- [ ] Username duplicado muestra error
- [ ] Email duplicado muestra error
- [ ] Documento duplicado muestra error
- [ ] Contraseñas no coinciden muestra error
- [ ] Validaciones de longitud funcionan
- [ ] Botones "mostrar contraseña" funcionan
- [ ] Link "Inicia Sesión" lleva a login
- [ ] Puede iniciar sesión después de registrarse

### **Recuperación:**
- [ ] Formulario de solicitud funciona
- [ ] Email existente genera token
- [ ] Email no existente muestra error
- [ ] Token se genera correctamente en BD
- [ ] URL del token se muestra en consola
- [ ] Link del token abre página de reset
- [ ] Muestra información del usuario
- [ ] Formulario de nueva contraseña funciona
- [ ] Indicadores de requisitos funcionan en tiempo real
- [ ] Contraseña se cambia correctamente
- [ ] Token se marca como usado
- [ ] Token usado no se puede reutilizar
- [ ] Token expirado muestra error
- [ ] Puede iniciar sesión con nueva contraseña

---

## 🎯 RESULTADO ESPERADO FINAL

✅ **TODO FUNCIONA CORRECTAMENTE:**
- ✅ Sistema de login completo
- ✅ Sistema de registro con validaciones
- ✅ Sistema de recuperación de contraseña
- ✅ Todas las validaciones operando
- ✅ Diseño moderno y responsive
- ✅ Base de datos actualizada correctamente
- ✅ Mensajes de error claros
- ✅ Experiencia de usuario fluida

**¡El sistema está 100% funcional!** 🎉

