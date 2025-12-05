"""
Script para agregar funcionalidad de reportes a todos los módulos
"""

MODULOS = [
    'ventas',
    'compras',
    'proveedores',
    'tecnicos',
    'equipos',
    'garantias',
    'ordenes',
    'capacitaciones',
]

REPORTES_VIEWS_TEMPLATE = """

# REPORTES PDF Y EXCEL
# ==============================================

@login_required
@staff_required
def {modulo}_reporte_pdf(request):
    \"\"\"Generar reporte de {modulo} en PDF\"\"\"
    from utils.reportes import generar_pdf
    from datetime import datetime
    
    # Obtener filtros (personalizar según módulo)
    query = request.GET.get('q', '').strip()
    
    # Filtrar datos
    datos = {Modelo}.objects.all()
    
    if query:
        datos = datos.filter(
            Q(campo1__icontains=query) |
            Q(campo2__icontains=query)
        )
    
    datos = datos.order_by('-fecha_creacion')
    
    context = {{
        'datos': datos,
        'fecha': datetime.now(),
        'usuario': request.user,
        'total': datos.count(),
    }}
    
    filename = f'reporte_{modulo}_{{datetime.now().strftime("%Y%m%d_%H%M%S")}}.pdf'
    return generar_pdf('reportes/{modulo}_pdf.html', context, filename)


@login_required
@staff_required
def {modulo}_reporte_excel(request):
    \"\"\"Generar reporte de {modulo} en Excel\"\"\"
    from utils.reportes import generar_excel_avanzado
    from datetime import datetime
    
    # Obtener filtros
    query = request.GET.get('q', '').strip()
    
    # Filtrar datos
    datos_query = {Modelo}.objects.all()
    
    if query:
        datos_query = datos_query.filter(
            Q(campo1__icontains=query) |
            Q(campo2__icontains=query)
        )
    
    datos_query = datos_query.order_by('-fecha_creacion')
    
    # Preparar datos para Excel
    datos = []
    for item in datos_query:
        datos.append({{
            'campo1': item.campo1,
            'campo2': item.campo2,
            # Agregar más campos según necesidad
        }})
    
    # Definir columnas
    columnas = [
        ('campo1', 'Campo 1', 'texto'),
        ('campo2', 'Campo 2', 'texto'),
        # Agregar más columnas
    ]
    
    titulo = 'Reporte de {Modulo}'
    filename = f'reporte_{modulo}_{{datetime.now().strftime("%Y%m%d_%H%M%S")}}.xlsx'
    
    return generar_excel_avanzado(datos, columnas, titulo, filename)
"""

URLS_TEMPLATE = """
    # Reportes
    path('reporte/pdf/', views.{modulo}_reporte_pdf, name='reporte_pdf'),
    path('reporte/excel/', views.{modulo}_reporte_excel, name='reporte_excel'),
"""

print("Templates creados. Personalizar según cada módulo.")

