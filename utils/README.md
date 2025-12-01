# 🐍 Utilidades Python del Proyecto

Esta carpeta contiene todos los scripts Python (.py) organizados por función.

---

## 📂 Estructura de Carpetas

### 🧪 01_SCRIPTS_PRUEBA/
Scripts de prueba y testing.

**Archivos típicos:**
- `test_*.py` - Scripts de prueba
- `prueba_*.py` - Scripts de prueba rápida
- `demo_*.py` - Scripts de demostración

**Uso:**
```bash
python utils/01_SCRIPTS_PRUEBA/test_nombre.py
```

---

### 📊 02_CREAR_DATOS/
Scripts para crear y poblar datos en la base de datos.

**Archivos típicos:**
- `crear_productos_*.py` - Crear productos
- `crear_superusuario.py` - Crear usuario administrador
- `crear_usuario_*.py` - Crear usuarios
- `agregar_datos_*.py` - Agregar datos de prueba

**Uso:**
```bash
# Crear productos de prueba
python utils/02_CREAR_DATOS/crear_productos_completos.py

# Crear superusuario
python utils/02_CREAR_DATOS/crear_superusuario.py
```

---

### 🔍 03_DIAGNOSTICO/
Scripts para diagnosticar problemas del sistema.

**Archivos típicos:**
- `diagnosticar_*.py` - Diagnóstico de componentes
- `diagnostico_*.py` - Scripts de diagnóstico

**Uso:**
```bash
python utils/03_DIAGNOSTICO/diagnosticar_carrito.py
```

---

### ✅ 04_VERIFICACION/
Scripts para verificar el estado y funcionamiento del sistema.

**Archivos típicos:**
- `verificar_*.py` - Verificación de componentes
- `verificacion_*.py` - Scripts de verificación

**Uso:**
```bash
python utils/04_VERIFICACION/verificar_sistema.py
```

---

### ⚙️ 05_SETUP/
Scripts de configuración e inicialización.

**Archivos típicos:**
- `setup_*.py` - Scripts de configuración
- `init_*.py` - Scripts de inicialización
- `update_*.py` - Scripts de actualización

**Uso:**
```bash
python utils/05_SETUP/setup_data.py
```

---

### 📦 06_OTROS/
Scripts de utilidades varias.

**Archivos típicos:**
- Scripts que no encajan en otras categorías
- Utilidades auxiliares
- Scripts experimentales

---

## 🚀 Cómo Usar los Scripts

### Desde la Raíz del Proyecto:
```bash
# Ejecutar un script de creación de datos
python utils/02_CREAR_DATOS/crear_productos_completos.py

# Ejecutar un script de diagnóstico
python utils/03_DIAGNOSTICO/diagnosticar_carrito.py

# Ejecutar un script de prueba
python utils/01_SCRIPTS_PRUEBA/test_ecommerce.py
```

### Con el Entorno Virtual Activado:
```bash
# Windows
venv\Scripts\activate
python utils/02_CREAR_DATOS/crear_productos_completos.py

# Linux/Mac
source venv/bin/activate
python utils/02_CREAR_DATOS/crear_productos_completos.py
```

---

## 📋 Scripts Más Utilizados

### Para Configurar el Sistema:
```bash
# 1. Crear superusuario
python utils/02_CREAR_DATOS/crear_superusuario.py

# 2. Crear productos de prueba
python utils/02_CREAR_DATOS/crear_productos_completos.py

# 3. Crear usuarios de prueba
python utils/02_CREAR_DATOS/crear_usuario_cliente.py
```

### Para Diagnosticar Problemas:
```bash
# Diagnosticar carrito
python utils/03_DIAGNOSTICO/diagnosticar_carrito.py

# Verificar sistema
python utils/04_VERIFICACION/verificar_sistema.py
```

### Para Probar Funcionalidades:
```bash
# Probar e-commerce
python utils/01_SCRIPTS_PRUEBA/test_ecommerce.py

# Demo del sistema
python utils/01_SCRIPTS_PRUEBA/demo_ecommerce.py
```

---

## 🔄 Agregar Nuevos Scripts

1. Crea tu script `.py` en la raíz del proyecto
2. Nómbralo según la función:
   - `test_*.py` → Se moverá a `01_SCRIPTS_PRUEBA/`
   - `crear_*.py` → Se moverá a `02_CREAR_DATOS/`
   - `diagnostico_*.py` → Se moverá a `03_DIAGNOSTICO/`
   - `verificar_*.py` → Se moverá a `04_VERIFICACION/`
   - `setup_*.py` → Se moverá a `05_SETUP/`
   - Otros → Se moverán a `06_OTROS/`
3. Ejecuta `ORGANIZAR_DOCS.bat` desde la raíz
4. El script se moverá automáticamente

---

## ⚠️ Precauciones

### Scripts de CREAR_DATOS:
- ⚡ Modifican la base de datos
- ⚡ Pueden crear registros duplicados si se ejecutan varias veces
- ⚡ Hacer backup antes si es necesario

### Scripts de DIAGNOSTICO:
- ✅ Solo lectura
- ✅ No modifican nada
- ✅ Seguros de ejecutar

### Scripts de PRUEBA:
- ⚡ Algunos pueden modificar datos
- ⚡ Revisar el código antes de ejecutar
- ⚡ Usar en entornos de desarrollo

### Scripts de SETUP:
- ⚠️ Modifican configuración
- ⚠️ Pueden afectar el funcionamiento del sistema
- ⚠️ Leer las instrucciones antes de ejecutar

---

## 🎯 Flujo de Trabajo Típico

### 1. Configuración Inicial:
```bash
# Crear entorno y instalar dependencias
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Crear superusuario
python utils/02_CREAR_DATOS/crear_superusuario.py

# Crear datos de prueba
python utils/02_CREAR_DATOS/crear_productos_completos.py
```

### 2. Durante Desarrollo:
```bash
# Verificar sistema
python utils/04_VERIFICACION/verificar_sistema.py

# Probar funcionalidad
python utils/01_SCRIPTS_PRUEBA/test_ecommerce.py
```

### 3. Solución de Problemas:
```bash
# Diagnosticar
python utils/03_DIAGNOSTICO/diagnosticar_carrito.py

# Ver el reporte
# Aplicar solución según el problema
```

---

## 📊 Estadísticas

Total de scripts Python: **~40-50 archivos** (aproximado)

Distribución aproximada:
- 🧪 Pruebas: ~10 scripts
- 📊 Crear datos: ~15 scripts
- 🔍 Diagnóstico: ~5 scripts
- ✅ Verificación: ~5 scripts
- ⚙️ Setup: ~5 scripts
- 📦 Otros: ~5-10 scripts

---

## 🔗 Enlaces Relacionados

- **Documentación:** `docs/README.md`
- **Scripts BAT:** `scripts/README.md`
- **Guías de uso:** `docs/01_GUIAS/`

---

## 📝 Convenciones de Nombres

### Prefijos:
- `test_*.py` - Scripts de prueba
- `crear_*.py` - Crear datos/objetos
- `agregar_*.py` - Agregar datos
- `diagnostico_*.py` - Diagnóstico
- `diagnosticar_*.py` - Diagnosticar
- `verificar_*.py` - Verificar
- `verificacion_*.py` - Verificación
- `setup_*.py` - Configuración
- `init_*.py` - Inicialización
- `update_*.py` - Actualización
- `demo_*.py` - Demostración
- `prueba_*.py` - Prueba

---

## 🆘 Ayuda

Si un script no funciona:

1. **Verifica que estés en la raíz del proyecto**
   ```bash
   cd C:\...\Digit_Sof_Nuevo
   ```

2. **Activa el entorno virtual**
   ```bash
   venv\Scripts\activate
   ```

3. **Verifica dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lee la documentación del script**
   - Abre el archivo con un editor
   - Lee los comentarios al inicio
   - Busca la función `main()` o las instrucciones

5. **Busca ayuda en la documentación**
   - `docs/01_GUIAS/` - Guías de uso
   - `docs/02_SOLUCIONES/` - Soluciones a problemas

---

## 🐍 Requisitos

La mayoría de scripts requieren:
- Python 3.8+
- Django instalado
- Base de datos configurada
- Entorno virtual activado

---

**Última actualización:** 2025-11-28
**Versión:** 1.0
**Total de scripts:** ~40-50 archivos Python

