# 🔒 CONFIGURACIÓN SEGURA DE CREDENCIALES

## ⚠️ IMPORTANTE: NUNCA SUBAS CREDENCIALES A GIT

Este proyecto usa **Google OAuth** para autenticación. Las credenciales **NUNCA** deben incluirse directamente en el código fuente.

---

## 📋 ARCHIVOS PROTEGIDOS

Los siguientes archivos están en `.gitignore` y **NO se suben a GitHub**:

- `limpiar_google_oauth.py` - Contiene credenciales hardcodeadas
- `INSTRUCCIONES_DAVID.txt` - Contiene información de configuración
- `SERVIDOR_INICIADO_LISTO.txt` - Contiene credenciales
- `*_CREDENCIALES.txt` - Cualquier archivo con credenciales
- `*_SECRETS.py` - Archivos de secretos
- `config_local.py` - Configuración local

---

## ✅ CÓMO CONFIGURAR GOOGLE OAUTH

### Opción 1: Variables de Entorno (Recomendado)

```bash
# Windows (PowerShell)
$env:GOOGLE_CLIENT_ID="tu_client_id_aqui"
$env:GOOGLE_CLIENT_SECRET="tu_client_secret_aqui"
python configurar_google_oauth_seguro.py

# Linux/Mac
export GOOGLE_CLIENT_ID="tu_client_id_aqui"
export GOOGLE_CLIENT_SECRET="tu_client_secret_aqui"
python configurar_google_oauth_seguro.py
```

### Opción 2: Panel de Administración de Django

1. Inicia el servidor: `python manage.py runserver`
2. Ve a: http://127.0.0.1:8000/admin/
3. Navega a: **Social applications** → **Add**
4. Configura:
   - Provider: `google`
   - Name: `Google OAuth DIGIT SOFT`
   - Client ID: `[tu_client_id]`
   - Secret key: `[tu_secret]`
   - Sites: Selecciona `localhost:8000`
5. Guarda

### Opción 3: Archivo .env (Crear localmente)

Crea un archivo `.env` en la raíz del proyecto:

```env
GOOGLE_CLIENT_ID=tu_client_id_aqui
GOOGLE_CLIENT_SECRET=tu_client_secret_aqui
```

**NOTA:** El archivo `.env` ya está en `.gitignore` y NO se subirá a GitHub.

---

## 🔑 OBTENER CREDENCIALES DE GOOGLE

1. Ve a: https://console.cloud.google.com/
2. Crea un proyecto o selecciona uno existente
3. Ve a: **APIs y servicios** → **Credenciales**
4. Haz clic en: **Crear credenciales** → **ID de cliente de OAuth 2.0**
5. Configura:
   - Tipo: `Aplicación web`
   - Orígenes JavaScript autorizados:
     - `http://127.0.0.1:8000`
     - `http://localhost:8000`
   - URIs de redirección autorizados:
     - `http://127.0.0.1:8000/accounts/google/login/callback/`
     - `http://localhost:8000/accounts/google/login/callback/`
6. Copia el **Client ID** y **Client Secret**

---

## 🚨 SI ACCIDENTALMENTE SUBISTE CREDENCIALES

Si ya subiste credenciales a GitHub:

1. **REVOCA las credenciales inmediatamente** en Google Cloud Console
2. **Crea nuevas credenciales**
3. Limpia el historial de Git:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch ARCHIVO_CON_CREDENCIALES" \
     --prune-empty --tag-name-filter cat -- --all
   ```
4. Fuerza el push:
   ```bash
   git push origin --force --all
   ```

---

## ✅ BUENAS PRÁCTICAS

- ✅ Usa variables de entorno para credenciales
- ✅ Agrega archivos sensibles a `.gitignore`
- ✅ Usa placeholders en ejemplos (ej: `TU_CLIENT_ID_AQUI`)
- ✅ Documenta cómo obtener las credenciales
- ❌ NUNCA hagas commit de credenciales reales
- ❌ NUNCA compartas credenciales en chat/email
- ❌ NUNCA uses credenciales de producción en desarrollo

---

## 📞 SOPORTE

Si necesitas ayuda con la configuración, consulta:
- `GOOGLE_OAUTH_ARREGLADO.md` - Guía completa de OAuth
- `SOLUCIONAR_ERROR_400.md` - Solución de errores comunes

