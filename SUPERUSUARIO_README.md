# Instrucciones para Crear Superusuarios

## ✓ Superusuario Creado

Se ha creado exitosamente un superusuario con las siguientes credenciales:

- **Usuario:** admin
- **Email:** admin@gmail.com
- **Contraseña:** admin123

Ya puedes iniciar sesión en:
- URL de login: http://127.0.0.1:8000/usuarios/login/
- Panel de administración: http://127.0.0.1:8000/admin/

## Scripts Disponibles

### 1. crear_superusuario.py (Interactivo)
Este script te permite crear un superusuario de forma interactiva, verificando si ya existen otros.

**Uso:**
```cmd
python crear_superusuario.py
```

El script te pedirá:
- Nombre de usuario
- Email (opcional)
- Contraseña
- Confirmación de contraseña

### 2. crear_superusuario_simple.py (Automático)
Este script crea un superusuario predeterminado rápidamente.

**Uso:**
```cmd
python crear_superusuario_simple.py
```

Credenciales predeterminadas:
- Usuario: admin
- Email: admin@digtsoft.com
- Contraseña: admin123

**Nota:** Puedes editar este archivo para cambiar las credenciales predeterminadas.

### 3. Comando de Django (Interactivo)
También puedes usar el comando estándar de Django:

```cmd
python manage.py createsuperuser
```

## Verificar Superusuarios Existentes

Para ver todos los superusuarios en el sistema:

```cmd
python manage.py shell -c "from django.contrib.auth.models import User; [print(f'{u.username} - {u.email}') for u in User.objects.filter(is_superuser=True)]"
```

## Cambiar Contraseña de un Usuario

Si olvidaste la contraseña:

```cmd
python manage.py changepassword admin
```

## Importante

🔒 **Seguridad:** Recuerda cambiar la contraseña predeterminada en producción y usar contraseñas seguras.

📝 **Migraciones:** Si aún no has aplicado las migraciones, ejecuta:
```cmd
python manage.py migrate
```

