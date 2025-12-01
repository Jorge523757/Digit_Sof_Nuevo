#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para organizar archivos .md, .bat, .txt y .py en carpetas por categoría
"""

import os
import shutil
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).parent

# Crear carpeta docs si no existe
DOCS_DIR = BASE_DIR / 'docs'
DOCS_DIR.mkdir(exist_ok=True)

# Crear carpeta scripts si no existe
SCRIPTS_DIR = BASE_DIR / 'scripts'
SCRIPTS_DIR.mkdir(exist_ok=True)

# Crear carpeta utils si no existe
UTILS_DIR = BASE_DIR / 'utils'
UTILS_DIR.mkdir(exist_ok=True)

# Crear carpeta static_custom si no existe (para JS propios)
STATIC_CUSTOM_DIR = BASE_DIR / 'static_custom'
STATIC_CUSTOM_DIR.mkdir(exist_ok=True)

# Crear carpeta templates_custom si no existe (para HTML propios)
TEMPLATES_CUSTOM_DIR = BASE_DIR / 'templates_custom'
TEMPLATES_CUSTOM_DIR.mkdir(exist_ok=True)

# Categorías para documentos (.md)
CATEGORIAS_DOCS = {
    'GUIAS': DOCS_DIR / '01_GUIAS',
    'SOLUCIONES': DOCS_DIR / '02_SOLUCIONES',
    'INSTRUCCIONES': DOCS_DIR / '03_INSTRUCCIONES',
    'IMPLEMENTACIONES': DOCS_DIR / '04_IMPLEMENTACIONES',
    'SISTEMAS': DOCS_DIR / '05_SISTEMAS',
    'CARRITO': DOCS_DIR / '06_CARRITO',
    'ERRORES': DOCS_DIR / '07_ERRORES_RESUELTOS',
    'ORGANIZACION': DOCS_DIR / '08_ORGANIZACION',
    'OTROS': DOCS_DIR / '09_OTROS'
}

# Categorías para scripts (.bat)
CATEGORIAS_SCRIPTS = {
    'INICIAR': SCRIPTS_DIR / '01_INICIAR',
    'DIAGNOSTICO': SCRIPTS_DIR / '02_DIAGNOSTICO',
    'LIMPIEZA': SCRIPTS_DIR / '03_LIMPIEZA',
    'UTILIDADES': SCRIPTS_DIR / '04_UTILIDADES'
}

# Categorías para textos (.txt)
CATEGORIAS_TEXTOS = {
    'GUIAS': DOCS_DIR / '10_TEXTOS_GUIAS',
    'CONFIGURACION': DOCS_DIR / '11_CONFIGURACION',
    'NOTAS': DOCS_DIR / '12_NOTAS'
}

# Categorías para JavaScript (.js)
CATEGORIAS_JS = {
    'DIAGNOSTICO': STATIC_CUSTOM_DIR / '01_JS_DIAGNOSTICO',
    'CARRITO': STATIC_CUSTOM_DIR / '02_JS_CARRITO',
    'DEBUG': STATIC_CUSTOM_DIR / '03_JS_DEBUG',
    'SOLUCIONES': STATIC_CUSTOM_DIR / '04_JS_SOLUCIONES',
    'OTROS': STATIC_CUSTOM_DIR / '05_JS_OTROS'
}

# Categorías para HTML (.html)
CATEGORIAS_HTML = {
    'PRUEBAS': TEMPLATES_CUSTOM_DIR / '01_HTML_PRUEBAS',
    'DIAGNOSTICO': TEMPLATES_CUSTOM_DIR / '02_HTML_DIAGNOSTICO',
    'SOLUCIONES': TEMPLATES_CUSTOM_DIR / '03_HTML_SOLUCIONES',
    'EJEMPLOS': TEMPLATES_CUSTOM_DIR / '04_HTML_EJEMPLOS',
    'OTROS': TEMPLATES_CUSTOM_DIR / '05_HTML_OTROS'
}

# Categorías para Python (.py)
CATEGORIAS_PYTHON = {
    'PRUEBAS': UTILS_DIR / '01_SCRIPTS_PRUEBA',
    'DATOS': UTILS_DIR / '02_CREAR_DATOS',
    'DIAGNOSTICO': UTILS_DIR / '03_DIAGNOSTICO',
    'VERIFICACION': UTILS_DIR / '04_VERIFICACION',
    'SETUP': UTILS_DIR / '05_SETUP',
    'OTROS': UTILS_DIR / '06_OTROS'
}

# Crear todas las carpetas
for carpeta in (list(CATEGORIAS_DOCS.values()) +
                list(CATEGORIAS_SCRIPTS.values()) +
                list(CATEGORIAS_TEXTOS.values()) +
                list(CATEGORIAS_JS.values()) +
                list(CATEGORIAS_HTML.values()) +
                list(CATEGORIAS_PYTHON.values())):
    carpeta.mkdir(exist_ok=True)

# Archivos que NO se deben mover
ARCHIVOS_EXCLUIDOS = [
    'organizar_docs.py',
    'ORGANIZAR_DOCS.bat',
    'manage.py',
    'README.md',
    'wsgi.py',
    'asgi.py',
    'settings.py',
    'urls.py',
    '__init__.py',
    'ecommerce_urls.py',  # URLs del e-commerce
    'ecommerce_views.py'  # Vistas del e-commerce
]

# Reglas de categorización para .md
def categorizar_md(nombre):
    nombre_upper = nombre.upper()

    if nombre_upper.startswith('README'):
        return None  # No mover READMEs principales
    elif nombre_upper.startswith('GUIA_'):
        return 'GUIAS'
    elif nombre_upper.startswith('SOLUCION_') or 'SOLUCIONADO' in nombre_upper or 'RESUELTO' in nombre_upper:
        return 'SOLUCIONES'
    elif nombre_upper.startswith('INSTRUCCIONES_'):
        return 'INSTRUCCIONES'
    elif nombre_upper.startswith('IMPLEMENTACION_') or 'IMPLEMENTADO' in nombre_upper:
        return 'IMPLEMENTACIONES'
    elif nombre_upper.startswith('SISTEMA_'):
        return 'SISTEMAS'
    elif 'CARRITO' in nombre_upper:
        return 'CARRITO'
    elif nombre_upper.startswith('ERROR_') or 'CORRECCIONES' in nombre_upper or 'CORRECCION' in nombre_upper:
        return 'ERRORES'
    elif 'ORGANIZACION' in nombre_upper or 'ORGANIZAR' in nombre_upper:
        return 'ORGANIZACION'
    else:
        return 'OTROS'

# Reglas de categorización para .bat
def categorizar_bat(nombre):
    nombre_upper = nombre.upper()

    if nombre in ARCHIVOS_EXCLUIDOS:
        return None
    elif nombre_upper.startswith('INICIAR_') or nombre_upper.startswith('ABRIR_'):
        return 'INICIAR'
    elif 'DIAGNOSTICO' in nombre_upper or 'DIAGNOSTICAR' in nombre_upper:
        return 'DIAGNOSTICO'
    elif 'LIMPIAR' in nombre_upper or 'LIMPIEZA' in nombre_upper or 'CLEAR' in nombre_upper:
        return 'LIMPIEZA'
    else:
        return 'UTILIDADES'

# Reglas de categorización para .txt
def categorizar_txt(nombre):
    nombre_upper = nombre.upper()

    if 'REQUIREMENTS' in nombre_upper:
        return None  # No mover requirements.txt
    elif nombre_upper.startswith('COMO_') or nombre_upper.startswith('GUIA_'):
        return 'GUIAS'
    elif 'IP_' in nombre_upper or 'CONFIG' in nombre_upper or 'SETTINGS' in nombre_upper:
        return 'CONFIGURACION'
    else:
        return 'NOTAS'

# Reglas de categorización para .js
def categorizar_js(nombre):
    nombre_upper = nombre.upper()

    # No mover archivos que están en carpetas de Django/static
    if 'DIAGNOSTICO' in nombre_upper or 'DIAGNOSTICAR' in nombre_upper:
        return 'DIAGNOSTICO'
    elif 'CARRITO' in nombre_upper:
        return 'CARRITO'
    elif 'DEBUG' in nombre_upper or 'TEST' in nombre_upper:
        return 'DEBUG'
    elif 'SOLUCION' in nombre_upper or 'EJECUTAR' in nombre_upper:
        return 'SOLUCIONES'
    elif 'LIMPIAR' in nombre_upper or 'LIMPIEZA' in nombre_upper:
        return 'SOLUCIONES'
    else:
        return 'OTROS'

# Reglas de categorización para .html
def categorizar_html(nombre):
    nombre_upper = nombre.upper()

    # No mover archivos importantes
    if nombre_upper.startswith('TEST_') or nombre_upper.startswith('PRUEBA_'):
        return 'PRUEBAS'
    elif 'DIAGNOSTICO' in nombre_upper or 'DIAGNOSTICAR' in nombre_upper:
        return 'DIAGNOSTICO'
    elif 'SOLUCION' in nombre_upper or 'LIMPIEZA' in nombre_upper or 'LIMPIAR' in nombre_upper:
        return 'SOLUCIONES'
    elif 'ECOMMERCE_LISTO' in nombre_upper or 'EJEMPLO' in nombre_upper or 'DEMO' in nombre_upper:
        return 'EJEMPLOS'
    elif 'RESUMEN' in nombre_upper or 'SISTEMA' in nombre_upper:
        return 'EJEMPLOS'
    else:
        return 'OTROS'

# Reglas de categorización para .py
def categorizar_py(nombre):
    nombre_upper = nombre.upper()

    # No mover archivos del sistema
    if nombre in ARCHIVOS_EXCLUIDOS:
        return None
    # No mover archivos que están en carpetas de Django
    elif nombre_upper.startswith('TEST_'):
        return 'PRUEBAS'
    elif nombre_upper.startswith('CREAR_') or nombre_upper.startswith('AGREGAR_'):
        return 'DATOS'
    elif nombre_upper.startswith('DIAGNOSTICO') or nombre_upper.startswith('DIAGNOSTICAR_'):
        return 'DIAGNOSTICO'
    elif nombre_upper.startswith('VERIFICAR_') or nombre_upper.startswith('VERIFICACION_'):
        return 'VERIFICACION'
    elif nombre_upper.startswith('SETUP_') or nombre_upper.startswith('INIT_'):
        return 'SETUP'
    elif nombre_upper.startswith('PRUEBA_') or nombre_upper.startswith('DEMO_'):
        return 'PRUEBAS'
    elif nombre_upper.startswith('UPDATE_'):
        return 'SETUP'
    else:
        return 'OTROS'

# Buscar archivos solo en la raíz
archivos_md = [f for f in BASE_DIR.glob('*.md') if f.is_file()]
archivos_bat = [f for f in BASE_DIR.glob('*.bat') if f.is_file()]
archivos_txt = [f for f in BASE_DIR.glob('*.txt') if f.is_file()]
archivos_js = [f for f in BASE_DIR.glob('*.js') if f.is_file()]
archivos_html = [f for f in BASE_DIR.glob('*.html') if f.is_file()]
archivos_py = [f for f in BASE_DIR.glob('*.py') if f.is_file()]

total_archivos = len(archivos_md) + len(archivos_bat) + len(archivos_txt) + len(archivos_js) + len(archivos_html) + len(archivos_py)

print(f"📁 Organizando archivos de documentación y utilidades...")
print(f"   • {len(archivos_md)} archivos .md")
print(f"   • {len(archivos_bat)} archivos .bat")
print(f"   • {len(archivos_txt)} archivos .txt")
print(f"   • {len(archivos_js)} archivos .js")
print(f"   • {len(archivos_html)} archivos .html")
print(f"   • {len(archivos_py)} archivos .py")
print(f"📂 Total: {total_archivos} archivos")
print("=" * 70)

# Contadores
movidos_docs = {'GUIAS': [], 'SOLUCIONES': [], 'INSTRUCCIONES': [], 'IMPLEMENTACIONES': [],
                'SISTEMAS': [], 'CARRITO': [], 'ERRORES': [], 'ORGANIZACION': [], 'OTROS': []}
movidos_scripts = {'INICIAR': [], 'DIAGNOSTICO': [], 'LIMPIEZA': [], 'UTILIDADES': []}
movidos_textos = {'GUIAS': [], 'CONFIGURACION': [], 'NOTAS': []}
movidos_js = {'DIAGNOSTICO': [], 'CARRITO': [], 'DEBUG': [], 'SOLUCIONES': [], 'OTROS': []}
movidos_html = {'PRUEBAS': [], 'DIAGNOSTICO': [], 'SOLUCIONES': [], 'EJEMPLOS': [], 'OTROS': []}
movidos_python = {'PRUEBAS': [], 'DATOS': [], 'DIAGNOSTICO': [], 'VERIFICACION': [], 'SETUP': [], 'OTROS': []}
no_movidos = []

# Procesar archivos .md
print("\n📄 Organizando archivos .md...")
for archivo in archivos_md:
    categoria = categorizar_md(archivo.name)

    if categoria is None:
        no_movidos.append(archivo.name)
        print(f"   ⏭️  Omitido: {archivo.name}")
        continue

    destino = CATEGORIAS_DOCS[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_docs[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → docs/{CATEGORIAS_DOCS[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Procesar archivos .bat
print("\n🔧 Organizando archivos .bat...")
for archivo in archivos_bat:
    categoria = categorizar_bat(archivo.name)

    if categoria is None:
        no_movidos.append(archivo.name)
        print(f"   ⏭️  Omitido: {archivo.name}")
        continue

    destino = CATEGORIAS_SCRIPTS[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_scripts[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → scripts/{CATEGORIAS_SCRIPTS[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Procesar archivos .txt
print("\n📝 Organizando archivos .txt...")
for archivo in archivos_txt:
    categoria = categorizar_txt(archivo.name)

    if categoria is None:
        no_movidos.append(archivo.name)
        print(f"   ⏭️  Omitido: {archivo.name}")
        continue

    destino = CATEGORIAS_TEXTOS[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_textos[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → docs/{CATEGORIAS_TEXTOS[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Procesar archivos .js
print("\n📜 Organizando archivos .js...")
for archivo in archivos_js:
    categoria = categorizar_js(archivo.name)

    destino = CATEGORIAS_JS[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_js[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → static_custom/{CATEGORIAS_JS[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Procesar archivos .html
print("\n🌐 Organizando archivos .html...")
for archivo in archivos_html:
    categoria = categorizar_html(archivo.name)

    destino = CATEGORIAS_HTML[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_html[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → templates_custom/{CATEGORIAS_HTML[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Procesar archivos .py
print("\n🐍 Organizando archivos .py...")
for archivo in archivos_py:
    categoria = categorizar_py(archivo.name)

    if categoria is None:
        no_movidos.append(archivo.name)
        print(f"   ⏭️  Omitido: {archivo.name}")
        continue

    destino = CATEGORIAS_PYTHON[categoria] / archivo.name

    try:
        shutil.move(str(archivo), str(destino))
        movidos_python[categoria].append(archivo.name)
        print(f"   ✅ {archivo.name} → utils/{CATEGORIAS_PYTHON[categoria].name}/")
    except Exception as e:
        print(f"   ❌ Error: {archivo.name} - {e}")

# Resumen
print("\n" + "=" * 70)
print("📊 RESUMEN DE ORGANIZACIÓN:")
print("=" * 70)

print("\n📄 DOCUMENTOS (.md):")
for categoria, archivos in movidos_docs.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

print("\n🔧 SCRIPTS (.bat):")
for categoria, archivos in movidos_scripts.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

print("\n📝 TEXTOS (.txt):")
for categoria, archivos in movidos_textos.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

print("\n📜 JAVASCRIPT (.js):")
for categoria, archivos in movidos_js.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

print("\n🌐 HTML (.html):")
for categoria, archivos in movidos_html.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

print("\n🐍 PYTHON (.py):")
for categoria, archivos in movidos_python.items():
    if archivos:
        print(f"   📁 {categoria}: {len(archivos)} archivos")

if no_movidos:
    print(f"\n⏭️  Archivos no movidos ({len(no_movidos)}):")
    for archivo in no_movidos[:10]:  # Mostrar solo los primeros 10
        print(f"   • {archivo}")
    if len(no_movidos) > 10:
        print(f"   ... y {len(no_movidos) - 10} más")

total_movidos = (sum(len(v) for v in movidos_docs.values()) +
                 sum(len(v) for v in movidos_scripts.values()) +
                 sum(len(v) for v in movidos_textos.values()) +
                 sum(len(v) for v in movidos_js.values()) +
                 sum(len(v) for v in movidos_html.values()) +
                 sum(len(v) for v in movidos_python.values()))

print("\n" + "=" * 70)
print(f"✅ ¡Organización completada!")
print(f"   • {total_movidos} archivos organizados")
print(f"   • Documentos .md → docs/")
print(f"   • Scripts .bat → scripts/")
print(f"   • Textos .txt → docs/")
print(f"   • JavaScript .js → static_custom/")
print(f"   • HTML .html → templates_custom/")
print(f"   • Python .py → utils/")
print("=" * 70)

