"""
Vistas para el proceso de checkout y facturación
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.utils import timezone
from decimal import Decimal
import json

from ventas.models import Venta, DetalleVenta
from clientes.models import Cliente
from productos.models import Producto
from facturacion.models import Factura


def checkout_view(request):
    """Vista para el proceso de checkout"""
    return render(request, 'ventas/checkout.html')


@transaction.atomic
def procesar_orden(request):
    """Procesar la orden de compra"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        # Obtener datos del POST
        data = json.loads(request.body)
        items = data.get('items', [])
        datos_cliente = data.get('cliente', {})
        tipo_pago = data.get('tipo_pago', 'EFECTIVO')

        if not items:
            return JsonResponse({'success': False, 'error': 'El carrito está vacío'})

        # Crear o obtener cliente
        cliente, created = Cliente.objects.get_or_create(
            email=datos_cliente.get('email'),
            defaults={
                'nombre': datos_cliente.get('nombre'),
                'apellido': datos_cliente.get('apellido', ''),
                'telefono': datos_cliente.get('telefono', ''),
                'direccion': datos_cliente.get('direccion', ''),
                'cedula': datos_cliente.get('cedula', ''),
            }
        )


        # Calcular totales
        subtotal = Decimal('0.00')
        items_procesados = []

        for item in items:
            producto = Producto.objects.get(id=item['id'])
            cantidad = int(item['cantidad'])

            # Verificar stock
            if producto.stock_actual < cantidad:
                return JsonResponse({
                    'success': False,
                    'error': f'Stock insuficiente para {producto.nombre_producto}'
                })

            precio_unitario = Decimal(str(item['precio']))
            subtotal_item = precio_unitario * cantidad
            subtotal += subtotal_item

            items_procesados.append({
                'producto': producto,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'subtotal': subtotal_item
            })

        # Calcular impuestos (IVA 12%)
        iva = subtotal * Decimal('0.12')
        total = subtotal + iva

        # Crear la venta
        venta = Venta.objects.create(
            cliente=cliente,
            subtotal=subtotal,
            impuestos=iva,
            total=total,
            metodo_pago=tipo_pago,
            estado='COMPLETADA',
            notas=datos_cliente.get('notas', '')
        )

        # Crear detalles de venta y actualizar stock
        for item_data in items_procesados:
            DetalleVenta.objects.create(
                venta=venta,
                producto=item_data['producto'],
                cantidad=item_data['cantidad'],
                precio_unitario=item_data['precio_unitario'],
                subtotal=item_data['subtotal']
            )

            # Actualizar stock
            producto = item_data['producto']
            producto.stock_actual -= item_data['cantidad']
            producto.save()

        # Crear factura si se requiere
        if datos_cliente.get('requiere_factura'):
            factura = Factura.objects.create(
                venta=venta,
                cliente=cliente,
                subtotal=subtotal,
                iva=iva,
                total=total,
                estado='EMITIDA'
            )
            factura_id = factura.id
        else:
            factura_id = None

        return JsonResponse({
            'success': True,
            'orden_id': venta.id,
            'factura_id': factura_id,
            'total': float(total),
            'mensaje': '¡Orden procesada exitosamente!'
        })

    except Producto.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def ver_factura(request, orden_id):
    """Ver la factura de una orden"""
    venta = get_object_or_404(Venta, id=orden_id)

    try:
        factura = Factura.objects.get(venta=venta)
    except Factura.DoesNotExist:
        factura = None

    context = {
        'venta': venta,
        'factura': factura,
        'detalles': venta.detalles.all()
    }

    return render(request, 'ventas/factura.html', context)


def descargar_factura_pdf(request, orden_id):
    """Generar y descargar factura en PDF"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from io import BytesIO
    except ImportError:
        return HttpResponse('ReportLab no está instalado. Instalar con: pip install reportlab', status=500)

    venta = get_object_or_404(Venta, id=orden_id)

    try:
        factura = Factura.objects.get(venta=venta)
    except Factura.DoesNotExist:
        return HttpResponse('Factura no encontrada', status=404)

    # Crear PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Título
    title = Paragraph(f"<b>FACTURA #{factura.numero_factura}</b>", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 0.2*inch))

    # Información de la empresa
    empresa_info = Paragraph("""
        <b>DIGITSOFT - Soluciones Informáticas</b><br/>
        RUC: XXXXXXXXXXX<br/>
        Dirección: Tu Dirección<br/>
        Teléfono: Tu Teléfono<br/>
        Email: info@digitsoft.com
    """, styles['Normal'])
    elements.append(empresa_info)
    elements.append(Spacer(1, 0.3*inch))

    # Información del cliente
    cliente_info = Paragraph(f"""
        <b>Cliente:</b> {venta.cliente.nombre} {venta.cliente.apellido}<br/>
        <b>CI:</b> {venta.cliente.cedula}<br/>
        <b>Email:</b> {venta.cliente.email}<br/>
        <b>Teléfono:</b> {venta.cliente.telefono}<br/>
        <b>Dirección:</b> {venta.cliente.direccion}
    """, styles['Normal'])

    elements.append(cliente_info)
    elements.append(Spacer(1, 0.3*inch))

    # Fecha
    fecha_info = Paragraph(f"<b>Fecha:</b> {venta.fecha_venta.strftime('%d/%m/%Y %H:%M')}", styles['Normal'])
    elements.append(fecha_info)
    elements.append(Spacer(1, 0.3*inch))

    # Tabla de productos
    data = [['Cant.', 'Producto', 'P. Unit.', 'Subtotal']]

    for detalle in venta.detalles.all():
        data.append([
            str(detalle.cantidad),
            detalle.producto.nombre_producto[:40],
            f'${detalle.precio_unitario:.2f}',
            f'${detalle.subtotal:.2f}'
        ])

    # Totales
    data.append(['', '', 'Subtotal:', f'${venta.subtotal:.2f}'])
    data.append(['', '', 'IVA 12%:', f'${venta.impuestos:.2f}'])
    data.append(['', '', 'TOTAL:', f'${venta.total:.2f}'])

    table = Table(data, colWidths=[0.8*inch, 4*inch, 1.2*inch, 1.2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -4), colors.beige),
        ('GRID', (0, 0), (-1, -4), 1, colors.black),
        ('FONTNAME', (0, -3), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -3), (-1, -1), colors.lightgrey),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))

    # Pie de página
    footer = Paragraph("<i>Gracias por su compra. DIGITSOFT - Soluciones Informáticas</i>", styles['Normal'])
    elements.append(footer)

    doc.build(elements)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.numero_factura}.pdf"'

    return response


def mis_ordenes(request):
    """Lista de órdenes del cliente"""
    # Por ahora mostrar todas las ventas
    ventas = Venta.objects.all().order_by('-fecha_venta')[:50]

    context = {
        'ventas': ventas
    }

    return render(request, 'ventas/mis_ordenes.html', context)

