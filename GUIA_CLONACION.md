# 📦 GUÍA COMPLETA PARA CLONAR Y DESPLEGAR

## 🎯 OBJETIVO

Esta guía te permitirá clonar el proyecto DIGIT SOFT en cualquier computadora y tenerlo funcionando en minutos.

---

## 📋 REQUISITOS PREVIOS

Antes de clonar, asegúrate de tener:

- ✅ Python 3.9 o superior instalado
- ✅ Git instalado
- ✅ Conexión a internet
- ✅ 500 MB de espacio en disco

---

## 🚀 MÉTODO 1: INSTALACIÓN AUTOMÁTICA (RECOMENDADO)

### Windows

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/digit-soft.git
cd digit-soft
```

2. **Ejecutar instalador automático:**
```bash
# Doble click en:
INSTALAR.bat
```

3. **Esperar a que termine** (aprox. 2-5 minutos)

4. **Iniciar el servidor:**
```bash
venv\Scripts\activate
python manage.py runserver
```

5. **Acceder al sistema:**
```
http://127.0.0.1:8000
Usuario: admin
Contraseña: admin123
```

### Linux / Mac

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/digit-soft.git
cd digit-soft
```

2. **Dar permisos al instalador:**
```bash
chmod +x instalar.sh
```

3. **Ejecutar instalador:**
```bash
./instalar.sh
```

4. **Iniciar el servidor:**
```bash
source venv/bin/activate
python manage.py runserver
```

5. **Acceder al sistema:**
```
http://127.0.0.1:8000
Usuario: admin
Contraseña: admin123
```

---

## 🛠️ MÉTODO 2: INSTALACIÓN MANUAL

### Paso 1: Clonar Repositorio

```bash
git clone https://github.com/tu-usuario/digit-soft.git
cd digit-soft
```

### Paso 2: Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Base de Datos

```bash
python manage.py migrate
```

### Paso 5: Crear Superusuario

**Opción A: Automático**
```bash
python crear_superusuario.py
```

**Opción B: Manual**
```bash
python manage.py createsuperuser
# Seguir instrucciones
```

### Paso 6: Iniciar Servidor

```bash
python manage.py runserver
```

### Paso 7: Acceder

```
http://127.0.0.1:8000
Usuario: admin
Contraseña: admin123
```

---

## 📦 VERIFICACIÓN POST-INSTALACIÓN

### Comprobar que todo funciona:

```bash
# 1. Verificar instalación
python manage.py check

# 2. Verificar base de datos
python manage.py showmigrations

# 3. Verificar superusuario
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.filter(is_superuser=True).count()
>>> exit()
```

Si todo muestra ✅, la instalación es exitosa.

---

## 🔧 CONFIGURACIÓN ADICIONAL (OPCIONAL)

### Configurar Email

**Windows:**
```bash
CONFIGURAR_EMAIL_GMAIL.bat
```

**Manual:**
1. Editar `config/settings.py`
2. Buscar sección `EMAIL_BACKEND`
3. Configurar con tus datos

### Cambiar Base de Datos a MySQL

1. Instalar MySQL:
```bash
pip install mysqlclient
```

2. Crear base de datos:
```bash
CREAR_BD_MYSQL.bat
```

3. Editar `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digit_soft',
        'USER': 'root',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. Migrar:
```bash
python manage.py migrate
```

---

## 🗂️ ESTRUCTURA DESPUÉS DE CLONAR

```
digit-soft/
├── venv/                    # ← Se crea al instalar
├── db.sqlite3              # ← Se crea al migrar
├── config/
├── core/
├── usuarios/
├── clientes/
├── ... (todos los módulos)
├── templates/
├── static/
├── requirements.txt
├── README.md
├── INSTALAR.bat            # ← Instalador Windows
├── instalar.sh             # ← Instalador Linux/Mac
├── crear_superusuario.py
└── manage.py
```

---

## ⚠️ PROBLEMAS COMUNES

### 1. Error: "Python no encontrado"

**Solución:**
- Windows: Agregar Python al PATH
- Linux/Mac: Instalar Python 3.9+

```bash
# Verificar instalación
python --version
# o
python3 --version
```

### 2. Error: "pip no encontrado"

**Solución:**
```bash
# Windows
python -m pip install --upgrade pip

# Linux/Mac
sudo apt install python3-pip
```

### 3. Error: "ModuleNotFoundError"

**Solución:**
```bash
# Activar entorno virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

### 4. Error: "Port already in use"

**Solución:**
```bash
# Usar otro puerto
python manage.py runserver 8080
```

### 5. Error al migrar base de datos

**Solución:**
```bash
# Eliminar db.sqlite3 y volver a migrar
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

python manage.py migrate
python crear_superusuario.py
```

---

## 🔐 CREDENCIALES POR DEFECTO

Después de la instalación:

**Superusuario:**
- Usuario: `admin`
- Contraseña: `admin123`
- Email: `admin@digitsoft.com`

**⚠️ IMPORTANTE:** 
Cambiar la contraseña inmediatamente después del primer login.

---

## 📊 DATOS DE PRUEBA

Si necesitas datos de prueba:

```bash
# Crear datos ficticios
python manage.py shell

# Ejecutar scripts de prueba (si los tienes)
python crear_datos_prueba.py
```

---

## 🌐 DESPLIEGUE EN PRODUCCIÓN

Para desplegar en un servidor:

### 1. Configurar settings.py

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']
```

### 2. Configurar archivos estáticos

```bash
python manage.py collectstatic
```

### 3. Usar un servidor WSGI

**Gunicorn (Linux):**
```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

**Waitress (Windows):**
```bash
pip install waitress
waitress-serve --listen=*:8000 config.wsgi:application
```

### 4. Configurar Nginx (opcional)

Ver documentación de Django para producción.

---

## 📝 CHECKLIST DE CLONACIÓN

- [ ] Repositorio clonado
- [ ] Entorno virtual creado
- [ ] Dependencias instaladas
- [ ] Base de datos migrada
- [ ] Superusuario creado
- [ ] Servidor iniciado
- [ ] Login verificado
- [ ] Contraseña cambiada
- [ ] Email configurado (opcional)
- [ ] Sistema funcionando

---

## 🎯 SIGUIENTE PASO

Una vez que el sistema esté funcionando:

1. **Cambiar contraseña del admin**
2. **Crear usuarios de prueba**
3. **Explorar los módulos**
4. **Leer la documentación**
5. **Personalizar según necesites**

---

## 📞 SOPORTE

Si tienes problemas:

1. Revisa esta guía completa
2. Consulta `README.md`
3. Revisa los archivos `.md` en el proyecto
4. Contacta al equipo de soporte

---

## ✅ VERIFICACIÓN FINAL

Para asegurar que todo está OK:

```bash
# 1. Activar entorno
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Verificar sistema
python manage.py check

# 3. Iniciar servidor
python manage.py runserver

# 4. Abrir navegador
http://127.0.0.1:8000

# 5. Login
Usuario: admin
Contraseña: admin123
```

Si puedes hacer login y ver el dashboard, ¡todo está funcionando correctamente! ✅

---

## 🎉 ¡LISTO!

El sistema DIGIT SOFT está clonado y funcionando.

**Disfruta del sistema** 🚀

---

**Última Actualización:** 11/02/2026  
**Versión Guía:** 1.0  
**Estado:** ✅ Completa y Verificada

