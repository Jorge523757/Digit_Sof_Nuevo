```

### Paso 2: En la página de debug
1. Click en "📡 Probar API"
2. Lee los mensajes en el log
3. Si dice ✅ "API FUNCIONA" → El backend está OK
4. Si dice ❌ con error → Lee el mensaje de error

### Paso 3: Si el API funciona
1. El dropdown en la página de debug debería mostrar tus notificaciones
2. Si las ves ahí, el problema está solo en el dashboard
3. Ve al dashboard: http://127.0.0.1:8000/dashboard/
4. Presiona F12
5. Ve a la pestaña "Console"
6. Busca mensajes de `[Notificaciones]`

### Paso 4: Si no ves mensajes de [Notificaciones]
Significa que el archivo `notificaciones.js` no se está cargando.

**Solución:**
```bash
# Recolectar archivos estáticos
python manage.py collectstatic --noinput --clear

# Limpiar caché del navegador
Ctrl + Shift + Delete

# Recarga fuerte
Ctrl + F5
```

---

## 📋 Checklist de Verificación

Marca cada uno:

- [ ] Ejecuté DEBUG_NOTIFICACIONES.bat
- [ ] Se abrió la página de debug
- [ ] Presioné "Probar API"
- [ ] Vi el resultado en el log
- [ ] Si dio error de autenticación, inicié sesión
- [ ] Volví a probar el API
- [ ] El API responde con HTTP 200
- [ ] Veo mis notificaciones en el dropdown de la página de debug
- [ ] Fui al dashboard (http://127.0.0.1:8000/dashboard/)
- [ ] Abrí la consola del navegador (F12)
- [ ] Busqué mensajes de [Notificaciones]

---

## 🆘 Si TODO FALLA

### Opción Nuclear: Limpiar Todo y Recargar

```bash
# 1. Detén el servidor (Ctrl+C)

# 2. Limpia archivos estáticos
python manage.py collectstatic --noinput --clear

# 3. Reinicia el servidor
python manage.py runserver

# 4. En el navegador:
#    - Ctrl + Shift + Delete (limpiar caché)
#    - Cerrar todas las pestañas del sitio
#    - Abrir nueva pestaña
#    - Ir a: http://127.0.0.1:8000/usuarios/notificaciones/debug/
```

---

## 📸 Captura de Pantalla

Si sigues teniendo problemas, toma captura de:

1. **La página de debug** después de presionar "Probar API"
2. **La consola del navegador** (F12 → Console) en el dashboard
3. **El terminal** donde corre el servidor

Y muéstrame las 3 capturas para ayudarte mejor.

---

## ✅ Resultado Esperado

En la página de debug deberías ver algo como:

```
[12:34:56] 🚀 Iniciando test de API...
[12:34:56] 📡 Consultando: /usuarios/notificaciones/json/
[12:34:57] 📥 Respuesta recibida: HTTP 200
[12:34:57] ✅ API FUNCIONA CORRECTAMENTE
[12:34:57] 📊 Datos recibidos:
[12:34:57]    - Notificaciones no leídas: 17
[12:34:57]    - Total recibidas: 10
[12:34:57] 📝 Notificaciones:
[12:34:57]    1. Bienvenido a DIGITSOFT!
[12:34:57]    2. Nueva Venta Registrada
[12:34:57]    3. Orden de Servicio Pendiente
[12:34:57]    ...
[12:34:57] ✅ Dropdown actualizado con notificaciones
```

Y el dropdown debería mostrar las notificaciones con iconos y todo.

---

**Fecha:** 2025-01-09  
**Herramienta:** DEBUG_NOTIFICACIONES.bat  
**Página:** http://127.0.0.1:8000/usuarios/notificaciones/debug/
# 🔧 DIAGNÓSTICO INMEDIATO - NOTIFICACIONES

## ⚡ ACCIÓN INMEDIATA

### Ejecuta AHORA:
```bash
DEBUG_NOTIFICACIONES.bat
```

Esto hará:
1. ✅ Iniciar el servidor
2. ✅ Abrir automáticamente la página de debug
3. ✅ Mostrarte EXACTAMENTE qué está fallando

---

## 🎯 ¿Qué verás en la página de debug?

Una interfaz estilo "hacker" que te mostrará:

### Botones de Control:
- **📡 Probar API** - Verifica si el backend responde
- **🔍 Verificar DOM** - Chequea si los elementos HTML existen
- **⚙️ Test JavaScript** - Valida que JS esté funcionando
- **🗑️ Limpiar Log** - Limpia la consola de debug

### Log de Eventos:
Verás mensajes en tiempo real como:
```
[HH:MM:SS] 🚀 Iniciando test de API...
[HH:MM:SS] 📡 Consultando: /usuarios/notificaciones/json/
[HH:MM:SS] 📥 Respuesta recibida: HTTP 200
[HH:MM:SS] ✅ API FUNCIONA CORRECTAMENTE
[HH:MM:SS] 📊 Datos recibidos:
[HH:MM:SS]    - Notificaciones no leídas: 17
[HH:MM:SS]    - Total recibidas: 10
```

---

## 🔴 Posibles Errores y Soluciones

### Error 1: "NO ESTÁS AUTENTICADO"
**Síntoma:** HTTP 401 o 403

**Solución:**
1. Abre en otra pestaña: http://127.0.0.1:8000/usuarios/login/
2. Inicia sesión con tu usuario
3. Vuelve a la página de debug
4. Presiona "Probar API" nuevamente

### Error 2: "Elementos DOM no encontrados"
**Síntoma:** ❌ en verificación de DOM

**Causa:** El HTML no se está cargando correctamente

**Solución:**
- Limpia el caché: Ctrl + Shift + Delete
- Recarga la página: Ctrl + F5

### Error 3: "fetch API NO disponible"
**Síntoma:** JavaScript no funciona

**Causa:** Navegador muy antiguo

**Solución:**
- Actualiza tu navegador
- Usa Chrome, Firefox o Edge moderno

### Error 4: El botón no responde
**Síntoma:** Nada pasa al hacer clic

**Solución en la página de debug:**
1. Presiona "Verificar DOM" - ¿Todos ✅?
2. Presiona "Test JavaScript" - ¿Todos ✅?
3. Presiona "Probar API" - ¿Responde?

Si todo está ✅ pero el botón no funciona:
- Es un problema de CSS z-index
- Abre F12 → pestaña "Elements" / "Elementos"
- Inspecciona el botón de la campana
- Verifica que no haya otro elemento encima

---

## 🎮 Pasos de Debug

### Paso 1: Ejecutar DEBUG_NOTIFICACIONES.bat
```bash
DEBUG_NOTIFICACIONES.bat

