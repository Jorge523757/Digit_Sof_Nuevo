# 🚀 GUÍA RÁPIDA - CÓMO USAR EL PROYECTO ACTUALIZADO

**Última Actualización:** 14 de Febrero de 2026  
**Commit Base:** 7b6302a - "cambios en la accesibilidad"

---

## ✅ PARA TI (JORGE) - YA ESTÁ TODO LISTO

Tu rama **jorge-dev** ya está actualizada y lista para usar. Todo funciona correctamente.

### Iniciar el Proyecto:

```bash
# 1. Ir al directorio del proyecto (ya estás ahí)
cd C:\Users\jorge\OneDrive\Escritorio\AdelantoDigitSoft2026\Digit_Sof_Nuevo

# 2. Iniciar el servidor
python manage.py runserver

# 3. Abrir navegador en:
http://127.0.0.1:8000/
```

### Credenciales de Acceso:
- **Usuario Admin:** admin
- **Contraseña:** admin123

O puedes usar **Google OAuth** para iniciar sesión.

---

## 📧 PARA ADRIANA - ACTUALIZAR SU RAMA

Adriana debe seguir estos pasos para actualizar su rama:

### Opción 1: Actualización Rápida (Recomendada)

```bash
# 1. Abrir PowerShell en el directorio del proyecto
cd [ruta-de-su-proyecto]

# 2. Descartar cambios locales (ADVERTENCIA: esto borra cambios no guardados)
git checkout .

# 3. Actualizar información del repositorio
git fetch --all

# 4. Cambiar a su rama
git checkout adriana

# 5. Actualizar con la versión del servidor
git reset --hard origin/adriana

# 6. Aplicar migraciones
python manage.py migrate

# 7. Iniciar servidor
python manage.py runserver
```

### Opción 2: Clonar de Nuevo

Si tiene problemas, puede clonar el repositorio nuevamente:

```bash
# 1. Respaldar archivos importantes (si los tiene)

# 2. Eliminar carpeta actual del proyecto

# 3. Clonar desde GitHub
git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git

# 4. Entrar al directorio
cd Digit_Sof_Nuevo

# 5. Cambiar a su rama
git checkout adriana

# 6. Instalar dependencias (si es necesario)
pip install -r requirements.txt

# 7. Aplicar migraciones
python manage.py migrate

# 8. Iniciar servidor
python manage.py runserver
```

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### Para Hacer Cambios:

1. **Asegurarse de estar en tu rama:**
   ```bash
   git checkout jorge-dev  # o adriana
   ```

2. **Antes de empezar a trabajar:**
   ```bash
   git pull origin jorge-dev  # o adriana
   ```

3. **Hacer tus cambios en el código**

4. **Guardar cambios:**
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```

5. **Subir a GitHub:**
   ```bash
   git push origin jorge-dev  # o adriana
   ```

### Para Sincronizar con Main:

```bash
# 1. Estar en tu rama
git checkout jorge-dev

# 2. Traer cambios de main
git pull origin main

# 3. Resolver conflictos si los hay

# 4. Subir cambios
git push origin jorge-dev
```

---

## 🎯 COMANDOS ÚTILES

### Ver Estado del Repositorio:
```bash
git status                 # Ver cambios pendientes
git log --oneline -5       # Ver últimos 5 commits
git branch -a              # Ver todas las ramas
```

### Verificar el Proyecto Django:
```bash
python manage.py check              # Verificar errores
python manage.py showmigrations     # Ver estado de migraciones
python manage.py migrate            # Aplicar migraciones
python manage.py createsuperuser    # Crear superusuario (si es necesario)
```

### Administrar la Base de Datos:
```bash
# Crear migraciones después de cambiar modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver SQL de una migración
python manage.py sqlmigrate [app_name] [migration_number]
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "No module named..."
```bash
pip install -r requirements.txt
```

### Error en Migraciones:
```bash
python manage.py migrate --fake [app_name] [migration_name]
python manage.py migrate
```

### Problemas con Git:
```bash
# Descartar todos los cambios locales
git checkout .
git clean -fd

# Actualizar forzadamente
git fetch --all
git reset --hard origin/[nombre-rama]
```

### El servidor no inicia:
```bash
# Verificar errores
python manage.py check

# Ver procesos en el puerto 8000
netstat -ano | findstr :8000

# Matar proceso si es necesario
taskkill /PID [número-proceso] /F
```

---

## 📊 ESTRUCTURA DEL PROYECTO

```
Digit_Sof_Nuevo/
├── config/              # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ordenes/             # Módulo de órdenes de servicio
├── clientes/            # Módulo de clientes
├── productos/           # Módulo de productos
├── compras/             # Módulo de compras
├── ventas/              # Módulo de ventas
├── usuarios/            # Gestión de usuarios
├── notificaciones/      # Sistema de notificaciones
├── ayuda/               # Módulo de ayuda
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Plantillas HTML
├── media/               # Archivos subidos por usuarios
├── db.sqlite3           # Base de datos
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto
```

---

## 🎨 CARACTERÍSTICAS DISPONIBLES

### Para Usuarios Admin:
- ✅ Gestión completa de órdenes de servicio
- ✅ CRUD de clientes, productos, técnicos
- ✅ Sistema de compras y ventas
- ✅ Reportes y estadísticas
- ✅ Configuración del sistema
- ✅ Gestión de usuarios

### Para Usuarios Cliente:
- ✅ Ver sus órdenes de servicio
- ✅ Tienda de productos
- ✅ Carrito de compras
- ✅ Historial de compras
- ✅ Perfil personal

### Para Todos:
- ✅ Tema claro/oscuro
- ✅ Accesibilidad mejorada
- ✅ Diseño responsive
- ✅ Notificaciones en tiempo real
- ✅ Sistema de ayuda integrado

---

## 📱 ACCESO AL SISTEMA

### URLs Principales:
- **Inicio:** http://127.0.0.1:8000/
- **Login:** http://127.0.0.1:8000/usuarios/login/
- **Dashboard:** http://127.0.0.1:8000/dashboard/
- **Admin Django:** http://127.0.0.1:8000/admin/
- **Órdenes:** http://127.0.0.1:8000/ordenes/
- **Clientes:** http://127.0.0.1:8000/clientes/
- **Productos:** http://127.0.0.1:8000/productos/
- **Tienda:** http://127.0.0.1:8000/ventas/tienda/

---

## 💡 CONSEJOS Y MEJORES PRÁCTICAS

### Al Desarrollar:
1. ✅ Hacer commits frecuentes con mensajes descriptivos
2. ✅ Probar en el navegador antes de hacer commit
3. ✅ Usar `git status` regularmente
4. ✅ Comunicar cambios importantes al equipo
5. ✅ Revisar código antes de hacer merge

### Al Colaborar:
1. ✅ Respetar las ramas de cada persona
2. ✅ Usar Pull Requests para merge a main
3. ✅ Documentar cambios importantes
4. ✅ Mantener sincronización regular
5. ✅ Resolver conflictos comunicándose

### Seguridad:
1. ✅ No compartir credenciales
2. ✅ No subir archivos sensibles (.env, db.sqlite3)
3. ✅ Usar .gitignore correctamente
4. ✅ Cambiar SECRET_KEY para producción
5. ✅ Configurar HTTPS en producción

---

## 🎉 ESTADO ACTUAL

| Componente | Estado | Notas |
|------------|--------|-------|
| **Código** | ✅ Funcionando | Sin errores |
| **Base de Datos** | ✅ Actualizada | Migraciones aplicadas |
| **Dependencias** | ✅ Instaladas | requirements.txt completo |
| **jorge-dev** | ✅ Actualizada | Lista para desarrollo |
| **main** | ✅ Actualizada | Sincronizada |
| **adriana** | ✅ Actualizada | Lista para que Adriana la use |
| **Servidor** | ✅ Operativo | http://127.0.0.1:8000/ |

---

## 📞 CONTACTO Y SOPORTE

Si tienes problemas:
1. Revisa este documento
2. Consulta `RAMAS_ACTUALIZADAS_CONFIRMACION.md`
3. Ejecuta `python manage.py check`
4. Revisa los logs en la consola

---

**¡TODO ESTÁ LISTO PARA TRABAJAR!** 🚀

*Última actualización: 14 de Febrero de 2026 - 11:30 AM*

