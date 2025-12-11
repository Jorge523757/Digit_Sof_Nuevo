"""
Script para generar código de reportes - VERSIÓN AUTOMÁTICA SIN INTERACCIÓN
Ejecutar: python scripts/generar_codigo_reportes_auto.py > codigo_reportes.txt
"""

# Definir módulos y sus modelos principales
MODULOS = {
    'compras': {
        'modelo': 'Compra',
        'campos_reporte': [
            ('numero_compra', 'Número Compra', 'texto'),
            ('proveedor', 'Proveedor', 'texto'),
            ('fecha_compra', 'Fecha', 'fecha'),
            ('subtotal', 'Subtotal', 'moneda'),
            ('impuestos', 'Impuestos', 'moneda'),
            ('total', 'Total', 'moneda'),
            ('estado', 'Estado', 'texto'),
        ],
        'filtros_busqueda': ['numero_compra__icontains', 'proveedor__nombre_empresa__icontains'],
        'orden_default': '-fecha_compra',
        'tiene_totales': True
    },
    'proveedores': {
        'modelo': 'Proveedor',
        'campos_reporte': [
            ('nombre_empresa', 'Empresa', 'texto'),
            ('ruc', 'RUC', 'texto'),
            ('contacto_nombre', 'Contacto', 'texto'),
            ('contacto_telefono', 'Teléfono', 'texto'),
            ('contacto_email', 'Email', 'texto'),
            ('ciudad', 'Ciudad', 'texto'),
            ('tipo_proveedor', 'Tipo', 'texto'),
        ],
        'filtros_busqueda': ['nombre_empresa__icontains', 'ruc__icontains'],
        'orden_default': 'nombre_empresa',
        'tiene_totales': False
    },
    'tecnicos': {
        'modelo': 'Tecnico',
        'campos_reporte': [
            ('numero_documento', 'Documento', 'texto'),
            ('nombres', 'Nombres', 'texto'),
            ('apellidos', 'Apellidos', 'texto'),
            ('telefono', 'Teléfono', 'texto'),
            ('email', 'Email', 'texto'),
            ('especialidad', 'Especialidad', 'texto'),
        ],
        'filtros_busqueda': ['nombres__icontains', 'apellidos__icontains'],
        'orden_default': 'apellidos',
        'tiene_totales': False
    },
    'equipos': {
        'modelo': 'Equipo',
        'campos_reporte': [
            ('numero_serie', 'Número Serie', 'texto'),
            ('tipo_equipo', 'Tipo', 'texto'),
            ('marca', 'Marca', 'texto'),
            ('modelo', 'Modelo', 'texto'),
            ('cliente', 'Cliente', 'texto'),
            ('estado', 'Estado', 'texto'),
        ],
        'filtros_busqueda': ['numero_serie__icontains', 'marca__icontains'],
        'orden_default': '-fecha_registro',
        'tiene_totales': False
    },
    'garantias': {
        'modelo': 'Garantia',
        'campos_reporte': [
            ('numero_serie', 'Número Serie', 'texto'),
            ('producto', 'Producto', 'texto'),
            ('cliente', 'Cliente', 'texto'),
            ('fecha_compra', 'F. Compra', 'fecha'),
            ('fecha_vencimiento', 'F. Vencimiento', 'fecha'),
            ('estado', 'Estado', 'texto'),
        ],
        'filtros_busqueda': ['numero_serie__icontains'],
        'orden_default': '-fecha_compra',
        'tiene_totales': False
    },
    'ordenes': {
        'modelo': 'OrdenServicio',
        'campos_reporte': [
            ('numero_orden', 'Número Orden', 'texto'),
            ('cliente', 'Cliente', 'texto'),
            ('tipo_servicio', 'Tipo', 'texto'),
            ('fecha_ingreso', 'F. Ingreso', 'fecha'),
            ('estado', 'Estado', 'texto'),
            ('costo_servicio', 'Costo Servicio', 'moneda'),
            ('costo_repuestos', 'Costo Repuestos', 'moneda'),
        ],
        'filtros_busqueda': ['numero_orden__icontains'],
        'orden_default': '-fecha_ingreso',
        'tiene_totales': True
    },
    'capacitaciones': {
        'modelo': 'Capacitacion',
        'campos_reporte': [
            ('titulo', 'Título', 'texto'),
            ('instructor', 'Instructor', 'texto'),
            ('fecha_inicio', 'F. Inicio', 'fecha'),
            ('duracion_horas', 'Duración (hrs)', 'numero'),
            ('costo', 'Costo', 'moneda'),
            ('cupo_maximo', 'Cupo', 'numero'),
            ('estado', 'Estado', 'texto'),
        ],
        'filtros_busqueda': ['titulo__icontains', 'instructor__icontains'],
        'orden_default': '-fecha_inicio',
        'tiene_totales': False
    },
}


def generar_codigo_modulo(modulo_nombre, config):
    """Generar código completo para un módulo"""

    modelo = config['modelo']

    print()
    print("=" * 100)
    print(f"MODULO: {modulo_nombre.upper()}")
    print("=" * 100)
    print()

    # CÓDIGO PARA views.py
    print("CÓDIGO PARA COPIAR EN", f"{modulo_nombre}/views.py")
    print("-" * 100)
    print()
    print("# Al inicio del archivo, agregar estos imports si no existen:")
    print("from django.db.models import Q, Sum")
    print("from django.core.paginator import Paginator")
    print()
    print("# Al final del archivo, agregar estas funciones:")
    print()
    print(f"# REPORTES PDF Y EXCEL PARA {modulo_nombre.upper()}")
    print("# " + "=" * 80)
    print()
    print("@login_required")
    print("@staff_required")
    print(f"def {modulo_nombre.rstrip('s')}_reporte_pdf(request):")
    print(f'    """Generar reporte de {modulo_nombre} en PDF"""')
    print("    from utils.reportes import generar_pdf")
    print("    from datetime import datetime")
    print("    ")
    print("    query = request.GET.get('q', '').strip()")
    print("    estado = request.GET.get('estado', '')")
    print("    ")
    print(f"    datos = {modelo}.objects.all()")
    print("    ")
    print("    if query:")
    print("        datos = datos.filter(")

    filtros = config['filtros_busqueda']
    for i, filtro in enumerate(filtros):
        separador = " |" if i > 0 else ""
        print(f"            {separador} Q({filtro}=query)")

    print("        )")
    print("    ")
    print("    if estado:")
    print("        datos = datos.filter(estado=estado)")
    print("    ")
    print(f"    datos = datos.order_by('{config['orden_default']}')")
    print("    ")
    print("    context = {")
    print("        'datos': datos,")
    print("        'fecha': datetime.now(),")
    print("        'usuario': request.user,")
    print("        'total': datos.count(),")
    print("    }")
    print("    ")
    print(f"    filename = f'reporte_{modulo_nombre}_{{datetime.now().strftime(\"%Y%m%d_%H%M%S\")}}.pdf'")
    print(f"    return generar_pdf('reportes/{modulo_nombre}_pdf.html', context, filename)")
    print()
    print()
    print("@login_required")
    print("@staff_required")
    print(f"def {modulo_nombre.rstrip('s')}_reporte_excel(request):")
    print(f'    """Generar reporte de {modulo_nombre} en Excel"""')
    print("    from utils.reportes import generar_excel_avanzado")
    print("    from datetime import datetime")
    print("    ")
    print("    query = request.GET.get('q', '').strip()")
    print("    estado = request.GET.get('estado', '')")
    print("    ")
    print(f"    datos_query = {modelo}.objects.all()")
    print("    ")
    print("    if query:")
    print("        datos_query = datos_query.filter(")

    for i, filtro in enumerate(filtros):
        separador = " |" if i > 0 else ""
        print(f"            {separador} Q({filtro}=query)")

    print("        )")
    print("    ")
    print("    if estado:")
    print("        datos_query = datos_query.filter(estado=estado)")
    print("    ")
    print(f"    datos_query = datos_query.order_by('{config['orden_default']}')")
    print("    ")
    print("    datos = []")
    print("    for item in datos_query:")
    print("        datos.append({")

    for campo, nombre, tipo in config['campos_reporte']:
        key = campo.replace('.', '_').replace('__', '_')
        if campo in ['cliente', 'proveedor', 'producto']:
            print(f"            '{key}': str(item.{campo}) if item.{campo} else '',")
        else:
            print(f"            '{key}': item.{campo},")

    print("        })")
    print("    ")
    print("    columnas = [")

    for campo, nombre, tipo in config['campos_reporte']:
        key = campo.replace('.', '_').replace('__', '_')
        print(f"        ('{key}', '{nombre}', '{tipo}'),")

    print("    ]")
    print("    ")
    print(f"    titulo = 'Reporte de {modelo}s'")
    print(f"    filename = f'reporte_{modulo_nombre}_{{datetime.now().strftime(\"%Y%m%d_%H%M%S\")}}.xlsx'")

    if config.get('tiene_totales'):
        print("    ")
        print("    # Columnas con totales")
        campos_moneda = [c[0].replace('.', '_').replace('__', '_') for c in config['campos_reporte'] if c[2] == 'moneda']
        print(f"    totales = {campos_moneda}")
        print("    ")
        print("    return generar_excel_avanzado(datos, columnas, titulo, filename, totales=totales)")
    else:
        print("    ")
        print("    return generar_excel_avanzado(datos, columnas, titulo, filename)")

    print()
    print("-" * 100)
    print()

    # RUTAS
    print("CÓDIGO PARA COPIAR EN", f"{modulo_nombre}/urls.py")
    print("-" * 100)
    print()
    print("# Agregar al final de urlpatterns, antes del corchete de cierre:")
    print("    # Reportes")
    print(f"    path('reporte/pdf/', views.{modulo_nombre.rstrip('s')}_reporte_pdf, name='reporte_pdf'),")
    print(f"    path('reporte/excel/', views.{modulo_nombre.rstrip('s')}_reporte_excel, name='reporte_excel'),")
    print()
    print("-" * 100)
    print()

    # BOTONES
    print(f"CÓDIGO PARA AGREGAR EN templates/{modulo_nombre}/lista.html")
    print("-" * 100)
    print()
    print("<!-- En el header del card o tabla, agregar: -->")
    print('<div class="btn-group">')
    print(f'    <a href="{{%url \'{modulo_nombre}:reporte_pdf\' %}}?{{{{ request.GET.urlencode }}}}" ')
    print('       class="btn btn-sm btn-danger" title="Descargar PDF">')
    print('        <i class="fas fa-file-pdf"></i> PDF')
    print('    </a>')
    print(f'    <a href="{{%url \'{modulo_nombre}:reporte_excel\' %}}?{{{{ request.GET.urlencode }}}}" ')
    print('       class="btn btn-sm btn-success" title="Descargar Excel">')
    print('        <i class="fas fa-file-excel"></i> Excel')
    print('    </a>')
    print('</div>')
    print()
    print("-" * 100)
    print()

    # TEMPLATE
    print(f"CREAR TEMPLATE: templates/reportes/{modulo_nombre}_pdf.html")
    print("-" * 100)
    print("Copia el archivo templates/reportes/ventas_pdf.html")
    print(f"y renómbralo a {modulo_nombre}_pdf.html")
    print("Luego adapta:")
    print(f"  - Título: 'REPORTE DE {modulo_nombre.upper()}'")
    print("  - Columnas de la tabla según los campos del modelo")
    print("  - Variable 'ventas' por 'datos'")
    print()


# EJECUTAR
print("=" * 100)
print("GENERADOR DE CODIGO DE REPORTES - DIGITSOFT")
print("=" * 100)
print()
print("INSTRUCCIONES GENERALES:")
print()
print("1. Copia el código de cada sección a su archivo correspondiente")
print("2. Asegúrate de tener los imports necesarios")
print("3. Agrega los decoradores @login_required y @staff_required si no los tienes")
print("4. Crea el template PDF copiando y adaptando ventas_pdf.html")
print("5. Agrega los botones en la interfaz de lista")
print()
print("=" * 100)
print()

for modulo, config in MODULOS.items():
    generar_codigo_modulo(modulo, config)
    print()
    print()

print("=" * 100)
print("CODIGO GENERADO PARA TODOS LOS MODULOS - COMPLETO")
print("=" * 100)
print()
print(f"Total módulos: {len(MODULOS)}")
print()
print("Estado de implementacion:")
print("  [OK] Productos - COMPLETO")
print("  [OK] Clientes - COMPLETO")
print("  [OK] Ventas - COMPLETO")
print("  [..] Los 7 modulos restantes - CODIGO GENERADO (listo para copiar)")
print()

