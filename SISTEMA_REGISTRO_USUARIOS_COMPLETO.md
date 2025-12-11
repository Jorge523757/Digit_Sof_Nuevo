# 🎯 SISTEMA DE REGISTRO DE USUARIOS - DIGITSOFT

## 📋 RESUMEN

El sistema ya está **completamente funcional** y permite que los usuarios registrados como CLIENTES o TÉCNICOS aparezcan automáticamente en sus respectivos módulos.

---

## ✅ FUNCIONALIDAD IMPLEMENTADA

### 🔹 Registro de Clientes

Cuando un usuario se registra como **CLIENTE** a través de `/usuarios/registro/`:

1. ✅ Se crea un registro en la tabla `auth_user` (Usuario Django)
2. ✅ Se crea un perfil en `usuarios_perfil` con `tipo_usuario = 'CLIENTE'`
3. ✅ Se crea un registro en la tabla `clientes` con todos sus datos
4. ✅ Se vincula automáticamente: `perfil.cliente = cliente`

**Resultado:** El cliente aparece en:
- 👉 **Módulo de Usuarios** (`/usuarios/gestionar/`)
- 👉 **Módulo de Clientes** (`/clientes/`)

---

### 🔹 Registro de Técnicos

Cuando un usuario se registra como **TÉCNICO** a través de `/usuarios/registro/tecnico/`:

1. ✅ Se crea un registro en la tabla `auth_user` (Usuario Django)
2. ✅ Se crea un perfil en `usuarios_perfil` con `tipo_usuario = 'TECNICO'`
3. ✅ Se crea un registro en la tabla `tecnicos` con todos sus datos
4. ✅ Se vincula automáticamente: `perfil.tecnico = tecnico`

**Resultado:** El técnico aparece en:
- 👉 **Módulo de Usuarios** (`/usuarios/gestionar/`)
- 👉 **Módulo de Técnicos** (`/tecnicos/`)

---

## 🏗️ ARQUITECTURA

### Modelo de Datos

```
┌─────────────────┐
│   auth_user     │  (Tabla de Django)
│   (Usuario)     │
└────────┬────────┘
         │ OneToOne
         ▼
┌─────────────────┐
│ usuarios_perfil │
│  (PerfilUsuario)│
│                 │
│ • tipo_usuario  │  ← 'CLIENTE' o 'TECNICO'
│ • telefono      │
│ • direccion     │
│ • documento     │
│ • cliente_id    │  ← FK a Cliente (nullable)
│ • tecnico_id    │  ← FK a Tecnico (nullable)
└─────┬─────┬─────┘
      │     │
      │     └──────────────┐
      ▼                    ▼
┌────────────┐      ┌─────────────┐
│  clientes  │      │  tecnicos   │
│            │      │             │
│ • nombres  │      │ • nombres   │
│ • apellidos│      │ • apellidos │
│ • documento│      │ • documento │
│ • telefono │      │ • telefono  │
│ • correo   │      │ • correo    │
│ • direccion│      │ • profesion │
└────────────┘      └─────────────┘
```

### Relaciones

```python
# En el modelo PerfilUsuario
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, ...)  # Relación con Usuario Django
    
    cliente = models.ForeignKey(
        'clientes.Cliente',
        null=True,
        blank=True,
        related_name='usuario_perfil'
    )
    
    tecnico = models.ForeignKey(
        'tecnicos.Tecnico',
        null=True,
        blank=True,
        related_name='usuario_perfil'
    )
```

---

## 📝 CÓDIGO IMPLEMENTADO

### 1. Formulario de Registro de Cliente

**Archivo:** `usuarios/forms.py`

```python
class RegistroClienteForm(UserCreationForm):
    # ... campos del formulario ...
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

            # 1. Actualizar perfil de usuario
            perfil = user.perfil
            perfil.tipo_usuario = 'CLIENTE'
            perfil.telefono = self.cleaned_data['telefono']
            perfil.direccion = self.cleaned_data['direccion']
            perfil.documento = self.cleaned_data['documento']
            perfil.save()

            # 2. Crear registro en tabla Cliente
            cliente = Cliente.objects.create(
                nombres=self.cleaned_data['first_name'],
                apellidos=self.cleaned_data['last_name'],
                numero_documento=self.cleaned_data['documento'],
                telefono=self.cleaned_data['telefono'],
                correo=self.cleaned_data['email'],
                direccion=self.cleaned_data['direccion'],
                activo=True
            )

            # 3. Vincular cliente con perfil
            perfil.cliente = cliente
            perfil.save()

        return user
```

### 2. Formulario de Registro de Técnico

**Archivo:** `usuarios/forms.py`

```python
class RegistroTecnicoForm(UserCreationForm):
    # ... campos del formulario ...
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

            # 1. Actualizar perfil de usuario
            perfil = user.perfil
            perfil.tipo_usuario = 'TECNICO'
            perfil.telefono = self.cleaned_data['telefono']
            perfil.documento = self.cleaned_data['documento']
            perfil.save()

            # 2. Crear registro en tabla Tecnico
            tecnico = Tecnico.objects.create(
                nombres=self.cleaned_data['first_name'],
                apellidos=self.cleaned_data['last_name'],
                numero_documento=self.cleaned_data['documento'],
                telefono=self.cleaned_data['telefono'],
                correo=self.cleaned_data['email'],
                profesion=self.cleaned_data['profesion'],
                activo=True
            )

            # 3. Vincular técnico con perfil
            perfil.tecnico = tecnico
            perfil.save()

        return user
```

### 3. Vistas de Registro

**Archivo:** `usuarios/views.py`

```python
def registro_cliente(request):
    """Vista para registro de nuevos clientes"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                '¡Registro exitoso! Tu cuenta ha sido creada.'
            )
            return redirect('usuarios:login')
    else:
        form = RegistroClienteForm()

    return render(request, 'usuarios/registro.html', {'form': form})


def registro_tecnico(request):
    """Vista para registro de nuevos técnicos"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RegistroTecnicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                '¡Registro exitoso! Tu cuenta de técnico ha sido creada.'
            )
            return redirect('usuarios:login')
    else:
        form = RegistroTecnicoForm()

    return render(request, 'usuarios/registro_tecnico.html', {'form': form})
```

### 4. URLs Configuradas

**Archivo:** `usuarios/urls.py`

```python
urlpatterns = [
    # Registro
    path('registro/', views.registro_cliente, name='registro'),
    path('registro/tecnico/', views.registro_tecnico, name='registro_tecnico'),
    
    # Gestión
    path('gestionar/', views.listar_usuarios, name='listar_usuarios'),
    # ... más URLs ...
]
```

---

## 🔗 URLs DE ACCESO

### Para Usuarios Finales

| Acción | URL | Descripción |
|--------|-----|-------------|
| Registro Cliente | `/usuarios/registro/` | Formulario de registro para clientes |
| Registro Técnico | `/usuarios/registro/tecnico/` | Formulario de registro para técnicos |
| Login | `/usuarios/login/` | Inicio de sesión |

### Para Administradores

| Módulo | URL | Descripción |
|--------|-----|-------------|
| Gestión Usuarios | `/usuarios/gestionar/` | Ver todos los usuarios del sistema |
| Gestión Clientes | `/clientes/` | Ver todos los clientes |
| Gestión Técnicos | `/tecnicos/` | Ver todos los técnicos |

---

## 🎯 FLUJO DE REGISTRO

### Cliente

```
1. Usuario visita: /usuarios/registro/
   ↓
2. Completa formulario con:
   • Username
   • Email
   • Nombres
   • Apellidos
   • Teléfono
   • Dirección
   • Documento
   • Contraseña
   ↓
3. Al enviar el formulario:
   ✅ Se crea User
   ✅ Se crea PerfilUsuario (tipo='CLIENTE')
   ✅ Se crea Cliente
   ✅ Se vinculan automáticamente
   ↓
4. Usuario puede iniciar sesión
   ↓
5. Aparece en:
   • Módulo de Usuarios (/usuarios/gestionar/)
   • Módulo de Clientes (/clientes/)
```

### Técnico

```
1. Usuario visita: /usuarios/registro/tecnico/
   ↓
2. Completa formulario con:
   • Username
   • Email
   • Nombres
   • Apellidos
   • Teléfono
   • Documento
   • Profesión/Especialidad
   • Contraseña
   ↓
3. Al enviar el formulario:
   ✅ Se crea User
   ✅ Se crea PerfilUsuario (tipo='TECNICO')
   ✅ Se crea Tecnico
   ✅ Se vinculan automáticamente
   ↓
4. Usuario puede iniciar sesión
   ↓
5. Aparece en:
   • Módulo de Usuarios (/usuarios/gestionar/)
   • Módulo de Técnicos (/tecnicos/)
```

---

## 🔍 CÓMO VERIFICAR

### Opción 1: Script de Verificación

Ejecuta el script incluido:

```bash
VERIFICAR_REGISTRO_USUARIOS.bat
```

Este script muestra:
- ✅ Cantidad de perfiles de cliente
- ✅ Cantidad de registros en tabla Cliente
- ✅ Vinculaciones correctas
- ✅ Cantidad de perfiles de técnico
- ✅ Cantidad de registros en tabla Tecnico
- ✅ Vinculaciones correctas

### Opción 2: Panel de Administración

1. Accede a: `http://localhost:8000/admin/`
2. Ve a **Perfiles de Usuarios**
3. Verifica que cada perfil tenga:
   - `tipo_usuario` correcto (CLIENTE o TECNICO)
   - Relación `cliente` o `tecnico` vinculada

### Opción 3: Interfaz Web

1. **Registra un cliente:**
   - Ve a `/usuarios/registro/`
   - Completa el formulario
   - Verifica que aparezca en `/clientes/` y `/usuarios/gestionar/`

2. **Registra un técnico:**
   - Ve a `/usuarios/registro/tecnico/`
   - Completa el formulario
   - Verifica que aparezca en `/tecnicos/` y `/usuarios/gestionar/`

---

## 📊 CONSULTAS SQL ÚTILES

### Ver todos los clientes con sus usuarios

```sql
SELECT 
    u.id as user_id,
    u.username,
    u.email,
    p.tipo_usuario,
    c.id as cliente_id,
    c.nombres,
    c.apellidos,
    c.numero_documento
FROM auth_user u
INNER JOIN usuarios_perfil p ON u.id = p.user_id
LEFT JOIN clientes c ON p.cliente_id = c.id
WHERE p.tipo_usuario = 'CLIENTE';
```

### Ver todos los técnicos con sus usuarios

```sql
SELECT 
    u.id as user_id,
    u.username,
    u.email,
    p.tipo_usuario,
    t.id as tecnico_id,
    t.nombres,
    t.apellidos,
    t.numero_documento,
    t.profesion
FROM auth_user u
INNER JOIN usuarios_perfil p ON u.id = p.user_id
LEFT JOIN tecnicos t ON p.tecnico_id = t.id
WHERE p.tipo_usuario = 'TECNICO';
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Problema: "El cliente/técnico no aparece en su módulo"

**Posibles causas:**
1. El registro fue creado antes de implementar esta funcionalidad
2. El registro se creó manualmente en el admin
3. Hubo un error durante el registro

**Solución:**
1. Ve al admin Django
2. Busca el `PerfilUsuario` del usuario
3. Asigna manualmente el `cliente` o `tecnico` correspondiente
4. Guarda los cambios

### Problema: "Duplicate key error al registrarse"

**Causa:** El documento de identidad ya existe en la base de datos

**Solución:**
- Verificar que el documento no esté ya registrado
- Los formularios ya tienen validación para esto

### Problema: "El perfil no se crea automáticamente"

**Causa:** La señal `post_save` no está funcionando

**Solución:**
Verificar en `usuarios/models.py`:
```python
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
```

---

## 🎨 PERSONALIZACIÓN

### Agregar campos adicionales al registro

1. **Editar el formulario** (`usuarios/forms.py`):
```python
class RegistroClienteForm(UserCreationForm):
    campo_nuevo = forms.CharField(...)
```

2. **Actualizar el método save:**
```python
def save(self, commit=True):
    # ...
    cliente = Cliente.objects.create(
        # ...
        campo_nuevo=self.cleaned_data['campo_nuevo']
    )
```

3. **Actualizar la plantilla** (`templates/usuarios/registro.html`)

### Cambiar el tipo de usuario por defecto

En `usuarios/models.py`:
```python
tipo_usuario = models.CharField(
    max_length=10,
    choices=TIPO_USUARIO_CHOICES,
    default='CLIENTE',  # ← Cambiar aquí
    verbose_name="Tipo de Usuario"
)
```

---

## 📚 ARCHIVOS RELACIONADOS

| Archivo | Descripción |
|---------|-------------|
| `usuarios/models.py` | Modelo PerfilUsuario con relaciones |
| `usuarios/forms.py` | Formularios de registro |
| `usuarios/views.py` | Vistas de registro y gestión |
| `usuarios/urls.py` | URLs del módulo usuarios |
| `clientes/models.py` | Modelo Cliente |
| `tecnicos/models.py` | Modelo Tecnico |
| `templates/usuarios/registro.html` | Template de registro cliente |
| `templates/usuarios/registro_tecnico.html` | Template de registro técnico |

---

## ✨ CARACTERÍSTICAS ADICIONALES

### Validaciones Implementadas

- ✅ Email único (no se permite duplicados)
- ✅ Username único (no se permite duplicados)
- ✅ Documento único por tipo (cliente/técnico)
- ✅ Contraseña segura (mínimo 8 caracteres)
- ✅ Teléfono con formato válido
- ✅ Todos los campos requeridos validados

### Seguridad

- ✅ Contraseñas hasheadas con algoritmo seguro
- ✅ Validación CSRF en formularios
- ✅ Sanitización de inputs
- ✅ Prevención de SQL injection (usando ORM)
- ✅ Validación de permisos en vistas de gestión

### Experiencia de Usuario

- ✅ Mensajes de éxito/error claros
- ✅ Redirección automática después del registro
- ✅ Formularios con placeholders descriptivos
- ✅ Validación en tiempo real
- ✅ Diseño responsive

---

## 🎯 CONCLUSIÓN

El sistema está **completamente funcional** y permite:

1. ✅ Registrar usuarios como CLIENTES o TÉCNICOS
2. ✅ Crear automáticamente registros en ambas tablas (User + Cliente/Tecnico)
3. ✅ Vincular correctamente los perfiles con sus entidades
4. ✅ Mostrar los datos en sus respectivos módulos
5. ✅ Gestionar usuarios desde un panel unificado

**No se requieren cambios adicionales.** El sistema ya cumple con todos los requisitos solicitados.

---

## 📞 SOPORTE

Si encuentras algún problema:

1. Ejecuta el script de verificación: `VERIFICAR_REGISTRO_USUARIOS.bat`
2. Revisa los logs de Django
3. Verifica la base de datos directamente
4. Consulta este documento para entender el flujo

---

**Fecha de documentación:** Diciembre 2024  
**Versión del sistema:** 1.0  
**Estado:** ✅ Funcional y probado

