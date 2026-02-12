# 🔧 COMANDOS GIT ÚTILES - DIGIT SOFT

## 📦 CONFIGURACIÓN INICIAL

### Configurar Git (primera vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Verificar configuración
```bash
git config --list
```

---

## 🚀 SUBIR EL PROYECTO A GITHUB

### 1. Crear repositorio en GitHub
- Ir a: https://github.com/new
- Nombre: `digit-soft`
- Descripción: "Sistema de Gestión Empresarial"
- Privado o Público (recomendado: Privado)
- NO marcar "Initialize with README"
- Crear repositorio

### 2. Inicializar Git local
```bash
cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
git init
```

### 3. Agregar archivos
```bash
# Agregar todos los archivos
git add .

# O agregar específicos
git add README.md
git add requirements.txt
```

### 4. Primer commit
```bash
git commit -m "Initial commit: Sistema DIGIT SOFT completo"
```

### 5. Conectar con GitHub
```bash
# Reemplazar con tu URL de GitHub
git remote add origin https://github.com/TU-USUARIO/digit-soft.git
```

### 6. Subir al repositorio
```bash
# Primera vez
git push -u origin main

# O si usa master
git push -u origin master
```

---

## 📝 COMANDOS DIARIOS

### Ver estado
```bash
git status
```

### Ver cambios
```bash
git diff
```

### Agregar archivos modificados
```bash
# Todos
git add .

# Específicos
git add archivo.py
```

### Hacer commit
```bash
git commit -m "Descripción de cambios"
```

### Subir cambios
```bash
git push
```

### Bajar cambios
```bash
git pull
```

---

## 🌿 RAMAS (BRANCHES)

### Crear rama
```bash
git branch nombre-rama
```

### Cambiar de rama
```bash
git checkout nombre-rama
```

### Crear y cambiar
```bash
git checkout -b nueva-rama
```

### Ver ramas
```bash
git branch
```

### Fusionar rama
```bash
git checkout main
git merge nombre-rama
```

### Eliminar rama
```bash
git branch -d nombre-rama
```

---

## 🔄 CLONAR Y ACTUALIZAR

### Clonar repositorio
```bash
git clone https://github.com/TU-USUARIO/digit-soft.git
cd digit-soft
```

### Actualizar desde GitHub
```bash
git pull origin main
```

### Ver repositorio remoto
```bash
git remote -v
```

---

## 📜 HISTORIAL

### Ver commits
```bash
git log
```

### Ver commits resumidos
```bash
git log --oneline
```

### Ver cambios de un commit
```bash
git show COMMIT_HASH
```

---

## ⏪ DESHACER CAMBIOS

### Deshacer cambios no guardados
```bash
git checkout -- archivo.py
```

### Deshacer último commit (conservar cambios)
```bash
git reset --soft HEAD~1
```

### Deshacer último commit (eliminar cambios)
```bash
git reset --hard HEAD~1
```

### Revertir commit específico
```bash
git revert COMMIT_HASH
```

---

## 🏷️ TAGS (VERSIONES)

### Crear tag
```bash
git tag -a v1.0.0 -m "Versión 1.0.0"
```

### Ver tags
```bash
git tag
```

### Subir tags
```bash
git push origin --tags
```

### Eliminar tag
```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

---

## 🔍 BÚSQUEDA

### Buscar en archivos
```bash
git grep "texto a buscar"
```

### Buscar en commits
```bash
git log --grep="texto"
```

---

## 🧹 LIMPIEZA

### Eliminar archivos no rastreados
```bash
# Ver qué se eliminará
git clean -n

# Eliminar
git clean -f
```

### Eliminar directorios no rastreados
```bash
git clean -fd
```

---

## 📦 ARCHIVOS ESPECÍFICOS DE DIGIT SOFT

### Archivos que DEBEN estar en Git:
```
✅ *.py (todos los archivos Python)
✅ *.html (templates)
✅ *.css, *.js (archivos estáticos)
✅ requirements.txt
✅ README.md
✅ manage.py
✅ .gitignore
✅ *.bat (scripts)
✅ *.sh (scripts Linux)
✅ *.md (documentación)
```

### Archivos que NO deben estar en Git:
```
❌ db.sqlite3 (base de datos)
❌ venv/ (entorno virtual)
❌ __pycache__/ (cache Python)
❌ *.pyc (bytecode)
❌ .env (variables de entorno)
❌ media/ (archivos subidos)
❌ staticfiles/ (archivos estáticos recolectados)
```

Estos están en `.gitignore` y se ignoran automáticamente.

---

## 🔐 CREDENCIALES Y SEGURIDAD

### Nunca subir:
```
❌ Contraseñas
❌ API Keys
❌ Tokens de acceso
❌ Archivos .env
❌ Credenciales de base de datos
```

### Si subiste algo sensible por error:

1. **Eliminar del historial:**
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch ruta/archivo" \
  --prune-empty --tag-name-filter cat -- --all

git push origin --force --all
```

2. **Cambiar credenciales inmediatamente**

---

## 📋 FLUJO DE TRABAJO RECOMENDADO

### 1. Antes de empezar a trabajar:
```bash
git pull
```

### 2. Hacer cambios en el código
```python
# Editar archivos...
```

### 3. Ver qué cambió:
```bash
git status
git diff
```

### 4. Agregar cambios:
```bash
git add .
```

### 5. Hacer commit:
```bash
git commit -m "Descripción clara de cambios"
```

### 6. Subir:
```bash
git push
```

---

## 🆘 PROBLEMAS COMUNES

### "Permission denied (publickey)"

**Solución:** Configurar SSH o usar HTTPS

**HTTPS:**
```bash
git remote set-url origin https://github.com/TU-USUARIO/digit-soft.git
```

### "Updates were rejected"

**Solución:**
```bash
git pull --rebase origin main
git push
```

### "Merge conflict"

**Solución:**
1. Abrir archivos en conflicto
2. Buscar `<<<<<<<`, `=======`, `>>>>>>>`
3. Resolver manualmente
4. Guardar
```bash
git add archivo-resuelto.py
git commit -m "Resuelto conflicto"
git push
```

### "Detached HEAD"

**Solución:**
```bash
git checkout main
```

---

## 🎯 MEJORES PRÁCTICAS

### Commits

✅ **HACER:**
- Commits pequeños y frecuentes
- Mensajes descriptivos
- Un cambio lógico por commit

❌ **NO HACER:**
- Commits gigantes
- Mensajes vagos ("fix", "update")
- Múltiples cambios no relacionados

### Mensajes de Commit

**Buenos ejemplos:**
```
✅ "Agregar módulo de reportes de daños"
✅ "Corregir error en login de usuarios"
✅ "Implementar sistema de notificaciones por email"
✅ "Actualizar documentación de instalación"
```

**Malos ejemplos:**
```
❌ "cambios"
❌ "fix"
❌ "update"
❌ "asdfasdf"
```

### Formato recomendado:
```
Tipo: Descripción corta

Descripción más detallada si es necesario.

- Cambio 1
- Cambio 2
- Cambio 3
```

**Tipos:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `style:` Formato, espacios
- `refactor:` Refactorización
- `test:` Pruebas
- `chore:` Tareas de mantenimiento

---

## 📊 VERIFICAR ANTES DE PUSH

```bash
# 1. Verificar que no haya errores
python manage.py check

# 2. Ver qué se va a subir
git status

# 3. Ver cambios
git diff

# 4. Probar el sistema
python manage.py runserver

# 5. Si todo OK, push
git push
```

---

## 🎓 RECURSOS ADICIONALES

### Documentación oficial:
- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com

### Tutoriales:
- https://try.github.io/
- https://learngitbranching.js.org/

### Cheat Sheet:
- https://training.github.com/downloads/github-git-cheat-sheet.pdf

---

## ✅ CHECKLIST GIT

- [ ] Git instalado y configurado
- [ ] Repositorio inicializado
- [ ] .gitignore configurado
- [ ] Archivos agregados
- [ ] Primer commit hecho
- [ ] Conectado a GitHub
- [ ] Push exitoso
- [ ] README.md actualizado
- [ ] Repositorio clonado en otra máquina (prueba)
- [ ] Sistema funciona después de clonar

---

## 🎉 ¡TODO LISTO PARA GIT!

Tu proyecto está preparado para Git y GitHub.

**Siguiente paso:** Subir a GitHub y compartir

---

**Última Actualización:** 11/02/2026  
**Guía para:** DIGIT SOFT  
**Estado:** ✅ Completa

