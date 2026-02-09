# ✅ LOGIN CON GOOGLE CONFIGURADO

## 🎉 Sistema Completamente Instalado

He integrado **django-allauth** en tu proyecto DIGIT SOFT para que el botón de Google funcione correctamente.

---

## ✅ Lo Que Hice

### 1. Instalé django-allauth
```bash
pip install django-allauth
pip install PyJWT cryptography
```

### 2. Configuré settings.py
- ✅ Agregué apps de allauth
- ✅ Agregué middleware requerido
- ✅ Configuré authentication backends
- ✅ Configuré redirecciones
- ✅ Agregué configuración de Google OAuth

### 3. Actualicé URLs
- ✅ Agregué `path('accounts/', include('allauth.urls'))`

### 4. Actualicé login.html
- ✅ Cambié el botón a un enlace real
- ✅ Eliminé JavaScript innecesario
- ✅ Ahora funciona con allauth

### 5. Ejecuté Migraciones
- ✅ `python manage.py migrate`
- ✅ Tablas de allauth creadas

---

## 🔧 SIGUIENTE PASO: Configurar Google OAuth

### Paso 1: Ir a Google Cloud Console

1. Ve a: https://console.cloud.google.com/
2. Inicia sesión con tu cuenta de Google

### Paso 2: Crear Proyecto

1. Haz clic en "Seleccionar proyecto" (arriba)
2. Clic en "Nuevo proyecto"
3. Nombre: "DIGIT SOFT Login"
4. Clic en "Crear"

### Paso 3: Habilitar APIs

1. En el menú (☰), ve a "APIs y servicios" > "Biblioteca"
2. Busca "Google+ API"
3. Haz clic en "Habilitar"

### Paso 4: Crear Credenciales OAuth 2.0

1. Ve a "APIs y servicios" > "Credenciales"
2. Haz clic en "Crear credenciales"
3. Selecciona "ID de cliente de OAuth"
4. **Tipo de aplicación:** Aplicación web
5. **Nombre:** "DIGIT SOFT Web Client"

6. **URIs de redirección autorizados** (IMPORTANTE):
   ```
   http://localhost:8000/accounts/google/login/callback/
   http://127.0.0.1:8000/accounts/google/login/callback/
   ```

7. Haz clic en "Crear"

### Paso 5: Copiar Credenciales

Aparecerá una ventana con:
- **Client ID** (algo como: `123456789-abcdefg.apps.googleusercontent.com`)
- **Client Secret** (algo como: `GOCSPX-xyz123abc`)

**¡Copia ambos valores!**

### Paso 6: Configurar en Django

Abre `config/settings.py` y busca (línea ~190):

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': 'TU_CLIENT_ID_DE_GOOGLE_AQUI',  # ← PEGAR AQUÍ
            'secret': 'TU_CLIENT_SECRET_DE_GOOGLE_AQUI',  # ← PEGAR AQUÍ
            'key': ''
        }
    }
}
```

**Reemplaza:**
- `'client_id':` con tu Client ID
- `'secret':` con tu Client Secret

**Ejemplo:**
```python
'client_id': '123456789-abcdefg.apps.googleusercontent.com',
'secret': 'GOCSPX-xyz123abc',
```

### Paso 7: Crear Site en Django Admin

1. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

2. Ve a: `http://localhost:8000/admin/`

3. Inicia sesión con tu superusuario

4. Ve a **Sites** (en DJANGO.CONTRIB.SITES)

5. Haz clic en el site existente (example.com)

6. Cambia:
   - **Domain name:** `localhost:8000`
   - **Display name:** `DIGIT SOFT`

7. Guarda

### Paso 8: Agregar Aplicación Social en Admin

1. En el admin, ve a **Social applications** (en DJANGO-ALLAUTH)

2. Haz clic en "Agregar Social application"

3. Llena:
   - **Provider:** Google
   - **Name:** Google OAuth
   - **Client id:** (pega tu Client ID)
   - **Secret key:** (pega tu Client Secret)
   - **Sites:** Selecciona "localhost:8000" (el que acabas de crear)

4. Guarda

---

## 🚀 Probar el Login con Google

### 1. Inicia el servidor:
```bash
python manage.py runserver
```

### 2. Ve al login:
```
http://localhost:8000/usuarios/login/
```

### 3. Haz clic en "Continuar con Google"

### 4. Debería:
- Redirigir a Google
- Pedir que elijas cuenta
- Pedir permisos
- Redirigir de vuelta al dashboard

---

## 📊 Flujo Completo

```
Usuario clic "Continuar con Google"
    ↓
Redirige a: /accounts/google/login/
    ↓
Django-allauth redirige a Google
    ↓
Google muestra pantalla de login
    ↓
Usuario elige cuenta y acepta permisos
    ↓
Google redirige a: /accounts/google/login/callback/
    ↓
Django-allauth procesa la respuesta
    ↓
Crea o actualiza usuario en la base de datos
    ↓
Inicia sesión automáticamente
    ↓
Redirige a: /dashboard/ ✅
```

---

## 🎯 URLs Importantes

| URL | Descripción |
|-----|-------------|
| `/usuarios/login/` | Página de login con botón Google |
| `/accounts/google/login/` | Inicia flujo OAuth (allauth) |
| `/accounts/google/login/callback/` | Callback de Google |
| `/dashboard/` | Redirige aquí después del login |

---

## 📝 Archivos Modificados

```
✅ config/settings.py
   - Agregado allauth apps
   - Configurado OAuth

✅ config/urls.py
   - Agregado path('accounts/', ...)

✅ templates/usuarios/login.html
   - Botón ahora funciona con allauth

✅ Base de datos
   - Migraciones aplicadas
```

---

## 🔒 Seguridad

### Para Producción:

1. Cambia las URIs de redirección a tu dominio:
   ```
   https://tudominio.com/accounts/google/login/callback/
   ```

2. Actualiza el Site en admin:
   ```
   Domain: tudominio.com
   ```

3. Usa HTTPS (SSL)

4. Cambia `DEBUG = False` en settings.py

---

## 🐛 Solución de Problemas

### "redirect_uri_mismatch"
- Verifica que las URIs en Google Cloud coincidan exactamente
- Debe incluir `http://` y `/` al final

### "403 Forbidden" o "access_denied"
- Verifica que creaste la Social Application en admin
- Verifica que el Site está configurado correctamente

### No redirige al dashboard
- Verifica `LOGIN_REDIRECT_URL = '/dashboard/'` en settings.py
- Verifica que `/dashboard/` existe y funciona

### Error "Site matching query does not exist"
- Ejecuta: `python manage.py migrate`
- Crea un Site en admin con domain `localhost:8000`

---

## ✅ Checklist Final

- [ ] Crear proyecto en Google Cloud Console
- [ ] Habilitar Google+ API
- [ ] Crear credenciales OAuth 2.0
- [ ] Configurar URIs de redirección
- [ ] Copiar Client ID y Secret
- [ ] Pegar en settings.py
- [ ] Crear Site en Django admin
- [ ] Crear Social Application en admin
- [ ] Probar login con Google

---

## 🎉 Resultado Final

Después de configurar todo:

1. Usuario ve botón "Continuar con Google"
2. Hace clic
3. Google pide login/permisos
4. Usuario acepta
5. **Entra automáticamente al dashboard** ✅

**Sin necesidad de:**
- Crear cuenta manual
- Recordar contraseña
- Verificar email

---

**Fecha:** 05/02/2026  
**Estado:** ✅ Configurado y listo  
**Pendiente:** Configurar credenciales de Google  
**Documentación:** https://docs.allauth.org/en/latest/

**¡El código está listo! Solo faltan las credenciales de Google.** 🚀

