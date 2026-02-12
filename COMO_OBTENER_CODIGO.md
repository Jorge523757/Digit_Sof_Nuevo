# 🔐 TU CÓDIGO DE RECUPERACIÓN

## ⚡ SOLUCIÓN RÁPIDA

Ya que la caja morada no está apareciendo en la pantalla, aquí están **TODAS las formas** de obtener tu código:

---

## 📋 MÉTODO 1: Desde PowerShell (MÁS RÁPIDO)

### Abre PowerShell y ejecuta:

```powershell
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python obtener_codigo.py
```

**Esto te mostrará:**
```
==================================================
🔐 TU CÓDIGO DE RECUPERACIÓN
==================================================

   CÓDIGO: [6 DÍGITOS]

   Expira: [HORA]
   Email: davidcristancho160@gmail.com

==================================================

✅ COPIA ESTE CÓDIGO: [6 DÍGITOS]
```

---

## 📋 MÉTODO 2: Shell de Django

```powershell
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python manage.py shell
```

Luego pega esto:

```python
from usuarios.models_tokens import TokenRecuperacion
token = TokenRecuperacion.objects.filter(
    email__iexact='davidcristancho160@gmail.com',
    usado=False
).order_by('-fecha_creacion').first()
print(f"\n🔢 CÓDIGO: {token.codigo}\n")
```

---

## 📋 MÉTODO 3: Ver Logs del Servidor

Busca en la ventana de PowerShell donde corre el servidor Django:

```
🔐 CÓDIGO: [6 DÍGITOS]
```

---

## 📋 MÉTODO 4: Genera Nuevo Código

Si el actual expiró, genera uno nuevo:

```powershell
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python manage.py shell
```

```python
from django.contrib.auth.models import User
from usuarios.services_password import ServicioRecuperacionPassword

usuario = User.objects.filter(email__iexact='davidcristancho160@gmail.com').first()
exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(
    usuario.email,
    '127.0.0.1'
)
print(f"\n🔢 NUEVO CÓDIGO: {token.codigo}\n")
```

---

## 📧 SOBRE TU PREGUNTA: "¿Ahora sí puede llegar a mi correo?"

### Respuesta: **DEPENDE**

Para que llegue al correo necesitas:

### 1. Verificar si `EMAIL_HOST_PASSWORD` está configurado

```powershell
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python -c "from decouple import config; print(f'Password: {config(\"EMAIL_HOST_PASSWORD\", default=\"NO CONFIGURADO\")}')"
```

**Si dice "NO CONFIGURADO" o "AQUI_TU_CONTRASEÑA...":**
- ❌ Los emails NO llegarán
- ✅ El código se muestra en pantalla (pero no aparece por algún bug)
- ✅ El código está en la consola
- ✅ Puedes obtenerlo con los métodos de arriba

### 2. Si cambiaste la contraseña en `.env`:

**Abre:** `C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo\.env`

**Verifica que tenga:**
```env
EMAIL_HOST_PASSWORD=tu_contraseña_de_16_caracteres
```

**Y NO:**
```env
EMAIL_HOST_PASSWORD=AQUI_TU_CONTRASEÑA_DE_APLICACION
```

### 3. Reinicia el servidor después de cambiar `.env`:

```powershell
taskkill /F /IM python.exe
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python manage.py runserver
```

---

## ✅ PASOS PARA USAR EL CÓDIGO

### 1. Obtén el código (usa cualquier método de arriba)

### 2. Ve a la página de verificación:
```
http://127.0.0.1:8000/usuarios/verificar-codigo/
```

### 3. Ingresa el código de 6 dígitos

### 4. Haz clic en "Verificar Código"

### 5. Ingresa tu nueva contraseña

### 6. ¡Listo! ✅

---

## 🔧 POR QUÉ NO APARECE LA CAJA MORADA

Puede ser por:

1. **DEBUG no está en True**
   - Verifica: `config/settings.py`
   - Debe tener: `DEBUG = True`

2. **El código expiró**
   - Genera uno nuevo con el Método 4

3. **Problema en el template**
   - Pero el código sigue funcionando
   - Úsalo de la consola o con los scripts

---

## 📊 ESTADO ACTUAL

| Componente | Estado | Solución |
|------------|--------|----------|
| Sistema genera código | ✅ | Funciona |
| Código en BD | ✅ | Funciona |
| Código en consola | ✅ | Funciona |
| Caja morada en pantalla | ❌ | Usar métodos alternativos |
| Email llega al correo | ⚠️ | Depende de configuración |

---

## 🎯 ACCIÓN INMEDIATA

### OPCIÓN A: Usa el script (MÁS FÁCIL)

```powershell
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python obtener_codigo.py
```

### OPCIÓN B: Mira la consola del servidor

Busca: `🔐 CÓDIGO: [6 dígitos]`

### OPCIÓN C: Shell de Django

```python
from usuarios.models_tokens import TokenRecuperacion
t = TokenRecuperacion.objects.filter(email__iexact='davidcristancho160@gmail.com', usado=False).first()
print(t.codigo)
```

---

## 💡 RECOMENDACIÓN

**Usa el MÉTODO 1** (script `obtener_codigo.py`)

Es el más rápido y te da toda la información que necesitas.

Luego usa ese código en la página de verificación.

---

## 📧 PARA CONFIGURAR EMAIL (Si quieres que llegue al correo)

### 1. Genera contraseña de aplicación de Gmail:
```
https://myaccount.google.com/apppasswords
```

### 2. Edita `.env`:
```env
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

### 3. Reinicia servidor:
```powershell
taskkill /F /IM python.exe
python manage.py runserver
```

### 4. Prueba enviando nuevo código:
```
http://127.0.0.1:8000/usuarios/recuperar/
```

---

## ✅ RESUMEN

**El sistema funciona** ✅  
**El código se genera** ✅  
**Puedes obtenerlo** ✅  
**Puedes usarlo** ✅  

**Solo que la caja morada no aparece en pantalla**  
**Pero eso NO impide que recuperes tu contraseña**

**Usa cualquiera de los 4 métodos de arriba para obtener el código**

---

**¡El código está ahí, solo necesitas obtenerlo con uno de estos métodos!** 🚀

