# 🧪 GUÍA DE PRUEBAS - REGISTRO DE USUARIOS

## ✅ PRUEBA 1: REGISTRAR UN CLIENTE

### Pasos:

1. **Abrir el navegador y acceder a la URL de registro de cliente:**
   ```
   http://localhost:8000/usuarios/registro/
   ```

2. **Completar el formulario con los siguientes datos:**
   - **Nombre de Usuario:** `cliente_prueba1`
   - **Email:** `cliente1@ejemplo.com`
   - **Nombres:** `Juan`
   - **Apellidos:** `Pérez García`
   - **Teléfono:** `5551234567`
   - **Dirección:** `Calle Principal 123, Ciudad`
   - **Documento:** `RFC123456789`
   - **Contraseña:** `Pass1234!`
   - **Confirmar Contraseña:** `Pass1234!`

3. **Hacer clic en el botón "Registrar"**

4. **Verificar el mensaje de éxito:**
   ```
   ¡Registro exitoso! Tu cuenta ha sido creada. Ahora puedes iniciar sesión.
   ```

5. **Iniciar sesión con las credenciales:**
   - Usuario: `cliente_prueba1`
   - Contraseña: `Pass1234!`

### ✅ Verificación:

1. **Ir al módulo de Clientes:**
   ```
   http://localhost:8000/clientes/
   ```
   - Debe aparecer el cliente "Juan Pérez García" con documento "RFC123456789"

2. **Ir al módulo de Usuarios:**
   ```
   http://localhost:8000/usuarios/gestionar/
   ```
   - Debe aparecer el usuario "cliente_prueba1"
   - Al hacer clic en detalles, debe mostrar:
     - Tipo de usuario: Cliente
     - Nombre completo: Juan Pérez García
     - Email: cliente1@ejemplo.com

3. **Verificar en el admin de Django:**
   ```
   http://localhost:8000/admin/usuarios/perfilusuario/
   ```
   - Buscar el perfil de "cliente_prueba1"
   - Verificar que:
     - `tipo_usuario` = CLIENTE
     - `cliente` está vinculado (no es None)

---

## ✅ PRUEBA 2: REGISTRAR UN TÉCNICO

### Pasos:

1. **Abrir el navegador y acceder a la URL de registro de técnico:**
   ```
   http://localhost:8000/usuarios/registro/tecnico/
   ```

2. **Completar el formulario con los siguientes datos:**
   - **Nombre de Usuario:** `tecnico_prueba1`
   - **Email:** `tecnico1@ejemplo.com`
   - **Nombres:** `María`
   - **Apellidos:** `González López`
   - **Teléfono:** `5559876543`
   - **Documento:** `RFC987654321`
   - **Profesión/Especialidad:** `Técnico en Reparación de Computadoras`
   - **Contraseña:** `Pass1234!`
   - **Confirmar Contraseña:** `Pass1234!`

3. **Hacer clic en el botón "Registrar"**

4. **Verificar el mensaje de éxito:**
   ```
   ¡Registro exitoso! Tu cuenta de técnico ha sido creada. Ahora puedes iniciar sesión.
   ```

5. **Iniciar sesión con las credenciales:**
   - Usuario: `tecnico_prueba1`
   - Contraseña: `Pass1234!`

### ✅ Verificación:

1. **Ir al módulo de Técnicos:**
   ```
   http://localhost:8000/tecnicos/
   ```
   - Debe aparecer el técnico "María González López" con documento "RFC987654321"
   - Profesión: "Técnico en Reparación de Computadoras"

2. **Ir al módulo de Usuarios:**
   ```
   http://localhost:8000/usuarios/gestionar/
   ```
   - Debe aparecer el usuario "tecnico_prueba1"
   - Al hacer clic en detalles, debe mostrar:
     - Tipo de usuario: Técnico
     - Nombre completo: María González López
     - Email: tecnico1@ejemplo.com

3. **Verificar en el admin de Django:**
   ```
   http://localhost:8000/admin/usuarios/perfilusuario/
   ```
   - Buscar el perfil de "tecnico_prueba1"
   - Verificar que:
     - `tipo_usuario` = TECNICO
     - `tecnico` está vinculado (no es None)

---

## ✅ PRUEBA 3: VERIFICAR DUPLICADOS

### Prueba 3.1: Intentar registrar un cliente con email duplicado

1. Ir a: `http://localhost:8000/usuarios/registro/`
2. Usar el email: `cliente1@ejemplo.com` (ya registrado)
3. **Resultado esperado:** Error de validación
   ```
   Este correo electrónico ya está registrado.
   ```

### Prueba 3.2: Intentar registrar un cliente con documento duplicado

1. Ir a: `http://localhost:8000/usuarios/registro/`
2. Usar el documento: `RFC123456789` (ya registrado)
3. **Resultado esperado:** Error de validación
   ```
   Este documento ya está registrado.
   ```

### Prueba 3.3: Intentar registrar un técnico con email duplicado

1. Ir a: `http://localhost:8000/usuarios/registro/tecnico/`
2. Usar el email: `tecnico1@ejemplo.com` (ya registrado)
3. **Resultado esperado:** Error de validación
   ```
   Este correo electrónico ya está registrado.
   ```

---

## ✅ PRUEBA 4: VERIFICAR VINCULACIÓN EN BASE DE DATOS

### Usando el admin de Django:

1. **Acceder al admin:**
   ```
   http://localhost:8000/admin/
   ```

2. **Verificar tabla Perfiles de Usuarios:**
   - Ir a: `Usuarios > Perfiles de Usuarios`
   - Ver todos los perfiles
   - Verificar que cada perfil tiene:
     - Usuario asociado
     - Tipo de usuario correcto
     - Cliente o Técnico vinculado (según corresponda)

3. **Verificar tabla Clientes:**
   - Ir a: `Clientes > Clientes`
   - Ver todos los clientes
   - Cada cliente debe tener:
     - Nombres, apellidos, documento
     - Email, teléfono, dirección
     - Estado activo

4. **Verificar tabla Técnicos:**
   - Ir a: `Técnicos > Técnicos`
   - Ver todos los técnicos
   - Cada técnico debe tener:
     - Nombres, apellidos, documento
     - Email, teléfono, profesión
     - Estado activo

---

## ✅ PRUEBA 5: VERIFICAR FILTROS Y BÚSQUEDA

### En el módulo de Clientes:

1. Ir a: `http://localhost:8000/clientes/`
2. Usar el buscador para buscar: `Juan`
3. **Resultado esperado:** Debe aparecer el cliente registrado
4. Buscar por documento: `RFC123456789`
5. **Resultado esperado:** Debe aparecer el cliente registrado

### En el módulo de Técnicos:

1. Ir a: `http://localhost:8000/tecnicos/`
2. Usar el buscador para buscar: `María`
3. **Resultado esperado:** Debe aparecer el técnico registrado
4. Buscar por profesión: `Reparación`
5. **Resultado esperado:** Debe aparecer el técnico registrado

### En el módulo de Usuarios:

1. Ir a: `http://localhost:8000/usuarios/gestionar/`
2. Filtrar por tipo: `CLIENTE`
3. **Resultado esperado:** Debe aparecer solo el cliente
4. Filtrar por tipo: `TECNICO`
5. **Resultado esperado:** Debe aparecer solo el técnico

---

## 📊 CHECKLIST DE VERIFICACIÓN

### Para Clientes:

- [ ] El formulario de registro está accesible
- [ ] Se puede registrar un nuevo cliente
- [ ] Se muestra mensaje de éxito
- [ ] Se puede iniciar sesión con las credenciales
- [ ] El cliente aparece en `/clientes/`
- [ ] El usuario aparece en `/usuarios/gestionar/`
- [ ] El perfil tiene tipo_usuario = CLIENTE
- [ ] El perfil está vinculado con la tabla Cliente
- [ ] Se pueden buscar y filtrar clientes
- [ ] No se permiten emails duplicados
- [ ] No se permiten documentos duplicados

### Para Técnicos:

- [ ] El formulario de registro está accesible
- [ ] Se puede registrar un nuevo técnico
- [ ] Se muestra mensaje de éxito
- [ ] Se puede iniciar sesión con las credenciales
- [ ] El técnico aparece en `/tecnicos/`
- [ ] El usuario aparece en `/usuarios/gestionar/`
- [ ] El perfil tiene tipo_usuario = TECNICO
- [ ] El perfil está vinculado con la tabla Tecnico
- [ ] Se pueden buscar y filtrar técnicos
- [ ] No se permiten emails duplicados
- [ ] No se permiten documentos duplicados

---

## 🔍 CONSULTAS SQL PARA VERIFICACIÓN MANUAL

### Ver todos los clientes con sus usuarios:

```sql
SELECT 
    u.username,
    u.first_name,
    u.last_name,
    u.email,
    p.tipo_usuario,
    c.nombres,
    c.apellidos,
    c.numero_documento
FROM auth_user u
INNER JOIN usuarios_perfil p ON u.id = p.user_id
LEFT JOIN clientes c ON p.cliente_id = c.id
WHERE p.tipo_usuario = 'CLIENTE';
```

### Ver todos los técnicos con sus usuarios:

```sql
SELECT 
    u.username,
    u.first_name,
    u.last_name,
    u.email,
    p.tipo_usuario,
    t.nombres,
    t.apellidos,
    t.numero_documento,
    t.profesion
FROM auth_user u
INNER JOIN usuarios_perfil p ON u.id = p.user_id
LEFT JOIN tecnicos t ON p.tecnico_id = t.id
WHERE p.tipo_usuario = 'TECNICO';
```

### Contar registros:

```sql
-- Total de perfiles de cliente
SELECT COUNT(*) FROM usuarios_perfil WHERE tipo_usuario = 'CLIENTE';

-- Total de registros en tabla clientes
SELECT COUNT(*) FROM clientes;

-- Total de perfiles de técnico
SELECT COUNT(*) FROM usuarios_perfil WHERE tipo_usuario = 'TECNICO';

-- Total de registros en tabla técnicos
SELECT COUNT(*) FROM tecnicos;
```

---

## ✨ RESULTADO ESPERADO

Después de realizar todas las pruebas:

1. ✅ Cada cliente registrado aparece en:
   - Módulo de Usuarios
   - Módulo de Clientes

2. ✅ Cada técnico registrado aparece en:
   - Módulo de Usuarios
   - Módulo de Técnicos

3. ✅ Los registros están correctamente vinculados en la base de datos

4. ✅ Las validaciones funcionan correctamente

5. ✅ Las búsquedas y filtros funcionan correctamente

---

## 🐛 SI ALGO NO FUNCIONA

1. **Verificar que el servidor esté corriendo:**
   ```
   python manage.py runserver
   ```

2. **Verificar las migraciones:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Verificar los logs de Django** en la consola donde corre el servidor

4. **Verificar la base de datos** directamente con las consultas SQL

5. **Revisar el archivo:** `SISTEMA_REGISTRO_USUARIOS_COMPLETO.md`

---

**Fecha:** Diciembre 2024  
**Estado:** ✅ Sistema funcional y listo para pruebas

