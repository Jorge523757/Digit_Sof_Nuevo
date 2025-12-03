# 🔧 Scripts del Proyecto Digit Soft E-commerce

Esta carpeta contiene todos los scripts ejecutables (.bat) organizados por función.

---

## 📂 Estructura de Carpetas

### 🚀 01_INICIAR/
Scripts para iniciar el sistema y sus componentes.

**Archivos típicos:**
- `INICIAR_ECOMMERCE.bat` - Inicia el servidor Django
- `INICIAR_SISTEMA.bat` - Inicia el sistema completo
- `ABRIR_ECOMMERCE.bat` - Abre el navegador en la tienda
- `DETECTAR_IP_E_INICIAR.bat` - Detecta IP y arranca servidor

**Uso:**
```
Doble clic en el script → El sistema se inicia automáticamente
```

---

### 🔍 02_DIAGNOSTICO/
Scripts para diagnosticar y verificar el estado del sistema.

**Archivos típicos:**
- `diagnosticar_carrito.py` - Verifica el estado del carrito
- `DIAGNOSTICAR_IMAGENES_CARRITO.js` - Script de consola para imágenes

**Uso:**
```
Ejecuta el script → Obtendrás un reporte del estado del sistema
```

---

### 🧹 03_LIMPIEZA/
Scripts para limpiar datos, cache y resetear el sistema.

**Archivos típicos:**
- Scripts de limpieza de localStorage
- Scripts de limpieza de carrito
- Scripts de reset de sistema

**Uso:**
```
⚠️ PRECAUCIÓN: Estos scripts eliminan datos
Ejecuta solo si sabes lo que haces
```

---

### 🛠️ 04_UTILIDADES/
Scripts de utilidades varias y herramientas auxiliares.

**Archivos típicos:**
- `crear_productos_*.py` - Crear productos de prueba
- `crear_superusuario.py` - Crear usuario admin
- `agregar_datos_*.py` - Agregar datos de prueba

**Uso:**
```
Ejecuta según necesites:
- Crear datos de prueba
- Configurar sistema
- Realizar tareas auxiliares
```

---

## 🚀 Cómo Usar los Scripts

### Windows:
```
1. Ve a la carpeta correspondiente
2. Doble clic en el archivo .bat
3. Sigue las instrucciones en pantalla
```

### Para Scripts Python:
```
1. Abre terminal/cmd
2. cd a la carpeta del proyecto
3. python nombre_script.py
```

---

## 📋 Scripts Más Utilizados

### Para Empezar:
```
scripts/01_INICIAR/INICIAR_ECOMMERCE.bat
→ Inicia el servidor Django en localhost:8000
```

### Para Crear Datos de Prueba:
```
scripts/04_UTILIDADES/crear_productos_completos.py
→ Crea productos de ejemplo para la tienda
```

### Para Diagnosticar Problemas:
```
scripts/02_DIAGNOSTICO/diagnosticar_carrito.py
→ Verifica el estado del carrito y detecta problemas
```

---

## 🔄 Agregar Nuevos Scripts

1. Crea tu script `.bat` en la raíz del proyecto
2. Nómbralo según la función:
   - `INICIAR_*.bat` → Se moverá a `01_INICIAR/`
   - `DIAGNOSTICO_*.bat` → Se moverá a `02_DIAGNOSTICO/`
   - `LIMPIAR_*.bat` → Se moverá a `03_LIMPIEZA/`
   - Otros → Se moverán a `04_UTILIDADES/`
3. Ejecuta `ORGANIZAR_DOCS.bat` desde la raíz
4. El script se moverá automáticamente

---

## ⚠️ Precauciones

### Scripts de LIMPIEZA:
- ⚠️ Eliminan datos permanentemente
- ⚠️ No se pueden deshacer
- ⚠️ Úsalos solo si estás seguro

### Scripts de INICIAR:
- ✅ Seguros de ejecutar
- ✅ Solo inician servicios
- ✅ Se pueden detener con Ctrl+C

### Scripts de DIAGNOSTICO:
- ✅ Solo lectura
- ✅ No modifican nada
- ✅ Generan reportes

### Scripts de UTILIDADES:
- ⚡ Pueden modificar la base de datos
- ⚡ Lee las instrucciones antes de ejecutar
- ⚡ Haz backup si es necesario

---

## 🎯 Flujo de Trabajo Típico

### 1. Configuración Inicial:
```
1. scripts/04_UTILIDADES/crear_superusuario.py
2. scripts/04_UTILIDADES/crear_productos_completos.py
3. scripts/01_INICIAR/INICIAR_ECOMMERCE.bat
```

### 2. Desarrollo Diario:
```
1. scripts/01_INICIAR/INICIAR_ECOMMERCE.bat
2. Desarrollar...
3. Ctrl+C para detener
```

### 3. Solución de Problemas:
```
1. scripts/02_DIAGNOSTICO/diagnosticar_carrito.py
2. Ver el reporte
3. Aplicar solución según el problema
```

### 4. Limpieza (si es necesario):
```
1. Hacer backup de datos importantes
2. scripts/03_LIMPIEZA/[script_apropiado].bat
3. Recargar datos de prueba si es necesario
```

---

## 📊 Estadísticas

Total de scripts: **~10-15 archivos**

Distribución aproximada:
- 🚀 Iniciar: ~5 scripts
- 🔍 Diagnóstico: ~3 scripts
- 🧹 Limpieza: ~2 scripts
- 🛠️ Utilidades: ~5 scripts

---

## 🔗 Enlaces Relacionados

- **Documentación:** `docs/README.md`
- **Guías de uso:** `docs/01_GUIAS/`
- **Soluciones:** `docs/02_SOLUCIONES/`

---

## 📝 Convenciones de Nombres

### Prefijos:
- `INICIAR_*.bat` - Inicia servicios
- `ABRIR_*.bat` - Abre aplicaciones
- `DIAGNOSTICO_*.bat` - Diagnóstico
- `LIMPIAR_*.bat` - Limpieza
- `crear_*.py` - Crear datos/objetos
- `agregar_*.py` - Agregar datos

### Sufijos:
- `*.bat` - Scripts Windows ejecutables
- `*.py` - Scripts Python (ejecutar con: python nombre.py)
- `*.js` - Scripts JavaScript (para consola del navegador)

---

## 🆘 Ayuda

Si un script no funciona:

1. **Verifica que estés en la carpeta correcta**
   ```
   cd C:\...\Digit_Sof_Nuevo
   ```

2. **Para scripts Python, verifica que Python esté instalado**
   ```
   python --version
   ```

3. **Lee la documentación del script**
   - Abre el archivo con un editor de texto
   - Lee los comentarios al inicio

4. **Busca ayuda en la documentación**
   - `docs/01_GUIAS/` - Guías de uso
   - `docs/02_SOLUCIONES/` - Soluciones a problemas

---

**Última actualización:** 2025-11-28
**Versión:** 1.0
**Total de scripts:** ~10-15 archivos

