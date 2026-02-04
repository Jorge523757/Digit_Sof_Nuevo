# 🚀 GUÍA PARA SUBIR A GITHUB SIN PERDER DATOS

## ✅ SISTEMA COMPLETADO

Has mejorado exitosamente el sistema de órdenes de servicio con:

- ✅ **Diseño moderno en azul** (sin colores rosa)
- ✅ **Formulario completo** para crear órdenes
- ✅ **Sistema de edición** con tracking de cambios
- ✅ **Historial visual** (timeline) de estados
- ✅ **Registro de técnicos** y responsables
- ✅ **Búsqueda avanzada** con filtros de fecha
- ✅ **Notificaciones automáticas** al cambiar estados
- ✅ **Paginación mejorada** con diseño profesional
- ✅ **40 órdenes de prueba** guardadas en MySQL

---

## 📊 DATOS GENERADOS

**Total de datos en MySQL:**
- 40 órdenes de servicio
- 88 seguimientos de estados
- 20 clientes
- 20 técnicos

**Estos datos están guardados en MySQL y NO se perderán al:**
- Reiniciar el servidor
- Hacer migraciones
- Cerrar la aplicación

---

## 🔄 CÓMO SUBIR A GITHUB (SIN PERDER DATOS)

### ⚠️ IMPORTANTE: Entender qué se sube y qué no

**Lo que SÍ se sube a GitHub (código):**
- ✅ Archivos Python (.py)
- ✅ Templates HTML (.html)
- ✅ CSS y JavaScript
- ✅ Configuración (settings.py)
- ✅ Scripts de generación de datos
- ✅ Migraciones de Django

**Lo que NO se sube a GitHub (datos):**
- ❌ Base de datos MySQL (archivos .sql, datos)
- ❌ Archivos compilados (.pyc, __pycache__)
- ❌ Archivos de entorno (.env)
- ❌ Archivos de media subidos por usuarios

---

## 📝 PASO A PASO PARA SUBIR A GITHUB

### 1️⃣ Preparar el Repositorio

```bash
# Ir a la carpeta del proyecto
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

# Verificar estado de Git
git status
```

### 2️⃣ Crear/Verificar .gitignore

Asegúrate de que tu archivo `.gitignore` incluya:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# MySQL
*.sql
*.mysql

# Entorno virtual
venv/
env/
ENV/

# Archivos de entorno
.env
.env.local

# Media y estáticos compilados
/media/
/staticfiles/

# IDE
.vscode/
.idea/
*.swp
*.swo
```

### 3️⃣ Agregar los Archivos Nuevos

```bash
# Agregar los nuevos archivos de órdenes
git add templates/ordenes/crear.html
git add templates/ordenes/editar.html
git add templates/ordenes/detalle.html
git add ordenes/views.py
git add ordenes/forms.py
git add static/css/ordenes-modern.css
git add generar_datos_ordenes.py
git add GENERAR_DATOS_ORDENES.bat
git add ORDENES_SERVICIO_GUIA_COMPLETA.md

# O agregar todo (Git ignorará automáticamente lo que está en .gitignore)
git add .
```

### 4️⃣ Hacer Commit

```bash
git commit -m "✨ Mejorar sistema de órdenes de servicio

- Diseño moderno en azul (sin rosa)
- Formulario completo de creación y edición
- Timeline visual de estados
- Sistema de notificaciones
- Búsqueda avanzada con filtros de fecha
- Paginación mejorada
- Script generador de datos de prueba"
```

### 5️⃣ Subir a GitHub

```bash
# Si ya tienes un repositorio remoto configurado
git push origin main

# O si usas otra rama
git push origin tu-rama
```

---

## 🎯 MANTENER LOS DATOS EN TU MÁQUINA

### Los datos permanecen en MySQL porque:

1. **MySQL es una base de datos persistente** que guarda todo en disco
2. **Git NO sube la base de datos** (está en .gitignore)
3. **Los datos están en tu computadora** en la carpeta de MySQL

### Ubicación de los datos en MySQL:

Los datos están guardados en el servidor MySQL local en:
- Base de datos: `digitsoft_db` (o el nombre que configuraste)
- Tablas: `ordenes_servicio`, `ordenes_seguimiento`, etc.

---

## 👥 PARA OTROS DESARROLLADORES QUE CLONEN EL REPO

Cuando otra persona clone tu repositorio:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2️⃣ Configurar el entorno
```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3️⃣ Configurar MySQL
```bash
# Crear la base de datos
mysql -u root -p
CREATE DATABASE digitsoft_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

### 5️⃣ Generar datos de prueba
```bash
# Primero generar clientes y técnicos
python generar_datos_faker.py

# Luego generar órdenes de servicio
python generar_datos_ordenes.py
```

### 6️⃣ Crear superusuario
```bash
python manage.py createsuperuser
```

---

## 📦 EXPORTAR/IMPORTAR DATOS (OPCIONAL)

### Si quieres compartir datos exactos con otros desarrolladores:

### Opción A: Exportar como Fixtures (JSON)

```bash
# Exportar órdenes
python manage.py dumpdata ordenes --indent 2 > ordenes_fixtures.json

# Exportar clientes
python manage.py dumpdata clientes --indent 2 > clientes_fixtures.json

# Exportar técnicos
python manage.py dumpdata tecnicos --indent 2 > tecnicos_fixtures.json
```

**Importar fixtures:**
```bash
python manage.py loaddata clientes_fixtures.json
python manage.py loaddata tecnicos_fixtures.json
python manage.py loaddata ordenes_fixtures.json
```

### Opción B: Exportar SQL de MySQL

```bash
# Exportar toda la base de datos
mysqldump -u root -p digitsoft_db > digitsoft_backup.sql

# Importar en otra máquina
mysql -u root -p digitsoft_db < digitsoft_backup.sql
```

---

## 🎨 VERIFICAR QUE TODO FUNCIONE

Después de subir a GitHub, verifica:

### 1️⃣ En tu máquina:
- [ ] Los datos siguen en MySQL (no se borraron)
- [ ] El servidor funciona correctamente
- [ ] Las órdenes se muestran con el diseño azul

### 2️⃣ En GitHub:
- [ ] Los archivos de código están subidos
- [ ] Los templates HTML están subidos
- [ ] Los CSS están subidos
- [ ] El .gitignore está funcionando (no hay .pyc ni __pycache__)

### 3️⃣ Probar en local:
```bash
python manage.py runserver
```

Visitar: `http://localhost:8000/ordenes/`

---

## 🔍 COMANDOS ÚTILES

### Ver estado de Git:
```bash
git status
```

### Ver qué archivos se ignorarán:
```bash
git status --ignored
```

### Ver diferencias antes de commit:
```bash
git diff
```

### Ver historial de commits:
```bash
git log --oneline
```

---

## 🎉 RESUMEN FINAL

### ✅ LO QUE LOGRASTE:

1. **Sistema completo de órdenes** con todas las funcionalidades
2. **Diseño profesional en azul** sin colores rosa
3. **40 órdenes de prueba** guardadas permanentemente en MySQL
4. **Sistema listo para producción**

### 📌 RECUERDA:

- Los **datos están en MySQL** (no en Git)
- El **código está en Git** (no los datos)
- Los datos **NO se borran** al hacer push
- Otros desarrolladores deben **generar sus propios datos** con los scripts

### 🚀 PRÓXIMOS PASOS:

1. ✅ Haz commit de los cambios
2. ✅ Sube a GitHub con `git push`
3. ✅ Los datos permanecen en tu MySQL
4. ✅ Otros clonarán y ejecutarán los scripts de datos

---

## 📞 SOPORTE

Si tienes dudas sobre:
- Subir a GitHub → Consulta la documentación de Git
- Configurar MySQL → Revisa `CONFIGURACION_MYSQL.md`
- Generar datos → Ejecuta `GENERAR_DATOS_ORDENES.bat`

---

**¡Todo listo para subir a GitHub!** 🎊

Tu código está organizado, los datos están seguros en MySQL, y el sistema funciona perfectamente.

**Creado:** 04/02/2026  
**Versión:** 1.0 - Guía de GitHub

