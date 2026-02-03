# 🔧 SOLUCIÓN: Error de Acceso a MySQL

## ❌ PROBLEMA

```
django.db.utils.OperationalError: (1045, "Access denied for user 'digitsoft_user'@'localhost' (using password: YES)")
```

**Causa:** El usuario 'digitsoft_user' no tiene permisos o no existe en MySQL.

---

## ✅ SOLUCIONES (3 OPCIONES)

### 🎯 OPCIÓN 1: Recrear Usuario en MySQL (RECOMENDADO)

#### Paso 1: Abrir MySQL como Administrador

**Opción A - MySQL Command Line:**
```bash
mysql -u root -p
```
Ingresa tu contraseña de root cuando te la pida.

**Opción B - MySQL Workbench:**
1. Abre MySQL Workbench
2. Conecta con usuario `root`
3. Abre una nueva pestaña de Query

#### Paso 2: Ejecutar el Script SQL

Copia y pega este código en MySQL:

```sql
-- Eliminar usuario si existe
DROP USER IF EXISTS 'digitsoft_user'@'localhost';

-- Crear usuario
CREATE USER 'digitsoft_user'@'localhost' IDENTIFIED BY 'digitsoft2024';

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS digitsoft_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Dar permisos
GRANT ALL PRIVILEGES ON digitsoft_db.* TO 'digitsoft_user'@'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;

-- Verificar
SELECT User, Host FROM mysql.user WHERE User = 'digitsoft_user';
SHOW GRANTS FOR 'digitsoft_user'@'localhost';
```

O ejecuta el archivo directamente:
```bash
mysql -u root -p < crear_usuario_mysql.sql
```

#### Paso 3: Aplicar Migraciones

```bash
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

### 🎯 OPCIÓN 2: Usar Usuario Root Temporalmente

Si no puedes crear el usuario, usa root temporalmente.

#### Paso 1: Editar settings.py

Abre `config/settings.py` y busca la sección DATABASES:

**ANTES:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digitsoft_db',
        'USER': 'digitsoft_user',
        'PASSWORD': 'digitsoft2024',
        'HOST': 'localhost',
        'PORT': '3306',
        ...
    }
}
```

**DESPUÉS:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digitsoft_db',
        'USER': 'root',
        'PASSWORD': 'TU_CONTRASEÑA_ROOT',  # Cambia esto
        'HOST': 'localhost',
        'PORT': '3306',
        ...
    }
}
```

#### Paso 2: Crear Base de Datos (si no existe)

```bash
mysql -u root -p
```

```sql
CREATE DATABASE IF NOT EXISTS digitsoft_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

#### Paso 3: Ejecutar Django

```bash
python manage.py migrate
python manage.py runserver
```

---

### 🎯 OPCIÓN 3: Cambiar a SQLite (Temporal)

Si tienes problemas con MySQL, usa SQLite temporalmente.

#### Paso 1: Editar settings.py

Abre `config/settings.py` y reemplaza la sección DATABASES:

**ANTES:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digitsoft_db',
        'USER': 'digitsoft_user',
        'PASSWORD': 'digitsoft2024',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

**DESPUÉS:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Paso 2: Ejecutar Migraciones

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🚀 SCRIPTS AUTOMÁTICOS

### Script 1: Ejecutar SQL Automáticamente

```bash
# En PowerShell
mysql -u root -p < crear_usuario_mysql.sql
```

### Script 2: Usar el .BAT

```bash
# Doble clic en:
SOLUCIONAR_MYSQL.bat
```

---

## 🔍 VERIFICACIÓN

Para verificar que el usuario fue creado correctamente:

```bash
mysql -u root -p
```

```sql
-- Ver usuarios
SELECT User, Host FROM mysql.user;

-- Ver privilegios del usuario
SHOW GRANTS FOR 'digitsoft_user'@'localhost';

-- Probar conexión
EXIT;
mysql -u digitsoft_user -p digitsoft_db
```

Si puedes conectarte con el último comando, ¡está funcionando!

---

## 📋 CHECKLIST DE SOLUCIÓN

### Opción 1 - MySQL (Recomendado)
- [ ] Conectar a MySQL como root
- [ ] Ejecutar script SQL (crear_usuario_mysql.sql)
- [ ] Verificar que el usuario existe
- [ ] Ejecutar `python manage.py migrate`
- [ ] Ejecutar `python manage.py createsuperuser`
- [ ] Ejecutar `python manage.py runserver`
- [ ] Verificar que no hay errores

### Opción 2 - Root Temporal
- [ ] Editar settings.py
- [ ] Cambiar USER a 'root'
- [ ] Cambiar PASSWORD a tu contraseña de root
- [ ] Crear base de datos si no existe
- [ ] Ejecutar `python manage.py migrate`
- [ ] Ejecutar `python manage.py runserver`

### Opción 3 - SQLite Temporal
- [ ] Editar settings.py
- [ ] Cambiar ENGINE a 'django.db.backends.sqlite3'
- [ ] Cambiar NAME a BASE_DIR / 'db.sqlite3'
- [ ] Eliminar USER, PASSWORD, HOST, PORT, OPTIONS
- [ ] Ejecutar `python manage.py migrate`
- [ ] Ejecutar `python manage.py createsuperuser`
- [ ] Ejecutar `python manage.py runserver`

---

## 🐛 PROBLEMAS COMUNES

### Error: "Access denied for root"
**Solución:** Verifica que estás usando la contraseña correcta de root.

### Error: "Can't connect to MySQL server"
**Solución:** 
1. Verifica que MySQL esté corriendo
2. En Windows: Services → MySQL → Start
3. O ejecuta: `net start MySQL80` (o la versión que tengas)

### Error: "Database doesn't exist"
**Solución:**
```sql
CREATE DATABASE digitsoft_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Error: "Table doesn't exist" después de cambiar
**Solución:**
```bash
python manage.py migrate
```

---

## 💡 RECOMENDACIÓN FINAL

**Para desarrollo rápido:** Usa SQLite (Opción 3)
- No requiere configuración
- Archivo único
- Fácil de respaldar

**Para producción:** Usa MySQL (Opción 1)
- Mejor rendimiento
- Más robusto
- Mejor para múltiples usuarios

---

## 📞 SIGUIENTE PASO

Elige una opción y sigue los pasos. Si sigues teniendo problemas, ejecuta:

```bash
# Ver detalles del error
python manage.py check --deploy
```

Y comparte el mensaje de error completo.

---

**Fecha:** 3 de febrero de 2026  
**Estado:** Solución lista para aplicar  
**Tiempo estimado:** 5-10 minutos

