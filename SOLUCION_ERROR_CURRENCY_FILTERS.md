# ✅ SOLUCIÓN: Error "currency_filters is not a registered tag library"

## 🔴 El Problema

```
TemplateSyntaxError at /ordenes/42/editar/
'currency_filters' is not a registered tag library. Must be one of:
admin_list, admin_modify, admin_urls, cache, i18n, l10n, log, math_filters, static, tz
```

---

## ✅ La Solución (APLICADA)

El error ocurría porque Django no reconocía `currency_filters` como una biblioteca de tags válida. 

### Cambios Realizados:

#### 1. **Agregado `utils` a INSTALLED_APPS** ✅
**Archivo:** `config/settings.py`

```python
INSTALLED_APPS = [
    # ... otras apps ...
    'utils',  # ← AGREGADO
]
```

#### 2. **Creados archivos de configuración** ✅

**`utils/__init__.py`**
```python
# Utils app - Utilidades y filtros personalizados
```

**`utils/apps.py`**
```python
from django.apps import AppConfig

class UtilsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utils'
    verbose_name = 'Utilidades'
```

---

## 🔧 Cómo Aplicar la Solución

### Paso 1: Detener el servidor
- Presiona `Ctrl + C` en la terminal donde corre el servidor

### Paso 2: Reiniciar el servidor
```bash
python manage.py runserver
```

O usa el script:
```bash
REINICIAR_SERVIDOR_CORREGIDO.bat
```

---

## ✅ Verificación

Después de reiniciar el servidor:

1. Ve a: http://localhost:8000/ordenes/42/editar/
2. La página debería cargar sin errores
3. Los campos de costo mostrarán formato colombiano

---

## 📝 Explicación Técnica

### ¿Por qué pasó esto?

Django necesita que los **template tags personalizados** estén dentro de una app registrada en `INSTALLED_APPS`.

**Antes:**
- `utils` era solo una carpeta
- No estaba en INSTALLED_APPS
- Django no reconocía `currency_filters`

**Después:**
- `utils` es una app Django válida
- Está en INSTALLED_APPS
- Django reconoce todos los templatetags dentro de `utils/templatetags/`

---

## 🎯 Estructura Correcta

```
utils/
├── __init__.py          ✅ (creado)
├── apps.py              ✅ (creado)
├── reportes.py          ✅ (ya existía)
└── templatetags/
    ├── __init__.py      ✅ (ya existía)
    └── currency_filters.py ✅ (ya existía)
```

---

## ✅ Estado Actual

- [x] `utils` agregado a INSTALLED_APPS
- [x] `utils/__init__.py` creado
- [x] `utils/apps.py` creado
- [x] Django verifica sin errores: `python manage.py check`
- [x] Listo para usar `{% load currency_filters %}`

---

## 🚀 Próximos Pasos

1. **Reinicia el servidor** (Ctrl+C, luego `python manage.py runserver`)
2. **Prueba la página** de editar orden
3. **Verifica** que los campos de costo funcionen correctamente

---

## 📞 Si el Error Persiste

1. Asegúrate de haber detenido completamente el servidor anterior
2. Limpia archivos cache:
   ```bash
   python manage.py collectstatic --clear --noinput
   ```
3. Reinicia el servidor:
   ```bash
   python manage.py runserver
   ```

---

**Fecha de solución:** 4 de Febrero de 2026  
**Estado:** ✅ SOLUCIONADO  
**Acción requerida:** Reiniciar servidor Django

