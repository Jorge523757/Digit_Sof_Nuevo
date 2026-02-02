# 🗄️ DIGITSOFT - CONFIGURACIÓN MYSQL

## ✅ ESTADO ACTUAL

El proyecto ha sido configurado para usar **MySQL** en lugar de SQLite.

---

## 📋 PASOS PARA CONFIGURAR MYSQL

### **PASO 1: Instalar MySQL** (Si no lo tienes)

1. Descarga **MySQL Community Server**: https://dev.mysql.com/downloads/mysql/
2. Instala MySQL siguiendo el wizard
3. **Anota la password de root** que configures

### **PASO 2: Verificar que MySQL esté corriendo**

1. Presiona `Win + R` y escribe: `services.msc`
2. Busca el servicio **MySQL80** (o similar)
3. Verifica que el estado sea **"En ejecución"**
4. Si no está corriendo, haz clic derecho → **Iniciar**

### **PASO 3: Instalar mysqlclient**

Ejecuta el archivo por lotes:
```cmd
INSTALAR_MYSQLCLIENT.bat
```

O manualmente:
```cmd
pip install mysqlclient
```

**⚠️ Posibles errores:**
- Si falla la instalación, necesitas **Visual C++ Build Tools**
- Descarga desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- O descarga el wheel precompilado desde: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

### **PASO 4: Crear la base de datos**

Ejecuta el archivo por lotes:
```cmd
CREAR_DATABASE_MYSQL.bat
```

O manualmente:
```cmd
mysql -u root -p < crear_database_mysql.sql
```

Te pedirá la password de root de MySQL.

### **PASO 5: Ejecutar migraciones**

Ejecuta el archivo por lotes:
```cmd
MIGRAR_MYSQL.bat
```

O manualmente:
```cmd
python manage.py migrate
```

### **PASO 6: Crear superusuario**

```cmd
python manage.py createsuperuser
```

### **PASO 7: Iniciar el servidor**

```cmd
python manage.py runserver
```

---

## 📊 DATOS DE CONEXIÓN MYSQL

| Campo | Valor |
|-------|-------|
| **Base de datos** | digitsoft_db |
| **Usuario** | digitsoft_user |
| **Password** | digitsoft2024 |
| **Host** | localhost |
| **Puerto** | 3306 |
| **Charset** | utf8mb4 |

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### ❌ Error: "mysqlclient install failed"

**Causa:** Faltan herramientas de compilación de C++

**Solución 1:** Instalar Visual C++ Build Tools
- https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Selecciona "Herramientas de compilación de C++" durante la instalación

**Solución 2:** Descargar wheel precompilado
1. Ve a: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
2. Descarga el archivo .whl que coincida con tu Python (ej: `mysqlclient-2.2.0-cp311-cp311-win_amd64.whl`)
3. Instala: `pip install ruta\al\archivo.whl`

### ❌ Error: "Access denied for user 'digitsoft_user'@'localhost'"

**Causa:** La base de datos no fue creada correctamente o el usuario no existe

**Solución:**
1. Ejecuta nuevamente: `CREAR_DATABASE_MYSQL.bat`
2. Verifica que ingresaste correctamente la password de root

### ❌ Error: "Can't connect to MySQL server on 'localhost'"

**Causa:** MySQL no está corriendo

**Solución:**
1. Abre `services.msc` (Win + R)
2. Busca **MySQL80**
3. Haz clic derecho → **Iniciar**

### ❌ Error: "Unknown database 'digitsoft_db'"

**Causa:** La base de datos no fue creada

**Solución:**
Ejecuta: `CREAR_DATABASE_MYSQL.bat`

---

## 📁 ARCHIVOS IMPORTANTES

| Archivo | Descripción |
|---------|-------------|
| `crear_database_mysql.sql` | Script SQL para crear la base de datos |
| `CREAR_DATABASE_MYSQL.bat` | Ejecuta el script SQL automáticamente |
| `INSTALAR_MYSQLCLIENT.bat` | Instala el conector MySQL para Python |
| `MIGRAR_MYSQL.bat` | Ejecuta las migraciones en MySQL |
| `GUIA_MYSQL.bat` | Muestra esta guía en la terminal |
| `config/settings.py` | Configuración de Django (ya configurado para MySQL) |
| `requirements.txt` | Dependencias del proyecto |

---

## 🎯 ORDEN RECOMENDADO

```
1. INSTALAR_MYSQLCLIENT.bat     ← Instalar conector
2. CREAR_DATABASE_MYSQL.bat     ← Crear base de datos
3. MIGRAR_MYSQL.bat             ← Ejecutar migraciones
4. python manage.py createsuperuser ← Crear admin
5. python manage.py runserver   ← Iniciar servidor
```

---

## 💡 NOTAS IMPORTANTES

- ✅ El proyecto ahora usa **MySQL** por defecto
- ✅ SQLite ya **NO** se usa
- ✅ Todos los datos se guardarán en MySQL
- ⚠️ Asegúrate de que MySQL esté corriendo antes de iniciar Django
- ⚠️ Si cambias de computadora, debes configurar MySQL nuevamente

---

## 🔄 VOLVER A SQLITE (Si lo necesitas)

Si quieres volver a usar SQLite en lugar de MySQL:

1. Abre `config/settings.py`
2. Busca la sección `DATABASES`
3. Cambia a:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

**🎉 ¡Listo! Tu proyecto ahora usa MySQL.**

