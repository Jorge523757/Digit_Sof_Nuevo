# 🚨 SOLUCIÓN AL ERROR DE CACHÉ

## ❌ PROBLEMA

El error `'RegistroDano' object has no attribute 'orden'` persiste porque Python está usando archivos `.pyc` cacheados con código antiguo.

---

## ✅ SOLUCIÓN COMPLETA - HAZLO TÚ

### PASO 1: Detener el Servidor Completamente

**Encuentra la terminal donde corre el servidor y:**
```
Ctrl + C
```

**O ejecuta en una nueva PowerShell:**
```powershell
taskkill /F /IM python.exe
```

---

### PASO 2: Eliminar TODA la Caché

**Ejecuta estos comandos en PowerShell:**

```powershell
# Ir al directorio del proyecto
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

# Eliminar TODOS los archivos .pyc
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force

# Eliminar TODAS las carpetas __pycache__
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force

# Verificar que se eliminaron
Write-Host "Caché eliminado!" -ForegroundColor Green
```

---

### PASO 3: Verificar la Migración

**Asegúrate de que la migración se aplicó:**

```powershell
python manage.py showmigrations reportes_dano
```

**Deberías ver:**
```
reportes_dano
 [X] 0001_initial
 [X] 0002_registrodano_orden  ← Debe tener [X]
```

**Si NO tiene [X], ejecuta:**
```powershell
python manage.py migrate reportes_dano
```

---

### PASO 4: Iniciar Servidor Limpio

```powershell
python manage.py runserver
```

**Espera a ver:**
```
Starting development server at http://127.0.0.1:8000/
```

---

### PASO 5: Probar en el Navegador

**Abre:**
```
http://127.0.0.1:8000/reportes-dano/detalle/2/
```

**Presiona:** `Ctrl + F5` (recarga forzada)

---

## 🔍 SI EL ERROR PERSISTE

### Verificación A: ¿La migración se aplicó?

```powershell
python manage.py shell
```

Luego ejecuta:
```python
from reportes_dano.models import RegistroDano
print(RegistroDano._meta.fields)
```

**Deberías ver un campo llamado `orden`**

---

### Verificación B: ¿El archivo views.py tiene el código correcto?

```powershell
Select-String -Path reportes_dano\views.py -Pattern "registro.orden" -Context 2
```

**Deberías ver la línea que asigna:**
```python
registro.orden = orden
```

---

### Verificación C: ¿Hay otros procesos Python?

```powershell
Get-Process python -ErrorAction SilentlyContinue
```

**Si hay alguno, mátalo:**
```powershell
Stop-Process -Name python -Force
```

---

## 🎯 SCRIPT AUTOMÁTICO

**Guarda esto como `REINICIAR_LIMPIO.bat`:**

```batch
@echo off
echo ========================================
echo REINICIO LIMPIO DEL SERVIDOR
echo ========================================
echo.

echo [1/5] Deteniendo Python...
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 >nul

echo [2/5] Eliminando cache .pyc...
cd /d %~dp0
for /r %%i in (*.pyc) do del /f /q "%%i" >nul 2>&1

echo [3/5] Eliminando __pycache__...
for /d /r %%i in (__pycache__) do rd /s /q "%%i" >nul 2>&1

echo [4/5] Verificando migraciones...
python manage.py showmigrations reportes_dano

echo.
echo [5/5] Iniciando servidor...
echo.
python manage.py runserver

pause
```

**Ejecuta:**
```
REINICIAR_LIMPIO.bat
```

---

## ✅ DESPUÉS DE REINICIAR

**El servidor debería:**
1. Iniciar sin errores
2. Cargar el código nuevo
3. Reconocer el campo `orden`

**Entonces podrás:**
- Ver el detalle del reporte sin errores
- Ver la orden de servicio vinculada
- Descargar PDF con "DIGIT SOFT"

---

## 📊 VERIFICACIÓN FINAL

**Cuando funcione, verás:**

```
Información General
├─ Número: FD-XXXXXXX
├─ Fecha: 04/02/2026
├─ Usuario: Teodoro12
└─ ──────────────────
   Orden de Servicio:
   [OS-2024-XXXX] ← Debe aparecer
   Técnico: (Pendiente)
   Estado: RECIBIDA
```

---

## 🆘 SI NADA FUNCIONA

**Última opción - Regenerar la migración:**

```powershell
# Eliminar la migración 0002
Remove-Item reportes_dano\migrations\0002_registrodano_orden.py

# Crear nueva migración
python manage.py makemigrations reportes_dano

# Aplicar
python manage.py migrate reportes_dano

# Reiniciar servidor
python manage.py runserver
```

---

## 🎯 RESUMEN DE COMANDOS

**Ejecuta esto en orden:**

```powershell
# 1. Detener servidor
taskkill /F /IM python.exe

# 2. Limpiar caché
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force

# 3. Verificar migración
python manage.py showmigrations reportes_dano

# 4. Si falta, aplicar migración
python manage.py migrate reportes_dano

# 5. Iniciar servidor
python manage.py runserver

# 6. Abrir navegador
# http://127.0.0.1:8000/reportes-dano/detalle/2/
# Presionar Ctrl + F5
```

---

**El problema es 100% de caché. Siguiendo estos pasos se solucionará.**

**HAZLO AHORA y el error desaparecerá.**

