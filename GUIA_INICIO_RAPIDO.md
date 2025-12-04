# 🚀 GUÍA RÁPIDA - INICIO DEL SISTEMA

## 📝 Pasos para Iniciar

### 1. Aplicar Migraciones (si es necesario)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Crear Superusuario
Ejecuta el archivo: **`CREAR_SUPERUSUARIO.bat`**

O manualmente:
```bash
python manage.py createsuperuser
```

Datos sugeridos:
- **Username**: admin
- **Email**: admin@digitsoft.com
- **Password**: Admin123! (o la que prefieras)

### 3. Iniciar Servidor
```bash
python manage.py runserver
```

### 4. Acceder al Sistema

#### Login Principal:
```
http://127.0.0.1:8000/usuarios/login/
```

#### Panel de Administración Django:
```
http://127.0.0.1:8000/admin/
```

#### Gestión de Usuarios:
```
http://127.0.0.1:8000/usuarios/gestionar/
```

---

## 👤 Primer Acceso

1. Ve a: `http://127.0.0.1:8000/usuarios/login/`
2. Ingresa las credenciales del superusuario
3. Serás redirigido al dashboard
4. Accede a "Gestión de Usuarios" desde el menú

---

## ✅ Funcionalidades Disponibles

### Como Administrador puedes:
- ✅ Ver todos los usuarios del sistema
- ✅ Crear nuevos usuarios de cualquier tipo
- ✅ Editar información de usuarios
- ✅ Bloquear/Desbloquear usuarios
- ✅ Eliminar usuarios (excepto superusuarios)
- ✅ Cambiar permisos de staff
- ✅ Ver estadísticas del sistema

### Los usuarios pueden:
- ✅ Iniciar sesión con sus credenciales
- ✅ Ver y editar su perfil
- ✅ Cambiar su contraseña
- ✅ Acceder según sus permisos

---

## 🔑 Tipos de Usuario

| Tipo | Descripción | Permisos |
|------|-------------|----------|
| **Superusuario** | Control total | Acceso completo |
| **Staff** | Personal autorizado | Gestión de usuarios |
| **Admin** | Administrador | Módulos principales |
| **Cliente** | Cliente registrado | Ver sus datos |
| **Técnico** | Personal técnico | Gestionar servicios |
| **Proveedor** | Proveedor | Gestionar productos |

---

## 🛡️ Seguridad

- ✅ Contraseñas encriptadas
- ✅ Protección CSRF
- ✅ Validación de permisos
- ✅ Sistema de bloqueo
- ✅ Sesiones seguras

---

## 📞 URLs Importantes

```
/usuarios/login/                 - Iniciar sesión
/usuarios/logout/                - Cerrar sesión
/usuarios/registro/              - Registro de clientes
/usuarios/perfil/                - Mi perfil
/usuarios/cambiar-contrasena/    - Cambiar contraseña
/usuarios/gestionar/             - Gestión de usuarios (staff)
/admin/                          - Panel Django admin
```

---

## 🎯 Prueba Rápida

1. **Crear superusuario**: `CREAR_SUPERUSUARIO.bat`
2. **Iniciar servidor**: `python manage.py runserver`
3. **Login**: http://127.0.0.1:8000/usuarios/login/
4. **Crear un usuario**: Gestión → Crear Usuario
5. **Ver estadísticas**: Dashboard con métricas

---

## ⚡ Comandos Útiles

```bash
# Ver usuarios en consola
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()

# Cambiar contraseña de usuario
python manage.py changepassword username

# Ver todos los modelos
python manage.py showmigrations
```

---

## 🐛 Solución de Problemas

### Error: "No module named usuarios"
```bash
# Verifica que estés en el directorio correcto
cd Digit_Sof_Nuevo
```

### Error: "Table doesn't exist"
```bash
# Ejecuta las migraciones
python manage.py migrate
```

### No puedo acceder al admin
```bash
# Verifica que el usuario sea superuser
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='admin')
>>> user.is_superuser = True
>>> user.is_staff = True
>>> user.save()
```

---

## ✨ ¡Listo para Usar!

El sistema está completamente configurado y listo para gestionar usuarios.

**Fecha**: 2025-12-04
**Estado**: ✅ Operativo
@echo off
echo ========================================
echo   CREAR SUPERUSUARIO - DIGT SOFT
echo ========================================
echo.
echo Este script creara un superusuario para acceder al sistema
echo.
cd /d "%~dp0"

python manage.py createsuperuser

echo.
echo ========================================
echo   SUPERUSUARIO CREADO EXITOSAMENTE
echo ========================================
echo.
echo Ahora puedes:
echo 1. Acceder al sistema: http://127.0.0.1:8000/usuarios/login/
echo 2. Acceder al admin: http://127.0.0.1:8000/admin/
echo 3. Gestionar usuarios: http://127.0.0.1:8000/usuarios/gestionar/
echo.
pause

