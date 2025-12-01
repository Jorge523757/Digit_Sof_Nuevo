# 🌐 GUÍA COMPLETA DE CONEXIÓN - DIGIT SOFT

## 📍 TUS DIRECCIONES IP DISPONIBLES

Según tu configuración de red, tienes múltiples formas de conectarte:

### 1️⃣ **Conexión Ethernet (Cable)** - Red 192.168.1.x
- **IP**: `192.168.1.56`
- **Máscara**: `255.255.255.0`
- **Gateway**: `192.168.1.1`
- **Uso**: Conexión principal por cable

### 2️⃣ **Conexión WiFi** - Red 192.168.137.x
- **IP**: `192.168.137.221`
- **Máscara**: `255.255.255.0`
- **Gateway**: `192.168.137.1`
- **Uso**: Punto de acceso WiFi / Hotspot móvil

### 3️⃣ **Localhost** - Solo en esta PC
- **IP**: `127.0.0.1` o `localhost`
- **Uso**: Acceso solo desde la PC donde corre el servidor

---

## 🖥️ ACCESO DESDE ESTA COMPUTADORA

Puedes usar cualquiera de estas URLs:

```
http://localhost:8000/
http://127.0.0.1:8000/
http://192.168.1.56:8000/
http://192.168.137.221:8000/
```

**Recomendado**: `http://localhost:8000/`

---

## 📱 ACCESO DESDE TELÉFONO/TABLET

### Método 1: Red Ethernet (192.168.1.x)

**Requisito**: Tu teléfono debe estar conectado a la **misma red WiFi** que está conectada a tu router principal.

#### URLs disponibles:

| Página | URL |
|--------|-----|
| 🏠 **Inicio** | `http://192.168.1.56:8000/` |
| 🛒 **Tienda** | `http://192.168.1.56:8000/tienda/` |
| 🛒 **Carrito** | `http://192.168.1.56:8000/tienda/carrito/` |
| 📊 **Dashboard** | `http://192.168.1.56:8000/dashboard/` |
| 🔐 **Login** | `http://192.168.1.56:8000/usuarios/login/` |
| 📦 **Productos** | `http://192.168.1.56:8000/productos/` |

### Método 2: Red WiFi / Hotspot (192.168.137.x)

**Requisito**: Tu teléfono debe estar conectado al **hotspot WiFi** de tu PC.

#### URLs disponibles:

| Página | URL |
|--------|-----|
| 🏠 **Inicio** | `http://192.168.137.221:8000/` |
| 🛒 **Tienda** | `http://192.168.137.221:8000/tienda/` |
| 🛒 **Carrito** | `http://192.168.137.221:8000/tienda/carrito/` |
| 📊 **Dashboard** | `http://192.168.137.221:8000/dashboard/` |
| 🔐 **Login** | `http://192.168.137.221:8000/usuarios/login/` |
| 📦 **Productos** | `http://192.168.137.221:8000/productos/` |

---

## 💻 ACCESO DESDE OTRA COMPUTADORA EN LA RED

### Si la otra PC está en la red Ethernet (192.168.1.x):
```
http://192.168.1.56:8000/
```

### Si la otra PC está conectada al hotspot (192.168.137.x):
```
http://192.168.137.221:8000/
```

---

## ⚙️ CONFIGURACIÓN Y REQUISITOS

### ✅ 1. Iniciar el Servidor

**Opción A - Script Automático** (Recomendado):
```batch
Doble clic en: INICIAR_SERVIDOR_MOVIL.bat
```

**Opción B - Manual**:
```bash
cd C:\Users\jorge\OneDrive\Escritorio\DigitSoftAdelanto\Digit_Sof_Nuevo
python manage.py runserver 0.0.0.0:8000
```

### ✅ 2. Configurar Firewall de Windows

El firewall debe permitir conexiones entrantes en el puerto 8000.

**Método Automático** (Ejecutar como Administrador):
```cmd
netsh advfirewall firewall add rule name="Django Dev Server" dir=in action=allow protocol=TCP localport=8000
```

**Método Manual**:
1. Panel de Control → Sistema y Seguridad → Firewall de Windows
2. Configuración avanzada
3. Reglas de entrada → Nueva regla
4. Puerto → TCP → Puerto específico: 8000
5. Permitir la conexión → Aplicar a todos los perfiles
6. Nombre: "Django Dev Server Port 8000"

### ✅ 3. Verificar que el Servidor Está Corriendo

Abre el navegador y prueba:
```
http://localhost:8000/
```

Si ves la página de DigitSoft, el servidor está funcionando correctamente.

### ✅ 4. Conectar Dispositivo Móvil

**Para red Ethernet**:
1. Conecta tu teléfono al mismo WiFi que tu PC
2. Abre el navegador móvil
3. Accede a: `http://192.168.1.56:8000/`

**Para hotspot móvil**:
1. Activa el hotspot WiFi en tu PC
2. Conecta tu teléfono a ese hotspot
3. Accede a: `http://192.168.137.221:8000/`

---

## 🔧 COMANDOS ÚTILES

### Ver tus IPs actuales:
```cmd
ipconfig
```

### Verificar si el puerto 8000 está abierto:
```cmd
netstat -an | findstr :8000
```

### Hacer ping a tu servidor desde el teléfono:
```cmd
ping 192.168.1.56
```

### Ver configuración de firewall:
```cmd
netsh advfirewall firewall show rule name=all | findstr 8000
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### ❌ Problema: "No se puede conectar" desde el teléfono

**Soluciones**:

1. **Verifica que el servidor esté corriendo**:
   ```
   Debes ver: "Starting development server at http://0.0.0.0:8000/"
   ```

2. **Verifica la IP con ipconfig**:
   ```cmd
   ipconfig
   ```
   Busca la IP correcta en "Dirección IPv4"

3. **Prueba con ambas IPs**:
   - `http://192.168.1.56:8000/`
   - `http://192.168.137.221:8000/`

4. **Verifica que estén en la misma red**:
   - Teléfono y PC deben estar en el mismo WiFi
   - O el teléfono debe estar conectado al hotspot de la PC

5. **Desactiva temporalmente el firewall** (para probar):
   ```
   Panel de Control → Firewall de Windows → Activar o desactivar
   ```

6. **Verifica desde la PC primero**:
   ```
   http://localhost:8000/
   ```

### ❌ Problema: "Bad Request (400)"

**Solución**:
- El servidor ya está configurado correctamente en `ALLOWED_HOSTS`
- Reinicia el servidor: Presiona `CTRL+C` y vuelve a iniciarlo

### ❌ Problema: "Timeout" o "No se puede alcanzar el sitio"

**Soluciones**:

1. **Verifica el firewall**:
   - Debe permitir conexiones en puerto 8000

2. **Prueba hacer ping**:
   ```cmd
   ping 192.168.1.56
   ```
   Debe responder. Si no responde, hay un problema de red.

3. **Verifica que ambos dispositivos estén en la misma red**:
   - Ve a Configuración → WiFi en tu teléfono
   - Debe mostrar el mismo nombre de red que tu PC

### ❌ Problema: El contador del carrito no funciona

**Solución**:
1. Abre la consola del navegador (F12)
2. Ejecuta:
   ```javascript
   localStorage.clear();
   location.reload();
   ```

### ❌ Problema: Los botones no responden

**Solución**:
1. Limpia la caché del navegador
2. Presiona `CTRL + F5` para refrescar forzadamente
3. Verifica en la consola (F12) si hay errores JavaScript

---

## 📊 RESUMEN RÁPIDO

### Para conectar desde tu teléfono:

```
1️⃣  Inicia el servidor:
    Doble clic en: INICIAR_SERVIDOR_MOVIL.bat

2️⃣  Conecta tu teléfono al mismo WiFi

3️⃣  Abre el navegador móvil

4️⃣  Escribe: http://192.168.1.56:8000/
    (O prueba: http://192.168.137.221:8000/)

5️⃣  ¡Listo! Ya puedes navegar en la tienda
```

---

## 🎯 CASOS DE USO

### Caso 1: Estás en tu casa con WiFi normal
- **PC**: Conectada por cable Ethernet o WiFi al router
- **Teléfono**: Conectado al mismo WiFi
- **URL a usar**: `http://192.168.1.56:8000/`

### Caso 2: Estás sin WiFi y quieres compartir desde tu PC
- **PC**: Activa hotspot móvil WiFi
- **Teléfono**: Conéctalo al hotspot de la PC
- **URL a usar**: `http://192.168.137.221:8000/`

### Caso 3: Solo quieres probar en tu PC
- **URL a usar**: `http://localhost:8000/`

---

## 📝 CONFIGURACIÓN ACTUAL

### ALLOWED_HOSTS (Ya configurado ✅):
```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '192.168.1.56',       # IP Ethernet
    '192.168.1.*',        # Red Ethernet completa
    '192.168.137.1',      # Adaptador local
    '192.168.137.221',    # IP WiFi
    '192.168.137.*',      # Red WiFi completa
    '*',                  # Permite todas (solo desarrollo)
]
```

### Servidor corriendo en:
```
0.0.0.0:8000
```
Esto significa que acepta conexiones desde cualquier interfaz de red.

---

## 🔒 SEGURIDAD

### ⚠️ IMPORTANTE - Solo para Desarrollo:

Esta configuración es **SOLO para desarrollo local**. 

**NO uses esto en producción** porque:
- `DEBUG = True` expone información sensible
- `ALLOWED_HOSTS = ['*']` permite conexiones de cualquier origen
- `SECRET_KEY` es la misma por defecto

### Para producción necesitas:
- `DEBUG = False`
- `ALLOWED_HOSTS` específicos (tu dominio)
- `SECRET_KEY` única y segura
- HTTPS configurado
- Configuración de seguridad adicional

---

## 💡 TIPS Y TRUCOS

1. **Agrega un bookmark en tu teléfono**:
   - Guarda `http://192.168.1.56:8000/` como favorito

2. **Usa un código QR**:
   - Genera un código QR con la URL
   - Escanéalo con tu teléfono para acceso rápido

3. **Mantén el servidor corriendo**:
   - No cierres la ventana de comandos
   - Si la cierras accidentalmente, vuelve a ejecutar el `.bat`

4. **Monitorea las peticiones**:
   - La ventana de comandos muestra cada petición HTTP
   - Útil para debugging

5. **Acceso desde múltiples dispositivos**:
   - Puedes conectar varios teléfonos/tablets simultáneamente
   - Todos deben estar en la misma red

---

## 📚 ARCHIVOS ÚTILES

| Archivo | Descripción |
|---------|-------------|
| `INICIAR_SERVIDOR_MOVIL.bat` | Inicia el servidor automáticamente |
| `GUIA_CONEXION_COMPLETA.bat` | Muestra esta guía en ventana |
| `CARRITO_SISTEMA_CORREGIDO_PROFESIONAL.md` | Documentación del carrito |
| `config/settings.py` | Configuración de Django |

---

## 🎉 ¡TODO LISTO!

Tu sistema está completamente configurado y listo para:
- ✅ Acceso desde PC
- ✅ Acceso desde teléfono/tablet
- ✅ Acceso desde otras computadoras en la red
- ✅ Sistema de carrito funcional
- ✅ Sincronización en tiempo real

**¡Disfruta de tu e-commerce DigitSoft! 🛒✨**

---

*Última actualización: 20/11/2025*
*Versión: 2.0 - Soporte Completo Multi-Red*

