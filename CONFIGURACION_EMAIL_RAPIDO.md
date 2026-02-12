# 📧 CONFIGURACIÓN DE EMAIL PARA RECUPERACIÓN RÁPIDA DE CONTRASEÑA

## ✅ PROBLEMA RESUELTO

Se ha optimizado el sistema de recuperación de contraseña para que los correos lleguen **más rápido** al usuario.

## 🚀 MEJORAS IMPLEMENTADAS

### 1. **Backend SMTP Real Configurado**
- Se cambió de `console.EmailBackend` (solo muestra en consola) a `smtp.EmailBackend` (envío real)
- Configuración optimizada para Gmail con timeout reducido (10 segundos)
- Soporte para variables de entorno para mayor seguridad

### 2. **Email con Formato HTML Mejorado**
- Emails con diseño profesional usando HTML
- Mejor visualización en clientes de correo
- Botón destacado para resetear contraseña
- Compatible con clientes que no soportan HTML (fallback a texto plano)

### 3. **Optimizaciones de Velocidad**
- Timeout reducido de 30s a 10s para conexión más rápida
- Uso de TLS en puerto 587 (más rápido que SSL en 465)
- Envío asíncrono preparado (opcional)

### 4. **Mejor Manejo de Errores**
- Mensajes detallados en caso de fallo
- Logs en consola para debugging
- Fallback a link directo en modo desarrollo

## 📝 CÓMO CONFIGURAR

### Opción 1: Usar el Script Automático (RECOMENDADO)

1. **Ejecuta el archivo batch:**
   ```
   CONFIGURAR_EMAIL_GMAIL.bat
   ```

2. **Sigue las instrucciones en pantalla:**
   - Ingresa tu email de Gmail
   - Ingresa la contraseña de aplicación (ver instrucciones abajo)
   - El script probará la conexión automáticamente
   - Creará el archivo `.env` con la configuración

3. **¡Listo!** Reinicia el servidor Django y prueba la recuperación de contraseña

### Opción 2: Configuración Manual

1. **Crea un archivo `.env` en la raíz del proyecto:**
   ```env
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=tu_email@gmail.com
   EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion
   DEFAULT_FROM_EMAIL=DIGITSOFT <tu_email@gmail.com>
   ADMIN_EMAIL=tu_email@gmail.com
   SITE_URL=http://localhost:8000
   ```

2. **Instala python-dotenv:**
   ```bash
   pip install python-dotenv
   ```

3. **Reinicia el servidor Django**

## 🔑 CÓMO OBTENER CONTRASEÑA DE APLICACIÓN DE GMAIL

### Paso a Paso:

1. **Ve a tu cuenta de Google:**
   - https://myaccount.google.com/

2. **Activa la verificación en dos pasos:**
   - Menú lateral → Seguridad → Verificación en dos pasos
   - Sigue las instrucciones para activarla

3. **Genera una contraseña de aplicación:**
   - Ve a: https://myaccount.google.com/apppasswords
   - Selecciona "Correo" como aplicación
   - Selecciona "Windows Computer" como dispositivo
   - Haz clic en "Generar"

4. **Copia la contraseña:**
   - Gmail mostrará una contraseña de 16 caracteres
   - Cópiala (sin espacios)
   - Úsala en `EMAIL_HOST_PASSWORD`

### ⚠️ IMPORTANTE:
- **NO uses tu contraseña normal de Gmail**
- **Usa SOLO la contraseña de aplicación generada**
- La contraseña tiene este formato: `abcd efgh ijkl mnop` (16 caracteres)
- Elimina los espacios al copiarla: `abcdefghijklmnop`

## 🧪 PROBAR LA CONFIGURACIÓN

### Desde la Aplicación:
1. Ve a la página de login
2. Haz clic en "¿Olvidaste tu contraseña?"
3. Ingresa tu email
4. **El correo debería llegar en menos de 1 minuto**

### Desde el Script:
```bash
python configurar_email_gmail.py
```
El script incluye una opción para enviar un email de prueba.

## 📊 VELOCIDAD ESPERADA

- **Con Gmail configurado:** 5-30 segundos
- **Factores que afectan la velocidad:**
  - Velocidad de internet
  - Carga del servidor SMTP de Gmail
  - Configuración del cliente de correo del destinatario
  - Filtros anti-spam

## 🐛 SOLUCIÓN DE PROBLEMAS

### El correo no llega:

1. **Verifica la configuración:**
   ```bash
   python configurar_email_gmail.py
   ```

2. **Revisa la carpeta de SPAM** del destinatario

3. **Verifica los logs en la consola de Django:**
   - Deberías ver: "✅ EMAIL DE RECUPERACIÓN ENVIADO"
   - Si ves errores, léelos cuidadosamente

4. **Errores comunes:**
   - **"Authentication failed":** Contraseña incorrecta o no es de aplicación
   - **"Connection timeout":** Problemas de red o firewall
   - **"Permission denied":** Verificación en dos pasos no activada

### Modo Desarrollo (Sin Gmail):

Si no quieres configurar Gmail aún, puedes usar el modo consola:

En `.env`:
```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

Los emails se mostrarán en la consola con un link directo para resetear.

## 📁 ARCHIVOS CREADOS/MODIFICADOS

### Nuevos Archivos:
- ✅ `configurar_email_gmail.py` - Script de configuración interactivo
- ✅ `CONFIGURAR_EMAIL_GMAIL.bat` - Ejecutable de Windows
- ✅ `.env.example` - Plantilla de configuración
- ✅ `CONFIGURACION_EMAIL_RAPIDO.md` - Esta documentación

### Archivos Modificados:
- ✅ `config/settings.py` - Configuración de email optimizada
- ✅ `usuarios/views.py` - Función de recuperación mejorada con HTML

## 🔐 SEGURIDAD

- ✅ Las contraseñas se almacenan en `.env` (NO subir a Git)
- ✅ `.env` está en `.gitignore`
- ✅ Usa contraseñas de aplicación (no la contraseña real de Gmail)
- ✅ Los tokens de recuperación expiran en 24 horas
- ✅ Los tokens solo se pueden usar una vez

## 📱 COMPATIBILIDAD

- ✅ Gmail (configurado por defecto)
- ✅ Outlook/Hotmail (cambiar host a smtp.office365.com)
- ✅ Otros proveedores SMTP (cambiar configuración en .env)

## 🎯 PRÓXIMOS PASOS

1. Ejecuta `CONFIGURAR_EMAIL_GMAIL.bat`
2. Sigue las instrucciones del script
3. Reinicia el servidor Django
4. Prueba la recuperación de contraseña
5. ¡Disfruta de los correos rápidos! 🚀

## 💡 TIPS ADICIONALES

### Para Producción:
- Usa un servicio de email transaccional (SendGrid, Mailgun, Amazon SES)
- Configura SPF y DKIM para evitar spam
- Usa dominios personalizados para emails
- Implementa rate limiting para prevenir abuso

### Para Desarrollo:
- Usa `console.EmailBackend` para no enviar emails reales
- O usa servicios de prueba como Mailtrap.io
- Activa DEBUG=True para ver links directos

---

**¿Necesitas ayuda?** Revisa los logs de Django o ejecuta el script de configuración.

**© 2026 DIGITSOFT - Sistema de Gestión Empresarial**

