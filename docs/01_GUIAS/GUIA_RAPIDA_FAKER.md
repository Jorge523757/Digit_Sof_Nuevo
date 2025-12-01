# 🎯 Guía Rápida de Uso - DIGIT SOFT con Faker

## ✅ Sistema Instalado y Listo

Tu sistema ya está configurado con:
- ✅ Superusuario creado (admin/admin123)
- ✅ 30 clientes de prueba
- ✅ 15 proveedores de prueba
- ✅ 50 productos de prueba en 7 categorías

## 🚀 Iniciar el Sistema

```bash
python manage.py runserver
```

Luego abre en tu navegador: **http://127.0.0.1:8000/admin/**

## 🔐 Credenciales de Acceso

- **Usuario:** `admin`
- **Contraseña:** `admin123`

⚠️ **IMPORTANTE:** Cambia estas credenciales en producción.

## 📦 Comandos de Seeding Disponibles

### Poblar Clientes
```bash
# Crear 30 clientes
python manage.py populate_clientes 30

# Crear 50 clientes y eliminar los existentes
python manage.py populate_clientes 50 --clear
```

### Poblar Proveedores
```bash
# Crear 15 proveedores
python manage.py populate_proveedores 15

# Crear 20 proveedores y eliminar los existentes
python manage.py populate_proveedores 20 --clear
```

### Poblar Productos
```bash
# Crear 50 productos
python manage.py populate_productos 50

# Crear 100 productos y eliminar los existentes
python manage.py populate_productos 100 --clear
```

### Inicializar TODO el Sistema
```bash
# Crea superusuario + pobla TODAS las tablas
python init_system.py
```

## 🔄 Reiniciar el Sistema Completo

Si quieres empezar desde cero:

```bash
# Windows
del db.sqlite3
python init_system.py

# Linux/Mac
rm db.sqlite3
python init_system.py
```

## 📊 Datos Generados

### Clientes
- Nombres y apellidos colombianos realistas
- Números de documento únicos
- Emails válidos basados en nombres
- Direcciones colombianas
- Teléfonos locales
- Estado activo/inactivo aleatorio
- Observaciones de negocio

### Proveedores
- Nombres de empresas tecnológicas
- NITs colombianos válidos
- Información de contacto completa
- Ciudades principales de Colombia
- Productos/servicios especializados
- Condiciones de pago realistas
- Tiempos de entrega
- Calificaciones

### Productos
- Nombres de productos tecnológicos realistas
- Códigos SKU únicos
- 7 categorías:
  - Computadores y Laptops
  - Componentes de Hardware
  - Periféricos
  - Smartphones y Tablets
  - Accesorios Tecnológicos
  - Redes y Comunicaciones
  - Audio y Video
- Especificaciones técnicas detalladas
- Precios coherentes (compra, venta, mayorista)
- Stock con niveles mínimos/máximos
- Marcas conocidas (HP, Dell, Lenovo, Samsung, Apple, etc.)
- Procesadores, RAM, almacenamiento
- Meses de garantía

## 🎨 Personalización

### Cambiar cantidad de datos por defecto

Edita `init_system.py` y modifica estas líneas:

```python
# En la función populate_database()
call_command('populate_clientes', 30, '--clear')    # Cambia 30
call_command('populate_proveedores', 15, '--clear')  # Cambia 15
call_command('populate_productos', 50, '--clear')    # Cambia 50
```

### Cambiar credenciales del superusuario

Edita `init_system.py` en la función `create_superuser()`:

```python
username = "admin"                # Tu usuario preferido
email = "admin@digitsoft.com"     # Tu email
password = "admin123"             # Tu contraseña segura
```

## 🛠️ Comandos Útiles de Django

```bash
# Ver migraciones pendientes
python manage.py showmigrations

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Abrir shell de Django
python manage.py shell

# Ver todos los comandos disponibles
python manage.py help

# Listar comandos personalizados
python manage.py help | findstr populate
```

## 📱 Al Clonar el Proyecto

Cuando clones este proyecto en otra máquina:

```bash
# 1. Clonar repositorio
git clone [url-repo]
cd Digit_Sof_Nuevo

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Inicializar sistema completo (hace TODO automáticamente)
python init_system.py

# 6. Iniciar servidor
python manage.py runserver
```

¡Listo! No necesitas crear el superusuario manualmente nunca más.

## 🎯 Uso del Script BAT (Solo Windows)

Simplemente ejecuta el archivo:

```
SETUP_COMPLETO.bat
```

Esto hará **TODO** automáticamente:
1. ✅ Verifica Python
2. ✅ Crea entorno virtual
3. ✅ Instala dependencias
4. ✅ Aplica migraciones
5. ✅ Crea superusuario
6. ✅ Pobla la base de datos

## 💡 Tips

1. **Usa `--clear`** cuando quieras refrescar los datos de prueba
2. **NO uses `--clear` en producción** - perderás todos los datos reales
3. Los datos generados son **completamente ficticios** pero realistas
4. Puedes ejecutar los comandos **múltiples veces** sin problema
5. Los SKUs, NITs y documentos son **únicos** automáticamente

## 🔍 Verificar los Datos

Después de poblar, puedes verificar en el panel admin:

1. Ve a http://127.0.0.1:8000/admin/
2. Inicia sesión (admin/admin123)
3. Explora las secciones:
   - Clientes
   - Productos
   - Proveedores
   - Categorías de Productos

## 📚 Documentación Adicional

- `README_FAKER_SETUP.md` - Documentación completa del sistema
- `GUIA_COMPLETA_USO.md` - Guía de uso del sistema
- `requirements.txt` - Lista de dependencias

---

**¡Disfruta usando DIGIT SOFT con datos de prueba realistas! 🎉**

