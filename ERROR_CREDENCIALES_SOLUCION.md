# ⚠️ ERROR: Credenciales No Aceptadas

## 🔴 PROBLEMA DETECTADO:

El email NO se pudo enviar. Error:
```
Username and Password not accepted
```

## ✅ SOLUCIÓN:

Necesitas verificar que la **Verificación en 2 Pasos** esté COMPLETAMENTE activada.

---

## 📋 PASOS PARA SOLUCIONAR:

### 1️⃣ Verifica Verificación en 2 Pasos

1. **Ve a:** https://myaccount.google.com/security

2. **Busca:** "Verificación en dos pasos"

3. **Debe decir:** "Activada" ✅

4. **Si dice "Desactivada":**
   - Haz clic en "Comenzar"
   - Sigue el asistente
   - Usa tu teléfono para verificar
   - Completa la activación

### 2️⃣ Genera NUEVA Contraseña de Aplicación

Una vez que la verificación en 2 pasos esté activada:

1. **Ve a:** https://myaccount.google.com/apppasswords

2. **En "Nombre de la aplicación":** Escribe `DIGIT SOFT`

3. **Haz clic en:** "Crear"

4. **Copia la nueva contraseña** de 16 caracteres (sin espacios)

### 3️⃣ Actualiza el archivo .env

1. **Abre:** `C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo\.env`

2. **Busca la línea:**
   ```env
   EMAIL_HOST_PASSWORD=rxsugagwrnzzacdm
   ```

3. **Reemplázala con la NUEVA contraseña:**
   ```env
   EMAIL_HOST_PASSWORD=tu_nueva_contraseña_sin_espacios
   ```

4. **Guarda el archivo**

### 4️⃣ Prueba de Nuevo

```bash
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python probar_email.py
```

---

## 🔍 VERIFICACIÓN RÁPIDA:

### ¿Tienes Verificación en 2 Pasos activada?

Verifica aquí: https://myaccount.google.com/security

- ✅ **SÍ está activada** → Genera nueva contraseña de aplicación
- ❌ **NO está activada** → Actívala primero, luego genera la contraseña

---

## 📧 ALTERNATIVA: Usa Otro Email

Si tienes problemas con `davidcristancho160@gmail.com`, puedes:

1. Crear una cuenta Gmail NUEVA específica para la aplicación
2. Activar verificación en 2 pasos
3. Generar contraseña de aplicación
4. Actualizar `.env` con el nuevo email y contraseña

---

## 💡 AYUDA ADICIONAL:

### Si la contraseña que copiaste fue:
```
rxsu gagw rnzz acdm
```

### En .env debe quedar (SIN ESPACIOS):
```env
EMAIL_HOST_PASSWORD=rxsugagwrnzzacdm
```

### Verifica que NO tenga:
- ❌ Espacios
- ❌ Saltos de línea
- ❌ Caracteres extra

---

## 🎯 RESUMEN:

1. ✅ Activa Verificación en 2 Pasos (si no está)
2. ✅ Genera NUEVA contraseña de aplicación
3. ✅ Cópiala SIN espacios
4. ✅ Actualiza `.env`
5. ✅ Ejecuta `python probar_email.py`

---

## 📞 ESTADO ACTUAL:

- ✅ Contraseña configurada en `.env`: `rxsugagwrnzzacdm`
- ❌ Error al enviar: Credenciales no aceptadas
- ⚠️ Acción requerida: Verificar que verificación en 2 pasos esté activada

---

**Verifica la verificación en 2 pasos y genera una nueva contraseña si es necesario.**

