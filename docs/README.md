# 📚 Documentación del Proyecto Digit Soft E-commerce

Esta carpeta contiene toda la documentación técnica, guías, soluciones, instrucciones y archivos de texto del proyecto organizados por categorías.

---

## 📂 Estructura de Carpetas

### 📘 DOCUMENTOS (.md)

#### 01_GUIAS/
Guías completas de uso, configuración y personalización del sistema.
- Guías de acceso y conexión
- Guías de personalización
- Guías de uso completo del sistema

#### 02_SOLUCIONES/
Documentación sobre soluciones implementadas para diferentes problemas.
- Soluciones de carrito
- Soluciones de imágenes
- Soluciones de localStorage
- Correcciones y optimizaciones

#### 03_INSTRUCCIONES/
Instrucciones paso a paso para diferentes procedimientos.
- Instrucciones de prueba
- Instrucciones de desarrollo
- Instrucciones finales

#### 04_IMPLEMENTACIONES/
Documentación sobre implementaciones de funcionalidades.
- Login y restricciones
- Módulos y características
- Integraciones

#### 05_SISTEMAS/
Documentación de sistemas completos implementados.
- Sistema de ventas
- Sistema de e-commerce
- Sistema de carrito y facturación

#### 06_CARRITO/
Documentación específica del sistema de carrito de compras.
- Carrito funcional
- Notificaciones del carrito
- Mejoras y optimizaciones

#### 07_ERRORES_RESUELTOS/
Registro de errores encontrados y sus soluciones.
- Errores corregidos
- Problemas resueltos
- Correcciones aplicadas

#### 08_OTROS/
Documentación miscelánea y otros archivos.
- Arquitecturas
- Diagramas
- Notas técnicas

#### 09_TEXTOS_GUIAS/
Archivos de texto con guías y tutoriales.
- Guías en formato .txt
- Tutoriales rápidos

#### 10_NOTAS/
Notas técnicas y recordatorios.
- Notas de desarrollo
- Recordatorios
- Información adicional

---

### 🔧 SCRIPTS (.bat)

Los scripts están organizados en la carpeta `scripts/` en la raíz del proyecto:

#### scripts/01_INICIAR/
Scripts para iniciar el sistema y sus componentes.
- Iniciar servidor Django
- Abrir aplicación
- Detectar IP e iniciar

#### scripts/02_DIAGNOSTICO/
Scripts para diagnosticar problemas.
- Diagnóstico de carrito
- Diagnóstico de imágenes
- Verificación de sistema

#### scripts/03_LIMPIEZA/
Scripts para limpiar datos y cache.
- Limpiar carrito
- Limpiar localStorage
- Resetear sistema

#### scripts/04_UTILIDADES/
Scripts de utilidades varias.
- Crear datos de prueba
- Gestión de productos
- Herramientas auxiliares

---

## 🚀 Cómo Usar Esta Documentación

### Para Encontrar Información:
1. Identifica el tema que necesitas (Guía, Solución, Error, etc.)
2. Ve a la carpeta correspondiente
3. Busca el archivo más reciente o específico

### Para Ejecutar Scripts:
1. Ve a la carpeta `scripts/` en la raíz del proyecto
2. Busca en la subcarpeta correspondiente
3. Ejecuta el archivo .bat con doble clic

### Para Agregar Nueva Documentación:
1. Crea el archivo `.md`, `.bat` o `.txt` en la raíz del proyecto
2. Ejecuta `ORGANIZAR_DOCS.bat`
3. El archivo se moverá automáticamente a la carpeta correcta

---

## 📌 Archivos Principales (No Organizados)

Algunos archivos permanecen en la raíz del proyecto por su importancia:
- `README.md` - Documentación principal del proyecto
- `ORGANIZAR_DOCS.bat` - Script de organización
- `manage.py` - Gestor de Django

---

## 🔍 Cómo Buscar

### Por Tipo de Archivo:
```
Documentos .md    → docs/
Scripts .bat      → scripts/
Textos .txt       → docs/09_TEXTOS_GUIAS/ o docs/10_NOTAS/
```

### Por Categoría:
```
docs/
├── 01_GUIAS/              → Guías de uso
├── 02_SOLUCIONES/         → Soluciones implementadas
├── 03_INSTRUCCIONES/      → Pasos a seguir
├── 04_IMPLEMENTACIONES/   → Funcionalidades nuevas
├── 05_SISTEMAS/           → Sistemas completos
├── 06_CARRITO/            → Todo sobre el carrito
├── 07_ERRORES_RESUELTOS/  → Problemas solucionados
├── 08_OTROS/              → Documentación varia
├── 09_TEXTOS_GUIAS/       → Guías en .txt
└── 10_NOTAS/              → Notas técnicas

scripts/
├── 01_INICIAR/            → Iniciar sistema
├── 02_DIAGNOSTICO/        → Diagnosticar problemas
├── 03_LIMPIEZA/           → Limpiar datos
└── 04_UTILIDADES/         → Herramientas varias
```

---

## 📝 Convenciones de Nombres

### Documentos (.md):
- `GUIA_*.md` - Guías de usuario
- `SOLUCION_*.md` - Soluciones a problemas
- `INSTRUCCIONES_*.md` - Instrucciones paso a paso
- `IMPLEMENTACION_*.md` - Nuevas funcionalidades
- `SISTEMA_*.md` - Sistemas completos
- `CARRITO_*.md` - Relacionado con el carrito
- `ERROR_*.md` - Errores resueltos

### Scripts (.bat):
- `INICIAR_*.bat` - Iniciar sistema
- `DIAGNOSTICO_*.bat` - Diagnóstico
- `LIMPIAR_*.bat` - Limpieza
- Otros - Utilidades

### Textos (.txt):
- `COMO_*.txt` - Guías
- Otros - Notas

---

## 🔄 Reorganizar Todo

Si necesitas reorganizar toda la documentación y scripts:

### Windows:
```batch
ORGANIZAR_DOCS.bat
```

### Linux/Mac:
```bash
python organizar_docs.py
```

---

## 📊 Estadísticas

Total de archivos organizados: **~100+ archivos**

Distribución aproximada:
- 📘 Documentos .md: ~86 archivos
- 🔧 Scripts .bat: ~10-15 archivos
- 📝 Textos .txt: ~5 archivos

---

## 🎯 Documentos Más Importantes

### Para Empezar:
- `docs/01_GUIAS/GUIA_COMPLETA_USO.md`
- `docs/01_GUIAS/GUIA_RAPIDA_ECOMMERCE.md`
- `scripts/01_INICIAR/INICIAR_ECOMMERCE.bat`

### Para Solucionar Problemas:
- `docs/02_SOLUCIONES/SOLUCION_DEFINITIVA_IMAGENES.md`
- `docs/02_SOLUCIONES/SOLUCION_CARRITO_COMPLETA.md`
- `scripts/02_DIAGNOSTICO/` (varios scripts)

### Para Implementar:
- `docs/04_IMPLEMENTACIONES/IMPLEMENTACION_COMPLETADA.md`
- `docs/04_IMPLEMENTACIONES/IMPLEMENTACION_LOGIN_RESTRICCIONES.md`

---

## ⚙️ Mantenimiento

Esta estructura se mantiene automáticamente mediante:
- `organizar_docs.py` - Script de organización
- `ORGANIZAR_DOCS.bat` - Script de ejecución rápida

El script organiza automáticamente:
- ✅ Archivos `.md` → `docs/` (por categoría)
- ✅ Archivos `.bat` → `scripts/` (por función)
- ✅ Archivos `.txt` → `docs/` (por tipo)

---

## 📞 Soporte

Si tienes dudas sobre alguna documentación:
1. Revisa el archivo correspondiente
2. Busca en carpetas relacionadas
3. Consulta los scripts en `scripts/`
4. Revisa los archivos principales en la raíz

---

**Última actualización:** 2025-11-28
**Versión:** 2.0
**Total de archivos:** ~100+ archivos organizados

