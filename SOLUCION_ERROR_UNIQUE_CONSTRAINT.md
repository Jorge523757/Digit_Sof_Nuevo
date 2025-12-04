# 🔧 SOLUCIÓN: Error de Registro - UNIQUE constraint failed

## ❌ Error Identificado

```
IntegrityError: UNIQUE constraint failed: main_userprofile.documento
```

### ¿Qué causó el error?

Tenías **dos modelos de perfil de usuario** compitiendo entre sí:

1. **`main.models.UserProfile`** (viejo) - tabla: `main_userprofile`
2. **`usuarios.models.PerfilUsuario`** (nuevo) - tabla: `usuarios_perfil`

Ambos tenían **signals** que intentaban crear un perfil automáticamente cuando se creaba un usuario. Esto causaba:
- ✅ Se creaba el usuario
- ❌ Signal 1 intentaba crear `UserProfile` → Éxito
- ❌ Signal 2 intentaba crear `PerfilUsuario` → ERROR (documento duplicado)

---

## ✅ Solución Aplicada

### 1. **Deshabilitado el signal duplicado**

**Archivo:** `main/models.py` (líneas 63-76)

**ANTES:**
```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # ← Causaba conflicto
```

**AHORA:**
```python
# SIGNALS DESHABILITADOS - Se usa el signal de usuarios/models.py
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
```

### 2. **Signal correcto activo**

**Archivo:** `usuarios/models.py` (líneas 92-104)

```python
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crea automáticamente un perfil cuando se crea un usuario"""
    if created:
        PerfilUsuario.objects.create(user=instance)  # ← Este es el correcto
```

### 3. **Script de limpieza creado**

**Archivo:** `usuarios/management/commands/limpiar_perfiles.py`

Este script:
- ✅ Elimina perfiles duplicados
- ✅ Migra datos de `UserProfile` a `PerfilUsuario`
- ✅ Asegura que cada usuario tenga un solo perfil

---

## 🚀 Cómo Corregir el Error

### Opción 1: Script Automático (Recomendado)
```bash
CORREGIR_ERROR_REGISTRO.bat
```

Este script:
1. Limpia perfiles duplicados
2. Reinicia el servidor
3. Todo listo para registrarse ✅

### Opción 2: Manual
```bash
# 1. Limpiar perfiles
python manage.py limpiar_perfiles

# 2. Reiniciar servidor
python manage.py runserver
```

---

## 🧪 Probar el Registro

Después de ejecutar el script:

1. Ve a: `http://127.0.0.1:8000/usuarios/registro/`
2. Completa el formulario
3. Click en "Registrarse"
4. **✅ Debería funcionar sin errores**

---

## 📊 ¿Qué hace el comando limpiar_perfiles?

```python
# Ejecuta: python manage.py limpiar_perfiles

Resultado:
✅ Eliminados X UserProfile duplicados
✅ Migrados X perfiles antiguos
✅ Creados X perfiles nuevos faltantes
✅ Total usuarios: X
```

---

## 🔍 Verificación de la Solución

### Antes de ejecutar:
```bash
# Usuarios con perfiles duplicados
```

### Después de ejecutar:
```bash
# Cada usuario tiene solo PerfilUsuario
# Sin UserProfile duplicados
# Registro funciona correctamente ✅
```

---

## 📝 Notas Técnicas

### Modelos Actuales:

**1. User (Django)**
- Tabla: `auth_user`
- Campos: username, email, password, etc.

**2. PerfilUsuario (Activo)**
- Tabla: `usuarios_perfil`
- Relación: OneToOne con User
- Campos: tipo_usuario, telefono, documento, cliente, etc.

**3. UserProfile (Obsoleto - Deshabilitado)**
- Tabla: `main_userprofile`
- Estado: Signals deshabilitados
- Acción: Se migrará/eliminará

---

## ⚠️ Si el Error Persiste

### Opción 1: Limpiar base de datos manualmente
```bash
# En la consola de Django
python manage.py shell

from main.models import UserProfile
UserProfile.objects.all().delete()
```

### Opción 2: Resetear migraciones (¡CUIDADO!)
```bash
# Solo en desarrollo, NUNCA en producción
python manage.py migrate usuarios zero
python manage.py migrate usuarios
```

### Opción 3: Eliminar tabla vieja
```sql
-- En SQLite
DROP TABLE IF EXISTS main_userprofile;
```

---

## 🎯 Prevención Futura

Para evitar este error en el futuro:

1. **Un solo modelo de perfil** - Usar solo `PerfilUsuario`
2. **Un solo signal** - Solo en `usuarios/models.py`
3. **Validación de unicidad** - En formularios, no solo en DB

---

## ✅ Estado Actual

| Componente | Estado |
|------------|--------|
| Signal de UserProfile | ❌ Deshabilitado |
| Signal de PerfilUsuario | ✅ Activo |
| Comando de limpieza | ✅ Creado |
| Script de corrección | ✅ Creado |

---

## 📁 Archivos Modificados

1. ✅ `main/models.py` - Signals deshabilitados
2. ✅ `usuarios/management/commands/limpiar_perfiles.py` - Comando nuevo
3. ✅ `CORREGIR_ERROR_REGISTRO.bat` - Script de corrección

---

## 🎉 Resultado Final

Después de ejecutar `CORREGIR_ERROR_REGISTRO.bat`:

```
✅ Registro funciona correctamente
✅ Un solo perfil por usuario
✅ No más errores de UNIQUE constraint
✅ Clientes se registran y aparecen en gestión
✅ Sistema estable y funcional
```

---

## 💡 Explicación Simple

**Problema:**
```
Intentabas crear 2 perfiles para un usuario
→ Primer perfil ✅
→ Segundo perfil ❌ (documento duplicado)
```

**Solución:**
```
Ahora solo se crea 1 perfil (PerfilUsuario)
→ Perfil único ✅
→ Sin duplicados ✅
→ Registro funciona ✅
```

---

**Fecha de corrección:** 2025-12-04  
**Estado:** ✅ Solucionado  
**Comando:** `python manage.py limpiar_perfiles`  
**Script:** `CORREGIR_ERROR_REGISTRO.bat`

🚀 **¡Tu sistema está corregido y listo para usar!**

