# 🚀 GUÍA RÁPIDA: SUBIR CAMBIOS A MAIN SIN BORRAR DATOS

## 📋 RESUMEN

Tienes cambios en la rama `jorge-dev` y quieres subirlos a `main` manteniendo tus datos de MySQL intactos.

---

## ⚡ OPCIÓN 1: USAR EL SCRIPT AUTOMÁTICO (RECOMENDADO)

### Paso 1: Ejecutar el script
```
Doble click en: SUBIR_A_MAIN.bat
```

### Paso 2: Seguir las instrucciones
El script te guiará automáticamente:
1. Hace commit de cambios en jorge-dev
2. Sube jorge-dev a GitHub
3. Te pregunta si quieres fusionar con main
4. Si dices SÍ, fusiona y sube main
5. Vuelve a jorge-dev automáticamente

### Paso 3: ¡Listo!
✅ Tus cambios están en GitHub (main y jorge-dev)
✅ Los datos de MySQL siguen en tu PC

---

## 🔧 OPCIÓN 2: MANUAL CON COMANDOS

### Paso 1: Verificar estado
```bash
git status
```

### Paso 2: Agregar archivos
```bash
git add -A
```

### Paso 3: Commit en jorge-dev
```bash
git commit -m "✨ Sistema completo de órdenes de servicio mejorado"
```

### Paso 4: Subir jorge-dev
```bash
git push origin jorge-dev
```

### Paso 5: Cambiar a main
```bash
git checkout main
```

### Paso 6: Actualizar main
```bash
git pull origin main
```

### Paso 7: Fusionar jorge-dev con main
```bash
git merge jorge-dev
```

### Paso 8: Subir main
```bash
git push origin main
```

### Paso 9: Volver a jorge-dev
```bash
git checkout jorge-dev
```

---

## ❓ PREGUNTAS FRECUENTES

### ¿Se borrarán mis datos de MySQL?
**NO.** Los datos están en MySQL local y NO se suben a GitHub.

### ¿Qué se sube a GitHub?
**Solo el código:**
- Archivos .py (Python)
- Archivos .html (Templates)
- Archivos .css (Estilos)
- Archivos .js (JavaScript)
- Archivos .md (Documentación)
- Scripts .bat

**NO se sube:**
- Base de datos MySQL
- Archivos .pyc
- Carpeta __pycache__
- db.sqlite3

### ¿Los datos estarán en GitHub para otros?
**NO.** Otros desarrolladores tendrán que:
1. Clonar el repositorio
2. Configurar su propia MySQL
3. Ejecutar: `python generar_datos_ordenes.py`

### ¿Puedo seguir trabajando después de subir?
**SÍ.** Continúa trabajando normal en jorge-dev.

### ¿Qué pasa si hay conflictos?
Si hay conflictos al fusionar:
1. Git te dirá qué archivos tienen conflicto
2. Ábrelos y busca las marcas: `<<<<<<`, `======`, `>>>>>>`
3. Decide qué código mantener
4. Elimina las marcas de conflicto
5. Haz commit de la resolución

---

## ✅ VERIFICACIÓN POST-SUBIDA

### 1. Verifica en GitHub
Ve a: `https://github.com/tu-usuario/tu-repo`

Deberías ver:
- Rama main actualizada
- Rama jorge-dev actualizada
- Los commits recientes
- Los archivos nuevos

### 2. Verifica en tu PC
```bash
# Ver en qué rama estás
git branch

# Ver últimos commits
git log --oneline -5

# Ver estado
git status
```

### 3. Verifica tus datos
```bash
# Iniciar servidor
python manage.py runserver

# Visitar
http://localhost:8000/ordenes/
```

Deberías ver tus 40 órdenes de servicio intactas.

---

## 🎯 FLUJO RECOMENDADO DE TRABAJO

### Desarrollo diario:
```
1. Trabajar en jorge-dev
2. Hacer commits frecuentes
3. Push a jorge-dev regularmente
4. Fusionar a main solo cuando esté estable
```

### Comandos diarios:
```bash
# Al empezar el día
git pull origin jorge-dev

# Mientras trabajas (cada pocas horas)
git add -A
git commit -m "Descripción del cambio"
git push origin jorge-dev

# Al terminar una feature completa
git checkout main
git merge jorge-dev
git push origin main
git checkout jorge-dev
```

---

## 🛡️ PROTECCIÓN DE DATOS

### Archivos que protegen tus datos:

**`.gitignore`** ya incluye:
```
# Base de datos
db.sqlite3
*.sql

# Python compilado
__pycache__/
*.pyc

# Entorno
.env
venv/
```

### MySQL está protegido porque:
1. ✅ Los datos están en tu PC (no en la carpeta del proyecto)
2. ✅ MySQL guarda en su propia ubicación (C:\ProgramData\MySQL)
3. ✅ Git NO puede acceder a esos datos
4. ✅ .gitignore bloquea archivos .sql

---

## 📊 RESUMEN DE LO QUE PASARÁ

### ANTES:
```
GitHub:
├─ main (versión antigua)
└─ jorge-dev (versión antigua)

Tu PC:
├─ Código (rama jorge-dev con cambios nuevos)
└─ MySQL (40 órdenes de servicio)
```

### DESPUÉS:
```
GitHub:
├─ main (versión nueva con órdenes mejoradas)
└─ jorge-dev (versión nueva con órdenes mejoradas)

Tu PC:
├─ Código (rama jorge-dev, sincronizado con GitHub)
└─ MySQL (40 órdenes de servicio - INTACTAS)
```

---

## 🎉 CONCLUSIÓN

**Usa el script SUBIR_A_MAIN.bat para hacerlo fácil y seguro.**

El script:
- ✅ Hace todo automáticamente
- ✅ Te pregunta antes de fusionar
- ✅ No toca tus datos de MySQL
- ✅ Maneja errores automáticamente
- ✅ Te devuelve a jorge-dev al final

**Tus datos de MySQL están seguros y NO se borrarán.**

---

**Fecha:** 04/02/2026  
**Versión:** 1.0 - Guía de Subida a Main

