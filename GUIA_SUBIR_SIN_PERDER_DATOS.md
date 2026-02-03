# 🔒 GUÍA: SUBIR A GIT CON BASE DE DATOS INCLUIDA

## ✅ NUEVO ENFOQUE: COMPARTIR DATOS CON QUIEN CLONE

La base de datos `db.sqlite3` **SÍ se subirá a GitHub** para que quien clone el repositorio tenga los 220 registros listos para usar.

---

## 🎯 VENTAJAS DE SUBIR LA BASE DE DATOS

### ✅ Para quien clone el repositorio:

- ✅ **Datos precargados**: 220 registros listos
- ✅ **No necesita seed**: `python manage.py seed_all_empty` no es necesario
- ✅ **Uso inmediato**: Solo clonar y ejecutar `python manage.py runserver`
- ✅ **Mismo contenido**: Todos trabajan con los mismos datos de prueba

### ✅ Datos incluidos:

- 20 Clientes
- 20 Órdenes de Servicio
- 20 Productos
- 20 Categorías
- 20 Proveedores
- 20 Técnicos
- 20 Equipos
- 20 Compras
- 20 Garantías
- 20 Facturas

**Total: 220 registros de datos vacíos listos para usar**

---

## 🚀 CÓMO SUBIR TODO (INCLUYENDO DB)

### Opción 1: Script Automático (RECOMENDADO)

```
Doble clic en: SUBIR_CON_BASE_DATOS.bat
```

El script hará:
1. ✅ Verificar que db.sqlite3 existe
2. ✅ Mostrar tamaño del archivo
3. ✅ Agregar TODOS los archivos (incluyendo db.sqlite3)
4. ✅ Hacer commit descriptivo
5. ✅ Subir a rama jorge-dev

### Opción 2: Manual (Línea de Comandos)

```bash
# 1. Ir al proyecto
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

# 2. Verificar que db.sqlite3 existe
dir db.sqlite3

# 3. Agregar TODO (incluyendo db.sqlite3)
git add .
git add db.sqlite3 -f

# 4. Hacer commit
git commit -m "feat: Sistema completo con base de datos incluida (220 registros)"

# 5. Subir a tu rama
git push origin jorge-dev
```

---

## 📊 QUÉ SE INCLUYE EN EL COMMIT

### ✅ Código fuente:
- `ordenes/views.py` (filtros, APIs)
- `ordenes/urls.py` (rutas)
- `config/settings.py` (SQLite)

### ✅ Templates:
- `templates/ordenes/lista.html` (diseño mejorado)

### ✅ Estilos:
- `static/css/ordenes-modern.css` (sin rosa)
- `static/css/autocomplete.css`

### ✅ JavaScript:
- `static/js/autocomplete-ordenes.js`

### ✅ Base de Datos:
- `db.sqlite3` (220 registros) ← **NUEVO**

### ✅ Documentación:
- `CONFIGURACION_SQLITE.md`
- `ORDENES_MEJORADAS_COMPLETO.md`
- `ORDENES_SIN_ROSA_MEJORADO.md`
- `FILTROS_PAGINACION_AUTOCOMPLETADO.md`

---

## 🔄 CLONAR EN OTRA COMPUTADORA

Ahora, cuando alguien clone el repositorio:

```bash
# 1. Clonar
git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
cd Digit_Sof_Nuevo

# 2. Cambiar a tu rama
git checkout jorge-dev

# 3. La base de datos YA ESTÁ INCLUIDA
# No es necesario ejecutar migrate ni seed

# 4. Iniciar servidor directamente
python manage.py runserver

# 5. Abrir navegador
# http://127.0.0.1:8000
# Los 220 registros ya están ahí!
```

---

## ⚠️ CONSIDERACIONES

### Tamaño del Archivo

GitHub tiene un límite de **100MB por archivo**. 

Si tu `db.sqlite3` es menor a 100MB, no hay problema.

**Verificar tamaño:**
```bash
dir db.sqlite3
# o
ls -lh db.sqlite3
```

### Si el archivo es muy grande

Si `db.sqlite3` supera 100MB:

**Opción A: Git LFS** (Large File Storage)
```bash
git lfs install
git lfs track "*.sqlite3"
git add .gitattributes
git add db.sqlite3
git commit -m "Add database with Git LFS"
git push origin jorge-dev
```

**Opción B: Comprimir**
```bash
# Exportar a JSON (más compacto)
python manage.py dumpdata > datos.json

# Subir el JSON en lugar de db.sqlite3
git add datos.json
git commit -m "Add data as JSON"
git push origin jorge-dev

# Quien clone restaura con:
python manage.py loaddata datos.json
```

**Opción C: No subir la DB**
Si prefieres no subir la DB, revierte los cambios:
```bash
# Descomentar en .gitignore
# db.sqlite3
```

---

## 🎯 PASOS PARA SUBIR SIN PERDER DATOS

### Opción 1: Usar el Script Automático (RECOMENDADO)

```
1. Doble clic en: SUBIR_A_GIT_SIN_PERDER_DATOS.bat
2. Seguir las instrucciones en pantalla
3. ¡Listo!
```

### Opción 2: Hacer Respaldo Primero (MÁS SEGURO)

```
1. Doble clic en: RESPALDAR_BASE_DATOS.bat
   (Crea una copia de seguridad de db.sqlite3)

2. Luego doble clic en: SUBIR_A_GIT_SIN_PERDER_DATOS.bat
   (Sube los cambios a GitHub)
```

### Opción 3: Manual (Línea de Comandos)

```bash
# 1. Ir al proyecto
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

# 2. Verificar archivos que se subirán
git status

# 3. Verificar que db.sqlite3 está ignorado
git check-ignore db.sqlite3
# Si muestra "db.sqlite3", está ignorado ✓

# 4. Agregar cambios
git add .

# 5. Hacer commit
git commit -m "Mejoras en Órdenes de Servicio - Diseño sin rosa, paginación mejorada"

# 6. Subir a tu rama
git push origin jorge-dev
```

---

## 🔍 VERIFICACIÓN: ¿Se Subirá la Base de Datos?

**SÍ**, ahora la base de datos SÍ se subirá.

### Verificar .gitignore

Abre el archivo `.gitignore` y verás que `db.sqlite3` está **comentado**:

```
# db.sqlite3  ← Comentado, ahora SÍ se sube
```

### Ver qué se va a subir

```bash
git status

# Deberías ver:
# - Archivos .py modificados
# - Archivos .html modificados
# - Archivos .css nuevos
# - db.sqlite3 (NUEVO - se incluirá)
```

### Verificar tamaño

```bash
# Ver tamaño del archivo
dir db.sqlite3

# Debe ser menor a 100MB para GitHub
```

---

## 💾 HACER RESPALDO (OPCIONAL)

Aunque ahora subes la DB a Git, puedes hacer un respaldo local:

### Opción A: Script Automático

```
Doble clic en: RESPALDAR_BASE_DATOS.bat
```

Esto creará:
```
respaldos/
  └── db_backup_20260203_145530.sqlite3
```

---

## 📤 SUBIR A GITHUB

### Con el Script (RECOMENDADO):

```
Doble clic en: SUBIR_CON_BASE_DATOS.bat
```

### Manual:

```bash
# 1. Ver cambios
git status

# 2. Agregar TODO (incluyendo db.sqlite3)
git add .
git add db.sqlite3 -f

# 3. Commit con mensaje descriptivo
git commit -m "feat: Sistema completo con datos de prueba incluidos

- Base de datos SQLite con 220 registros
- Mejoras en Órdenes de Servicio
- Diseño sin rosa, paleta azul/verde/naranja
- Paginación moderna con iconos
- Sistema de registro de estados
- Filtros avanzados
- Autocompletado de clientes y técnicos"

# 4. Subir a tu rama
git push origin jorge-dev
```

---

## ✅ DESPUÉS DE SUBIR

### Verificar en GitHub

1. Ve a: https://github.com/Jorge523757/Digit_Sof_Nuevo
2. Cambia a la rama `jorge-dev`
3. Verifica que **SÍ aparezca** el archivo `db.sqlite3`
4. Verifica el tamaño del archivo

### En Tu Computadora

Después de subir, todo sigue igual:

```
✓ db.sqlite3 (LOCAL y en GitHub)
✓ 220 registros preservados
✓ Base de datos funcional
```

---

## 🔄 EN OTRA COMPUTADORA

Si clonas el repositorio en otra computadora:

```bash
# 1. Clonar
git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
cd Digit_Sof_Nuevo

# 2. Cambiar a tu rama
git checkout jorge-dev

# 3. La base de datos NO estará, así que:
python manage.py migrate

# 4. Crear datos vacíos (opcional)
python manage.py seed_all_empty --count 20

# 5. O restaurar desde respaldo
# Si tienes el respaldo, cópialo como db.sqlite3
```

---

## 🎯 RESUMEN

### ✅ LO QUE SE SUBE A GIT:

- Código fuente (.py)
- Templates (.html)
- Estilos (.css)
- Configuraciones (.txt, .md)
- Scripts (.bat)
- Documentación (.md)
- **Base de datos (db.sqlite3)** ← AHORA SÍ SE SUBE

### ❌ LO QUE NO SE SUBE:

- Archivos temporales (__pycache__)
- Archivos de entorno (.env)
- Media files (/media)
- Static files (/staticfiles)
- Logs (*.log)

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Error: "File size exceeds GitHub's 100MB limit"

Si db.sqlite3 es muy grande:

```bash
# Opción 1: Usar Git LFS
git lfs install
git lfs track "*.sqlite3"
git add .gitattributes
git commit -m "Add Git LFS support"

# Opción 2: Exportar a JSON
python manage.py dumpdata > datos.json
git add datos.json
git commit -m "Add data as JSON"

# Opción 3: Volver a NO subir la DB
# Descomentar en .gitignore: db.sqlite3
```

### Error: "db.sqlite3 not found"

```bash
# Verificar que existe
dir db.sqlite3

# Si no existe, crear una nueva
python manage.py migrate
python manage.py seed_all_empty --count 20
```

### Error: "Permission denied"

```bash
# Verificar que no tengas el servidor corriendo
# Detén el servidor Django (Ctrl+C)

# Luego intenta de nuevo
git push origin jorge-dev
```

### Error: "Conflicto de fusión"

```bash
# Traer cambios remotos
git pull origin jorge-dev

# Resolver conflictos manualmente
# Luego:
git add .
git commit -m "Resolver conflictos"
git push origin jorge-dev
```

---

## 📋 CHECKLIST ANTES DE SUBIR

- [ ] ✅ db.sqlite3 existe y tiene datos
- [ ] ✅ db.sqlite3 NO está en .gitignore (comentado)
- [ ] ✅ Servidor Django detenido
- [ ] ✅ Git status revisado
- [ ] ✅ Tamaño de db.sqlite3 menor a 100MB
- [ ] ✅ Mensaje de commit preparado
- [ ] ✅ Conexión a internet activa

---

## 🎉 RESULTADO ESPERADO

```
Archivos locales:
├── db.sqlite3 ✓ (LOCAL y SE SUBE)
├── ordenes-modern.css ✓ (SE SUBE)
├── lista.html ✓ (SE SUBE)
├── views.py ✓ (SE SUBE)
└── ...

GitHub (rama jorge-dev):
├── db.sqlite3 ✓ (CON 220 REGISTROS)
├── ordenes-modern.css ✓
├── lista.html ✓
├── views.py ✓
└── ...

Quien clone el repositorio:
✓ Obtiene db.sqlite3 automáticamente
✓ 220 registros incluidos
✓ No necesita ejecutar seed
✓ Solo ejecuta: python manage.py runserver
```

---

**Fecha:** 3 de febrero de 2026  
**Estado:** ✅ Guía actualizada  
**Base de datos:** SÍ se sube a Git  
**Ventaja:** Quien clone tiene datos listos

