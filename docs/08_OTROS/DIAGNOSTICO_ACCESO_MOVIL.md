# 🔧 DIAGNÓSTICO Y SOLUCIÓN - NO PUEDO ACCEDER DESDE EL MÓVIL

## 🎯 PROBLEMA IDENTIFICADO

No puedes acceder desde tu móvil a: `http://192.168.137.221:8000/`

---

## ✅ SOLUCIÓN PASO A PASO

### **SOLUCIÓN 1: Usar el Script Automático (RECOMENDADO)**

1. **Click derecho** sobre el archivo:
   ```
   SOLUCIONAR_ACCESO_MOVIL.bat
   ```

2. Selecciona: **"Ejecutar como administrador"**

3. Acepta el diálogo de seguridad (UAC)

4. El script va a:
   - ✅ Configurar el firewall automáticamente
   - ✅ Iniciar el servidor correctamente
   - ✅ Mostrarte las URLs para usar en el móvil

5. Una vez iniciado, en tu móvil:
   - Abre el navegador
   - Escribe: `http://192.168.137.221:8000/`

---

### **SOLUCIÓN 2: Manual (Si la anterior no funciona)**

#### Paso 1: Configurar el Firewall Manualmente

**Opción A - Comando (Como Administrador):**
```cmd
netsh advfirewall firewall add rule name="Django Port 8000" dir=in action=allow protocol=TCP localport=8000
```

**Opción B - Interfaz Gráfica:**
1. Presiona `Windows + R`
2. Escribe: `wf.msc` y Enter
3. Click en "Reglas de entrada" (lado izquierdo)
4. Click en "Nueva regla..." (lado derecho)
5. Selecciona "Puerto" → Siguiente
6. Selecciona "TCP" y escribe `8000` → Siguiente
7. Selecciona "Permitir la conexión" → Siguiente
8. Marca TODAS las casillas (Dominio, Privado, Público) → Siguiente
9. Nombre: `Django DigitSoft` → Finalizar

#### Paso 2: Iniciar el Servidor Correctamente

```cmd
python manage.py runserver 0.0.0.0:8000
```

⚠️ **IMPORTANTE**: Debe decir `0.0.0.0:8000` NO `127.0.0.1:8000`

#### Paso 3: Verificar que Funciona en tu PC Primero

Abre el navegador en tu PC y prueba:
```
http://192.168.137.221:8000/
```

Si funciona aquí, funcionará en el móvil.

#### Paso 4: Conectar desde el Móvil

1. **Verifica el WiFi**: Mismo WiFi en ambos dispositivos
2. **Abre el navegador móvil**
3. **Escribe exactamente**: `http://192.168.137.221:8000/`
4. **NO uses https://** solo http://

---

## 🔍 DIAGNÓSTICO: ¿Por qué no funciona?

### Causa 1: Firewall Bloqueando (MÁS COMÚN) 🔥

**Síntomas:**
- Timeout o "No se puede conectar"
- Funciona en la PC pero no en el móvil

**Solución:**
- Usa el script `SOLUCIONAR_ACCESO_MOVIL.bat` como Administrador
- O configura el firewall manualmente (ver arriba)

**Verificar:**
```cmd
netsh advfirewall firewall show rule name=all | findstr 8000
```

---

### Causa 2: Servidor No Está Corriendo Correctamente 🚫

**Síntomas:**
- No funciona ni en la PC ni en el móvil

**Solución:**
```cmd
python manage.py runserver 0.0.0.0:8000
```

**Verificar:**
Debes ver este mensaje:
```
Starting development server at http://0.0.0.0:8000/
```

---

### Causa 3: WiFi Diferente 📶

**Síntomas:**
- Ping falla desde el móvil

**Solución:**
1. En el móvil: Configuración → WiFi
2. Verifica que sea el MISMO nombre de red que tu PC
3. Si usas hotspot, conecta el móvil al hotspot de la PC

**Verificar en PC:**
```cmd
ipconfig
```
Busca: `Puerta de enlace predeterminada` - debe ser igual en ambos

---

### Causa 4: URL Incorrecta ⌨️

**Errores comunes:**
- ❌ `https://192.168.137.221:8000/` (debe ser http://)
- ❌ `192.168.137.221` (falta el puerto :8000)
- ❌ `http://localhost:8000/` (solo funciona en la PC)
- ❌ Espacios o caracteres extraños

**URL Correcta:**
```
http://192.168.137.221:8000/
```

---

### Causa 5: Antivirus o Software de Seguridad 🛡️

**Síntomas:**
- Firewall configurado pero aún no funciona

**Solución:**
Desactiva temporalmente:
- Antivirus (Windows Defender, Norton, etc.)
- VPN si tienes activa
- Software de seguridad de terceros

**Prueba y si funciona, agrega una excepción en el antivirus.**

---

## 🧪 PRUEBAS DE DIAGNÓSTICO

### Test 1: Servidor Activo
```cmd
netstat -an | findstr :8000
```
Debe mostrar: `0.0.0.0:8000` o similar

### Test 2: Ping desde el Móvil
En tu móvil, instala una app de "Network Tools" y haz ping a:
```
192.168.137.221
```
Debe responder. Si no responde, problema de red.

### Test 3: Acceso desde la PC
En el navegador de tu PC:
```
http://192.168.137.221:8000/
```
Debe funcionar.

### Test 4: Firewall
```cmd
netsh advfirewall show allprofiles state
```
Si dice "Activado", el firewall está activo y necesitas configurarlo.

---

## 🆘 SOLUCIONES RÁPIDAS (ORDEN DE PRIORIDAD)

### ⚡ Opción 1: Desactiva el Firewall (Solo para probar)
1. Panel de Control → Firewall de Windows
2. "Activar o desactivar Firewall de Windows"
3. Desactiva AMBOS (Red privada y pública)
4. Prueba acceder desde el móvil
5. **Si funciona**: El problema es el firewall, reactívalo y usa el script

### ⚡ Opción 2: Reinicia Todo
1. Presiona `CTRL+C` en el servidor
2. Cierra la terminal
3. Ejecuta: `SOLUCIONAR_ACCESO_MOVIL.bat` como Admin
4. Prueba desde el móvil

### ⚡ Opción 3: Cambia el Puerto
Si 8000 está bloqueado, prueba otro puerto:
```cmd
python manage.py runserver 0.0.0.0:8080
```
Luego en el móvil: `http://192.168.137.221:8080/`

---

## 📋 CHECKLIST DE VERIFICACIÓN

Antes de contactar soporte, verifica:

- [ ] El servidor está corriendo con `0.0.0.0:8000`
- [ ] El firewall permite el puerto 8000
- [ ] Ambos dispositivos en el mismo WiFi
- [ ] URL correcta: `http://192.168.137.221:8000/`
- [ ] La URL funciona en el navegador de la PC
- [ ] No hay antivirus bloqueando
- [ ] El móvil puede hacer ping a la IP

---

## 📱 URLS PARA TU MÓVIL

Una vez que funcione, guarda estas URLs:

```
🏠 Inicio:     http://192.168.137.221:8000/
🛒 Tienda:     http://192.168.137.221:8000/tienda/
🛒 Carrito:    http://192.168.137.221:8000/tienda/carrito/
📊 Dashboard:  http://192.168.137.221:8000/dashboard/
🔐 Login:      http://192.168.137.221:8000/usuarios/login/
```

---

## 💡 CONSEJOS ADICIONALES

### Si estás en tu casa con WiFi normal:
Tu router probablemente está asignando IPs en el rango `192.168.1.x` o `192.168.0.x`.
Verifica con `ipconfig` y usa esa IP en vez de `192.168.137.221`.

### Si usas Hotspot Móvil desde tu PC:
La IP `192.168.137.221` es correcta. Asegúrate de:
1. Hotspot activado en la PC
2. Móvil conectado a ese hotspot
3. No a otro WiFi

### Para acceso permanente:
1. Configura IP estática en tu router
2. Configura port forwarding si quieres acceso desde internet (NO recomendado en desarrollo)
3. Usa ngrok para compartir temporalmente

---

## 🎯 SOLUCIÓN DEFINITIVA

**HAZ ESTO AHORA:**

1. **Click derecho** en: `SOLUCIONAR_ACCESO_MOVIL.bat`
2. **Ejecutar como administrador**
3. **Espera** a que diga "SERVIDOR ACTIVO"
4. En tu móvil: `http://192.168.137.221:8000/`

**Si aún no funciona después de esto:**
1. Desactiva el firewall completamente (solo para probar)
2. Si funciona con firewall desactivado → Problema de firewall
3. Si NO funciona ni con firewall desactivado → Problema de red WiFi

---

## 📞 ESTADO ACTUAL

Tu configuración:
- ✅ IP: `192.168.137.221`
- ✅ Puerto: `8000`
- ✅ ALLOWED_HOSTS: Configurado
- ⚠️  Firewall: Probablemente bloqueando
- ⚠️  Servidor: Necesita reinicio

---

**🎉 Con estas soluciones deberías poder acceder sin problemas.**

*Última actualización: 20/11/2025*

