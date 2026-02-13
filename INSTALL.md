# INSTRUCCIONES DE INSTALACIÓN

## 🚀 CONFIGURACIÓN AUTOMÁTICA (RECOMENDADO)

Después de clonar el repositorio:

### Windows
```bash
SETUP_AUTOMATICO.bat
```

### Linux/Mac
```bash
python setup_proyecto.py
```

Esto hará AUTOMÁTICAMENTE:
1. ✅ Instalará todas las dependencias
2. ✅ Aplicará las migraciones
3. ✅ Creará el superusuario (admin/admin123)
4. ✅ Configurará las vistas SQL
5. ✅ Recolectará archivos estáticos

## ⚡ INICIO RÁPIDO

Una vez completada la configuración:

```bash
python manage.py runserver
```

Acceder a: http://127.0.0.1:8000

**Credenciales:**
- Usuario: `admin`
- Contraseña: `admin123`

## ✅ VERIFICACIÓN

Para verificar que todo está correcto:

```bash
python manage.py check
```

Debe mostrar: "System check identified no issues (0 silenced)."

## 📋 REQUISITOS

- Python 3.8+
- pip

Todas las dependencias se instalan automáticamente con el script de configuración.

