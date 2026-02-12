# 📧 CONFIGURAR ENVÍO REAL DE CORREOS - GUÍA RÁPIDA

## ⚠️ PROBLEMA ACTUAL

Los correos de recuperación se están mostrando en la **consola del servidor** pero **NO se envían** al correo del usuario porque:

```
EMAIL_HOST_PASSWORD=AQUI_TU_CONTRASEÑA_DE_APLICACION
```

Falta configurar la **contraseña de aplicación de Gmail**.

---

## ✅ SOLUCIÓN EN 3 PASOS

### PASO 1: Activar Verificación en 2 Pasos en Gmail

1. **Abre:** https://myaccount.google.com/security
2. **Busca:** "Verificación en dos pasos"
3. **Actívala** si no está activada
4. **Sigue** las instrucciones para configurarla

---

### PASO 2: Generar Contraseña de Aplicación

1. **Abre:** https://myaccount.google.com/apppasswords
2. **Selecciona:**
   - Aplicación: "Correo"
   - Dispositivo: "Computadora Windows"
3. **Haz clic en:** "Generar"
4. **Copia** la contraseña de 16 caracteres que aparece
   - Ejemplo: `abcd efgh ijkl mnop`
   - Puedes quitar los espacios: `abcdefghijklmnop`

---

### PASO 3: Configurar el Archivo `.env`

1. **Abre el archivo:** `C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo\.env`

2. **Busca la línea:**
   ```env
   EMAIL_HOST_PASSWORD=AQUI_TU_CONTRASEÑA_DE_APLICACION
   ```

3. **Reemplázala con tu contraseña de aplicación:**
   ```env
   EMAIL_HOST_PASSWORD=abcdefghijklmnop
   ```

4. **Guarda el archivo**

5. **Reinicia el servidor Django:**
   - Presiona `CTRL+C` en la terminal
   - Ejecuta: `python manage.py runserver`

---

## 🚀 MÉTODO AUTOMÁTICO (RECOMENDADO)

Si prefieres configurarlo automáticamente:

1. **Haz doble clic en:**
   ```
   CONFIGURAR_EMAIL_GMAIL.bat
   ```

2. **Sigue las instrucciones:**
   - Te abrirá la página de contraseñas de aplicación
   - Generarás la contraseña
   - La pegarás en el script
   - Se configurará automáticamente

---

## 🧪 PROBAR QUE FUNCIONA

### Prueba 1: Desde la Web

1. **Abre:** http://127.0.0.1:8000/usuarios/login/
2. **Haz clic en:** "¿Olvidaste tu contraseña?"
3. **Ingresa:** davidcristancho160@gmail.com
4. **Haz clic en:** "Enviar Código"
5. **Revisa tu email:** Debería llegar en menos de 1 minuto

### Prueba 2: Desde la Consola de Django

```bash
python manage.py shell
```

```python
from usuarios.services_password import ServicioRecuperacionPassword
from django.contrib.auth.models import User

# Obtener usuario
usuario = User.objects.filter(email='davidcristancho160@gmail.com').first()

# Solicitar recuperación
exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(
    'davidcristancho160@gmail.com',
    '127.0.0.1'
)

print(f"Éxito: {exito}")
print(f"Mensaje: {mensaje}")
if token:
    print(f"Código: {token.codigo}")
```

**Si funciona correctamente:**
- ✅ `Éxito: True`
- ✅ Recibirás un email con el código
- ✅ El código será de 6 dígitos

---

## 📋 ARCHIVO .env COMPLETO

Tu archivo `.env` debería verse así:

```env
# CONFIGURACIÓN DE EMAIL - DIGIT SOFT
# Configurado automáticamente

# Backend de email (SMTP real)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Configuración SMTP de Gmail
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Credenciales de Gmail
EMAIL_HOST_USER=davidcristancho160@gmail.com
EMAIL_HOST_PASSWORD=abcdefghijklmnop  # <-- CAMBIA ESTO

# Email remitente
DEFAULT_FROM_EMAIL=DIGIT SOFT <davidcristancho160@gmail.com>

# Email del administrador
ADMIN_EMAIL=davidcristancho160@gmail.com

# URL del sitio
SITE_URL=http://localhost:8000

# Otras configuraciones
DEBUG=True
SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
```

---

## 🔍 VERIFICAR CONFIGURACIÓN ACTUAL

### Ver qué backend está usando:

```bash
python manage.py shell
```

```python
from django.conf import settings

print(f"Backend: {settings.EMAIL_BACKEND}")
print(f"Host: {settings.EMAIL_HOST}")
print(f"Usuario: {settings.EMAIL_HOST_USER}")
print(f"Password configurado: {'Sí' if settings.EMAIL_HOST_PASSWORD else 'No'}")
```

**Si muestra:**
```
Backend: django.core.mail.backends.console.EmailBackend
```

Significa que está usando el backend de consola (no envía emails reales).

**Debería mostrar:**
```
Backend: django.core.mail.backends.smtp.EmailBackend
Host: smtp.gmail.com
Usuario: davidcristancho160@gmail.com
Password configurado: Sí
```

---

## ⚠️ PROBLEMAS COMUNES

### 1. "SMTPAuthenticationError"
**Causa:** Contraseña incorrecta o verificación en 2 pasos no activada
**Solución:** 
- Verifica que la verificación en 2 pasos esté activa
- Genera una nueva contraseña de aplicación
- Asegúrate de copiarla sin espacios

### 2. "SMTPServerDisconnected"
**Causa:** Problema de conexión
**Solución:**
- Verifica tu conexión a internet
- Asegúrate de que `EMAIL_PORT=587` y `EMAIL_USE_TLS=True`

### 3. Los emails van a spam
**Causa:** Normal para correos nuevos
**Solución:**
- Marca el correo como "No es spam"
- Con el tiempo Gmail aprenderá

### 4. Backend sigue siendo "console"
**Causa:** El archivo `.env` no se está leyendo
**Solución:**
- Verifica que el archivo se llame exactamente `.env` (sin extensión)
- Reinicia el servidor Django
- Verifica que `python-decouple` esté instalado:
  ```bash
  pip install python-decouple
  ```

---

## 📧 FORMATO DEL EMAIL QUE LLEGARÁ

El usuario recibirá un email así:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                                              
     🔐 RECUPERACIÓN DE CONTRASEÑA - DIGIT SOFT                
                                                              
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hola CristanchoG,

Has solicitado recuperar tu contraseña en DIGIT SOFT.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 TU CÓDIGO DE VERIFICACIÓN:

            513155

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ IMPORTANTE: Este código es válido por 30 minutos.

Ingresa este código en la página de recuperación para continuar.

Si no solicitaste este cambio, ignora este mensaje.

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
```

---

## 🎯 CONFIGURACIÓN PARA 100+ USUARIOS

Si necesitas enviar correos a más de 100 usuarios:

### Opción 1: Gmail (Límite: ~500 emails/día)
- ✅ Gratis
- ✅ Fácil configuración
- ⚠️ Limitado para alta demanda

### Opción 2: SendGrid (Recomendado para producción)
- ✅ 100 emails/día gratis
- ✅ Escalable a miles de emails
- ✅ Mejor deliverability

**Para configurar SendGrid:**

1. **Regístrate:** https://sendgrid.com/
2. **Genera API Key**
3. **Instala:**
   ```bash
   pip install sendgrid
   ```
4. **Configura en `.env`:**
   ```env
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.sendgrid.net
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=apikey
   EMAIL_HOST_PASSWORD=tu_api_key_de_sendgrid
   ```

### Opción 3: Amazon SES (Para producción grande)
- Extremadamente escalable
- Muy barato (€0.10 por 1000 emails)
- Requiere más configuración

---

## ✅ CHECKLIST FINAL

Antes de considerar que está funcionando:

- [ ] Verificación en 2 pasos activada en Gmail
- [ ] Contraseña de aplicación generada
- [ ] Archivo `.env` actualizado con la contraseña
- [ ] Servidor Django reiniciado
- [ ] Email de prueba enviado correctamente
- [ ] Email recibido en la bandeja de entrada
- [ ] Código de 6 dígitos visible en el email
- [ ] Código funciona para cambiar contraseña

---

## 🚀 RESUMEN

**Estado Actual:**
- ❌ Los emails se muestran en consola
- ❌ NO se envían al correo real

**Después de configurar:**
- ✅ Los emails se envían al correo real
- ✅ Llegan en menos de 1 minuto
- ✅ Funciona para todos los usuarios registrados
- ✅ Escalable a 100+ usuarios

**Tiempo de configuración:** 5-10 minutos

**¡Listo para producción!** 🎉

