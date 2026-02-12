# ⚡ INICIO RÁPIDO - DIGIT SOFT

## 🚀 Ejecuta Esto Primero

```batch
CONFIGURAR_SISTEMA_COMPLETO.bat
```

Luego:

```bash
python manage.py runserver
```

Visita: http://127.0.0.1:8000/usuarios/login/

---

## ✅ ¿Qué hay nuevo?

### 🤖 reCAPTCHA - "No soy un robot"
- Activo en login
- Activo en recuperación de contraseña
- Usa claves de prueba (funcionan en localhost)

### 🔐 Recuperación de Contraseña Mejorada
**3 Pasos Simples:**
1. **Ingresa tu email** + reCAPTCHA → Recibes código de 6 dígitos
2. **Código de verificación** → Expira en 30 minutos
3. **Nueva contraseña** → Validaciones de seguridad

### 🔵 Google OAuth Corregido
- Error `MultipleObjectsReturned` solucionado
- Login con Google funciona perfectamente
- Email: davidcristancho160@gmail.com

---

## 📧 Sobre los Emails

### MODO DESARROLLO (Actual)
Los emails **NO se envían**, aparecen en la **consola del servidor**.

**Para ver códigos de recuperación:**
1. Mira la terminal donde corre `python manage.py runserver`
2. Busca: `Código de recuperación: 123456`
3. Usa ese código en el Paso 2

### MODO PRODUCCIÓN
Edita `config/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-app-password'
```

---

## 🧪 Prueba Todo

### 1. Login Normal
- Usuario + contraseña + "No soy un robot"

### 2. Recuperar Contraseña
- http://127.0.0.1:8000/usuarios/recuperar/
- Email + reCAPTCHA
- **Mira la consola para ver el código**

### 3. Login con Google
- Botón "Continuar con Google"
- Email: davidcristancho160@gmail.com

---

## ❌ ¿Problemas?

### Google OAuth no funciona
```bash
python LIMPIAR_GOOGLE_OAUTH.py
```

### No veo el reCAPTCHA
```bash
pip install django-recaptcha
```
Luego reinicia el servidor.

### No aparece el código
**Está en la consola del servidor**, no en tu email (modo desarrollo).

---

## 📖 Documentación Completa

Lee: `INSTRUCCIONES_SISTEMA_COMPLETO.md`

---

## ✅ Checklist Rápido

- [ ] Ejecutar `CONFIGURAR_SISTEMA_COMPLETO.bat`
- [ ] Servidor corre: `python manage.py runserver`
- [ ] Login funciona con reCAPTCHA
- [ ] Google OAuth funciona
- [ ] Recuperación funciona (código en consola)

---

**🎉 ¡Todo listo! Ahora tienes un sistema completo y profesional.**

