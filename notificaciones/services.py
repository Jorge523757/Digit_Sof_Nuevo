"""
DIGIT SOFT - Servicio de Notificaciones
Sistema de envío de emails y notificaciones web para órdenes de servicio
"""

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone

from .models import NotificacionEmail, NotificacionWeb


class ServicioNotificaciones:
    """Servicio centralizado para envío de notificaciones"""

    @staticmethod
    def notificar_admin_reporte_cliente(reporte):
        """
        Notifica al administrador sobre un nuevo reporte de cliente
        Asunto: "Envío de reporte de cliente"
        """
        try:
            # Obtener emails de administradores
            admins = User.objects.filter(is_staff=True, is_superuser=True)

            for admin in admins:
                # Crear contenido del email
                asunto = "Envío de reporte de cliente"

                contexto = {
                    'reporte': reporte,
                    'cliente': reporte.cliente,
                    'equipo': reporte.equipo,
                    'descripcion': reporte.descripcion_dano,
                    'tiempo_requerido': reporte.tiempo_requerido_cliente,
                }

                # Contenido HTML
                html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 30px; text-align: center; }}
        .content {{ padding: 30px; }}
        .info-box {{ background: #e7f3ff; border-left: 4px solid #1e3c72; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .label {{ font-weight: bold; color: #1e3c72; }}
        .value {{ margin-bottom: 10px; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">📋 Nuevo Reporte de Cliente</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT - Sistema de Gestión</p>
        </div>
        <div class="content">
            <h2>Reporte #{reporte.numero_reporte}</h2>
            <p>Se ha recibido un nuevo reporte de equipo dañado:</p>
            
            <div class="info-box">
                <div class="value">
                    <span class="label">👤 Cliente:</span> {reporte.cliente.nombre_completo}
                </div>
                <div class="value">
                    <span class="label">📧 Email:</span> {reporte.cliente.email}
                </div>
                <div class="value">
                    <span class="label">📱 Teléfono:</span> {reporte.cliente.telefono or 'No especificado'}
                </div>
            </div>
            
            <div class="info-box">
                <div class="value">
                    <span class="label">💻 Equipo:</span> {reporte.equipo.nombre if reporte.equipo else 'No especificado'}
                </div>
                {f'<div class="value"><span class="label">🏷️ Código:</span> {reporte.equipo.codigo_equipo}</div>' if reporte.equipo else ''}
            </div>
            
            <h3>📝 Descripción del Daño:</h3>
            <p style="background: #f8f9fa; padding: 15px; border-radius: 5px;">{reporte.descripcion_dano}</p>
            
            <div class="value">
                <span class="label">⏰ Tiempo requerido por cliente:</span> {reporte.tiempo_requerido_cliente or 'No especificado'}
            </div>
            
            <div class="value">
                <span class="label">📅 Fecha del reporte:</span> {reporte.fecha_reporte.strftime('%d/%m/%Y %H:%M')}
            </div>
            
            <p style="margin-top: 20px;"><strong>Acción requerida:</strong> Revisar el reporte y asignar un técnico disponible.</p>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
            <p>Este es un correo automático, por favor no responder.</p>
        </div>
    </div>
</body>
</html>
"""

                # Contenido texto plano
                text_content = f"""
NUEVO REPORTE DE CLIENTE - DIGIT SOFT

Reporte #{reporte.numero_reporte}
Fecha: {reporte.fecha_reporte.strftime('%d/%m/%Y %H:%M')}

INFORMACIÓN DEL CLIENTE:
- Nombre: {reporte.cliente.nombre_completo}
- Email: {reporte.cliente.email}
- Teléfono: {reporte.cliente.telefono or 'No especificado'}

EQUIPO:
- {reporte.equipo.nombre if reporte.equipo else 'No especificado'}
{f'- Código: {reporte.equipo.codigo_equipo}' if reporte.equipo else ''}

DESCRIPCIÓN DEL DAÑO:
{reporte.descripcion_dano}

TIEMPO REQUERIDO POR CLIENTE:
{reporte.tiempo_requerido_cliente or 'No especificado'}

ACCIÓN REQUERIDA:
Revisar el reporte y asignar un técnico disponible.

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
"""

                # Crear registro de email
                notif_email = NotificacionEmail.objects.create(
                    destinatario=admin.email,
                    asunto=asunto,
                    contenido_texto=text_content,
                    contenido_html=html_content,
                    tipo_notificacion='REPORTE_CLIENTE'
                )

                # Enviar email
                email = EmailMultiAlternatives(
                    subject=asunto,
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[admin.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send(fail_silently=False)

                # Marcar como enviado
                notif_email.enviado = True
                notif_email.estado = 'ENVIADO'
                notif_email.fecha_envio = timezone.now()
                notif_email.save()

                # Crear notificación web
                NotificacionWeb.objects.create(
                    usuario=admin,
                    titulo="Nuevo Reporte de Cliente",
                    mensaje=f"El cliente {reporte.cliente.nombre_completo} ha reportado un equipo dañado. Reporte #{reporte.numero_reporte}",
                    tipo='PRIMARY',
                    icono='fa-file-medical',
                    url=f'/admin/reportes_dano/registrodano/{reporte.id}/change/'
                )

            # Marcar reporte como notificado
            reporte.notificado_admin = True
            reporte.fecha_notificacion_admin = timezone.now()
            reporte.save()

            print(f"✅ Administradores notificados sobre reporte #{reporte.numero_reporte}")
            return True

        except Exception as e:
            print(f"❌ Error al notificar admin: {e}")
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    def notificar_tecnico_asignacion(orden):
        """
        Notifica al técnico sobre una nueva asignación
        Asunto: "Envío de equipo"
        """
        try:
            if not orden.tecnico_asignado:
                print("⚠️ No hay técnico asignado")
                return False

            tecnico = orden.tecnico_asignado

            # Obtener usuario asociado al técnico
            # Asumiendo que el técnico tiene un email
            destinatario = tecnico.correo

            asunto = "Envío de equipo"

            # Contenido HTML
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 30px; text-align: center; }}
        .content {{ padding: 30px; }}
        .info-box {{ background: #e7f3ff; border-left: 4px solid #1e3c72; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .label {{ font-weight: bold; color: #1e3c72; }}
        .value {{ margin-bottom: 10px; }}
        .alert {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">🔧 Nueva Orden Asignada</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT - Sistema de Gestión</p>
        </div>
        <div class="content">
            <h2>Hola {tecnico.nombre_completo},</h2>
            <p>Se te ha asignado una nueva orden de servicio:</p>
            
            <div class="info-box">
                <h3 style="margin-top: 0;">📋 Orden de Servicio #{orden.numero_orden}</h3>
                <div class="value">
                    <span class="label">📅 Fecha de recepción:</span> {orden.fecha_recepcion.strftime('%d/%m/%Y %H:%M')}
                </div>
                <div class="value">
                    <span class="label">⚡ Prioridad:</span> {orden.get_prioridad_display()}
                </div>
            </div>
            
            <div class="info-box">
                <h3 style="margin-top: 0;">👤 Datos del Cliente</h3>
                <div class="value">
                    <span class="label">Nombre:</span> {orden.cliente.nombre_completo}
                </div>
                <div class="value">
                    <span class="label">Email:</span> {orden.cliente.email}
                </div>
                <div class="value">
                    <span class="label">Teléfono:</span> {orden.cliente.telefono or 'No especificado'}
                </div>
            </div>
            
            <div class="info-box">
                <h3 style="margin-top: 0;">💻 Descripción del Equipo</h3>
                <div class="value">
                    <span class="label">Tipo:</span> {orden.tipo_equipo}
                </div>
                <div class="value">
                    <span class="label">Marca:</span> {orden.marca}
                </div>
                <div class="value">
                    <span class="label">Modelo:</span> {orden.modelo}
                </div>
                {f'<div class="value"><span class="label">Serie:</span> {orden.serie}</div>' if orden.serie else ''}
            </div>
            
            <h3>🔍 Falla Reportada:</h3>
            <p style="background: #f8f9fa; padding: 15px; border-radius: 5px;">{orden.falla_reportada}</p>
            
            {f'<div class="alert"><strong>⏰ Tiempo requerido por cliente:</strong> {orden.tiempo_requerido_cliente}</div>' if orden.tiempo_requerido_cliente else ''}
            
            <p style="margin-top: 20px;"><strong>Próximos pasos:</strong></p>
            <ol>
                <li>Revisar el equipo</li>
                <li>Realizar diagnóstico</li>
                <li>Registrar tiempo estimado de reparación</li>
                <li>Actualizar estado de la orden</li>
            </ol>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
            <p>Este es un correo automático, por favor no responder.</p>
        </div>
    </div>
</body>
</html>
"""

            # Contenido texto plano
            text_content = f"""
NUEVA ORDEN ASIGNADA - DIGIT SOFT

Hola {tecnico.nombre_completo},

Se te ha asignado una nueva orden de servicio.

ORDEN DE SERVICIO #{orden.numero_orden}
Fecha de recepción: {orden.fecha_recepcion.strftime('%d/%m/%Y %H:%M')}
Prioridad: {orden.get_prioridad_display()}

DATOS DEL CLIENTE:
- Nombre: {orden.cliente.nombre_completo}
- Email: {orden.cliente.email}
- Teléfono: {orden.cliente.telefono or 'No especificado'}

DESCRIPCIÓN DEL EQUIPO:
- Tipo: {orden.tipo_equipo}
- Marca: {orden.marca}
- Modelo: {orden.modelo}
{f'- Serie: {orden.serie}' if orden.serie else ''}

FALLA REPORTADA:
{orden.falla_reportada}

{f'TIEMPO REQUERIDO POR CLIENTE: {orden.tiempo_requerido_cliente}' if orden.tiempo_requerido_cliente else ''}

PRÓXIMOS PASOS:
1. Revisar el equipo
2. Realizar diagnóstico
3. Registrar tiempo estimado de reparación
4. Actualizar estado de la orden

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
"""

            # Crear registro de email
            notif_email = NotificacionEmail.objects.create(
                destinatario=destinatario,
                asunto=asunto,
                contenido_texto=text_content,
                contenido_html=html_content,
                tipo_notificacion='ASIGNACION_TECNICO',
                orden_servicio=orden
            )

            # Enviar email
            email = EmailMultiAlternatives(
                subject=asunto,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[destinatario]
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

            # Marcar como enviado
            notif_email.enviado = True
            notif_email.estado = 'ENVIADO'
            notif_email.fecha_envio = timezone.now()
            notif_email.save()

            # Buscar usuario del técnico para notificación web
            usuario_tecnico = User.objects.filter(email=tecnico.correo).first()
            if usuario_tecnico:
                NotificacionWeb.objects.create(
                    usuario=usuario_tecnico,
                    titulo="Nueva Orden Asignada",
                    mensaje=f"Se te ha asignado la orden #{orden.numero_orden} del cliente {orden.cliente.nombre_completo}",
                    tipo='SUCCESS',
                    icono='fa-tasks',
                    url=f'/ordenes/{orden.id}/',
                    orden_servicio=orden
                )

            # Marcar orden como notificada
            orden.notificado_tecnico = True
            orden.fecha_notificacion_tecnico = timezone.now()
            orden.save()

            print(f"✅ Técnico {tecnico.nombre_completo} notificado sobre orden #{orden.numero_orden}")
            return True

        except Exception as e:
            print(f"❌ Error al notificar técnico: {e}")
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    def notificar_cliente_orden_servicio(orden):
        """
        Notifica al cliente sobre la orden de servicio con diagnóstico
        Asunto: "Orden de Servicio - [Número]"
        """
        try:
            cliente = orden.cliente
            destinatario = cliente.email

            asunto = f"Orden de Servicio - {orden.numero_orden}"

            # Contenido HTML
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 30px; text-align: center; }}
        .content {{ padding: 30px; }}
        .info-box {{ background: #e7f3ff; border-left: 4px solid #1e3c72; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .label {{ font-weight: bold; color: #1e3c72; }}
        .value {{ margin-bottom: 10px; }}
        .success-box {{ background: #d4edda; border-left: 4px solid #28a745; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">📋 Orden de Servicio</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT - Sistema de Gestión</p>
        </div>
        <div class="content">
            <h2>Estimado/a {cliente.nombre_completo},</h2>
            <p>Nos complace informarle que hemos completado el diagnóstico de su equipo:</p>
            
            <div class="info-box">
                <h3 style="margin-top: 0;">📋 Información de la Orden</h3>
                <div class="value">
                    <span class="label">Número de Orden:</span> {orden.numero_orden}
                </div>
                <div class="value">
                    <span class="label">Fecha de recepción:</span> {orden.fecha_recepcion.strftime('%d/%m/%Y %H:%M')}
                </div>
                <div class="value">
                    <span class="label">Estado:</span> {orden.get_estado_display()}
                </div>
            </div>
            
            <div class="info-box">
                <h3 style="margin-top: 0;">💻 Equipo</h3>
                <div class="value">
                    {orden.tipo_equipo} {orden.marca} {orden.modelo}
                </div>
            </div>
            
            <h3>🔍 Diagnóstico Técnico:</h3>
            <p style="background: #f8f9fa; padding: 15px; border-radius: 5px;">{orden.diagnostico or 'Diagnóstico en proceso'}</p>
            
            {f'<div class="success-box"><h3 style="margin-top: 0;">⏰ Tiempo Estimado de Reparación</h3><p style="font-size: 18px; margin: 0;"><strong>{orden.tiempo_estimado_reparacion} horas</strong></p></div>' if orden.tiempo_estimado_reparacion else ''}
            
            {f'<div class="info-box"><div class="value"><span class="label">📅 Fecha estimada de entrega:</span> {orden.fecha_compromiso.strftime("%d/%m/%Y")}</div></div>' if orden.fecha_compromiso else ''}
            
            {f'<div class="info-box"><h3 style="margin-top: 0;">💰 Costos Estimados</h3><div class="value"><span class="label">Diagnóstico:</span> ${orden.costo_diagnostico}</div><div class="value"><span class="label">Mano de obra:</span> ${orden.costo_mano_obra}</div><div class="value"><span class="label">Repuestos:</span> ${orden.costo_repuestos}</div><div class="value" style="font-size: 18px;"><span class="label">TOTAL:</span> <strong>${orden.costo_total}</strong></div></div>' if orden.costo_total > 0 else ''}
            
            <p style="margin-top: 20px;">Si tiene alguna pregunta, no dude en contactarnos.</p>
            
            <p><strong>Gracias por confiar en DIGIT SOFT</strong></p>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
            <p>Este es un correo automático, por favor no responder.</p>
        </div>
    </div>
</body>
</html>
"""

            # Contenido texto plano
            text_content = f"""
ORDEN DE SERVICIO - DIGIT SOFT

Estimado/a {cliente.nombre_completo},

Nos complace informarle que hemos completado el diagnóstico de su equipo.

INFORMACIÓN DE LA ORDEN:
- Número de Orden: {orden.numero_orden}
- Fecha de recepción: {orden.fecha_recepcion.strftime('%d/%m/%Y %H:%M')}
- Estado: {orden.get_estado_display()}

EQUIPO:
{orden.tipo_equipo} {orden.marca} {orden.modelo}

DIAGNÓSTICO TÉCNICO:
{orden.diagnostico or 'Diagnóstico en proceso'}

{f'TIEMPO ESTIMADO DE REPARACIÓN: {orden.tiempo_estimado_reparacion} horas' if orden.tiempo_estimado_reparacion else ''}

{f'FECHA ESTIMADA DE ENTREGA: {orden.fecha_compromiso.strftime("%d/%m/%Y")}' if orden.fecha_compromiso else ''}

{f'''COSTOS ESTIMADOS:
- Diagnóstico: ${orden.costo_diagnostico}
- Mano de obra: ${orden.costo_mano_obra}
- Repuestos: ${orden.costo_repuestos}
- TOTAL: ${orden.costo_total}''' if orden.costo_total > 0 else ''}

Si tiene alguna pregunta, no dude en contactarnos.

Gracias por confiar en DIGIT SOFT

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
"""

            # Crear registro de email
            notif_email = NotificacionEmail.objects.create(
                destinatario=destinatario,
                asunto=asunto,
                contenido_texto=text_content,
                contenido_html=html_content,
                tipo_notificacion='ORDEN_SERVICIO_CLIENTE',
                orden_servicio=orden
            )

            # Enviar email
            email = EmailMultiAlternatives(
                subject=asunto,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[destinatario]
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

            # Marcar como enviado
            notif_email.enviado = True
            notif_email.estado = 'ENVIADO'
            notif_email.fecha_envio = timezone.now()
            notif_email.save()

            # Buscar usuario del cliente para notificación web
            usuario_cliente = User.objects.filter(email=cliente.email).first()
            if usuario_cliente:
                NotificacionWeb.objects.create(
                    usuario=usuario_cliente,
                    titulo="Orden de Servicio Disponible",
                    mensaje=f"Su orden #{orden.numero_orden} ha sido diagnosticada. Tiempo estimado: {orden.tiempo_estimado_reparacion} horas." if orden.tiempo_estimado_reparacion else f"Su orden #{orden.numero_orden} ha sido diagnosticada.",
                    tipo='INFO',
                    icono='fa-file-alt',
                    url=f'/ordenes/{orden.id}/',
                    orden_servicio=orden
                )

            # Marcar orden como notificada
            orden.notificado_cliente = True
            orden.fecha_notificacion_cliente = timezone.now()
            orden.save()

            print(f"✅ Cliente {cliente.nombre_completo} notificado sobre orden #{orden.numero_orden}")
            return True

        except Exception as e:
            print(f"❌ Error al notificar cliente: {e}")
            import traceback
            traceback.print_exc()
            return False

