"""
Sistema de Notificaciones Automáticas para Órdenes de Servicio
Gestiona notificaciones por email, in-app y alertas al administrador
"""

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.models import User
from usuarios.models import Notificacion
from datetime import datetime, timedelta
from django.utils import timezone


class ServicioNotificaciones:
    """Servicio centralizado para gestionar todas las notificaciones del sistema"""

    @staticmethod
    def notificar_nueva_orden_admin(orden):
        """
        Notifica al administrador cuando se crea una nueva orden de servicio
        """
        # Crear notificación in-app para administradores
        admins = User.objects.filter(is_staff=True, is_active=True)

        for admin in admins:
            Notificacion.objects.create(
                usuario=admin,
                tipo='ORDEN_NUEVA',
                titulo=f'🔔 Nueva Orden de Servicio: {orden.numero_orden}',
                mensaje=f'Cliente: {orden.cliente.nombre_completo}\n'
                        f'Equipo: {orden.tipo_equipo} {orden.marca} {orden.modelo}\n'
                        f'Falla: {orden.falla_reportada[:100]}...',
                url=f'/ordenes/{orden.pk}/',
                icono='fas fa-tools',
                color='primary',
                prioridad='ALTA'
            )

        # Enviar email al administrador principal
        try:
            admin_email = settings.ADMIN_EMAIL if hasattr(settings, 'ADMIN_EMAIL') else admins.first().email

            contexto = {
                'orden': orden,
                'cliente': orden.cliente,
                'url_orden': f'{settings.SITE_URL}/ordenes/{orden.pk}/',
            }

            html_content = render_to_string('emails/nueva_orden_admin.html', contexto)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject=f'Nueva Orden de Servicio - {orden.numero_orden}',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[admin_email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return True
        except Exception as e:
            print(f"Error enviando email al admin: {e}")
            return False

    @staticmethod
    def notificar_cambio_estado_cliente(orden, estado_anterior, estado_nuevo, descripcion=''):
        """
        Notifica al cliente cuando cambia el estado de su orden
        """
        cliente = orden.cliente

        # Crear notificación in-app
        mensajes_estado = {
            'RECIBIDA': '📥 Su equipo ha sido recibido y está siendo registrado en nuestro sistema.',
            'EN_DIAGNOSTICO': '🔍 Su equipo está siendo diagnosticado por nuestros técnicos.',
            'EN_REPARACION': '🔧 Su equipo está siendo reparado. Le notificaremos cuando esté listo.',
            'ESPERANDO_REPUESTOS': '📦 Estamos esperando la llegada de repuestos necesarios.',
            'LISTA_ENTREGA': '✅ ¡Buenas noticias! Su equipo está listo para retirar.',
            'ENTREGADA': '🎉 Su equipo ha sido entregado. ¡Gracias por confiar en nosotros!',
            'CANCELADA': '❌ Su orden ha sido cancelada.',
        }

        mensaje = mensajes_estado.get(estado_nuevo, 'Su orden ha cambiado de estado.')
        if descripcion:
            mensaje += f'\n\nDetalles: {descripcion}'

        # Crear notificación in-app para el cliente
        try:
            if hasattr(cliente, 'usuario') and cliente.usuario:
                Notificacion.objects.create(
                    usuario=cliente.usuario,
                    tipo='CAMBIO_ESTADO',
                    titulo=f'Actualización: Orden {orden.numero_orden}',
                    mensaje=mensaje,
                    url=f'/ordenes/{orden.pk}/',
                    icono='fas fa-sync-alt',
                    color='info',
                    prioridad='MEDIA'
                )
        except Exception as e:
            print(f"Error creando notificación in-app: {e}")

        # Enviar email al cliente
        try:
            if cliente.email:
                contexto = {
                    'orden': orden,
                    'cliente': cliente,
                    'estado_anterior': estado_anterior,
                    'estado_nuevo': estado_nuevo,
                    'descripcion': descripcion,
                    'mensaje': mensaje,
                    'url_orden': f'{settings.SITE_URL}/ordenes/{orden.pk}/',
                }

                html_content = render_to_string('emails/cambio_estado_cliente.html', contexto)
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject=f'Actualización de su Orden {orden.numero_orden}',
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[cliente.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

                return True
        except Exception as e:
            print(f"Error enviando email al cliente: {e}")
            return False

    @staticmethod
    def notificar_demora_detectada(orden, dias_demora):
        """
        Notifica al administrador cuando se detecta una demora en una orden
        """
        admins = User.objects.filter(is_staff=True, is_active=True)

        for admin in admins:
            Notificacion.objects.create(
                usuario=admin,
                tipo='DEMORA',
                titulo=f'⚠️ Demora Detectada: {orden.numero_orden}',
                mensaje=f'La orden lleva {dias_demora} días sin actualización.\n'
                        f'Cliente: {orden.cliente.nombre_completo}\n'
                        f'Estado actual: {orden.get_estado_display()}',
                url=f'/ordenes/{orden.pk}/',
                icono='fas fa-exclamation-triangle',
                color='warning',
                prioridad='ALTA'
            )

        return True

    @staticmethod
    def notificar_orden_lista_entrega(orden):
        """
        Notifica al cliente cuando su orden está lista para retirar
        """
        cliente = orden.cliente

        # Notificación in-app
        try:
            if hasattr(cliente, 'usuario') and cliente.usuario:
                Notificacion.objects.create(
                    usuario=cliente.usuario,
                    tipo='LISTA_ENTREGA',
                    titulo=f'✅ ¡Su equipo está listo!',
                    mensaje=f'Orden {orden.numero_orden}: Su {orden.tipo_equipo} {orden.marca} está listo para retirar.\n'
                            f'Costo total: ${orden.costo_total:,.0f}',
                    url=f'/ordenes/{orden.pk}/',
                    icono='fas fa-check-circle',
                    color='success',
                    prioridad='ALTA'
                )
        except Exception as e:
            print(f"Error creando notificación: {e}")

        # Email al cliente
        try:
            if cliente.email:
                contexto = {
                    'orden': orden,
                    'cliente': cliente,
                    'url_orden': f'{settings.SITE_URL}/ordenes/{orden.pk}/',
                }

                html_content = render_to_string('emails/orden_lista.html', contexto)
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject=f'¡Su equipo está listo! - Orden {orden.numero_orden}',
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[cliente.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

                return True
        except Exception as e:
            print(f"Error enviando email: {e}")
            return False

    @staticmethod
    def enviar_recordatorio_recuperacion_password(usuario, token):
        """
        Envía enlace seguro de recuperación de contraseña
        """
        try:
            reset_url = f'{settings.SITE_URL}/reset-password/{token}/'

            contexto = {
                'usuario': usuario,
                'reset_url': reset_url,
                'vigencia_horas': 24,
            }

            html_content = render_to_string('emails/recuperacion_password.html', contexto)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject='Recuperación de Contraseña - DIGIT SOFT',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[usuario.email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return True
        except Exception as e:
            print(f"Error enviando email de recuperación: {e}")
            return False

    @staticmethod
    def notificar_asignacion_tecnico(orden, tecnico):
        """
        Notifica al técnico cuando se le asigna una orden de servicio
        """
        # Notificación in-app
        try:
            if hasattr(tecnico, 'usuario') and tecnico.usuario:
                Notificacion.objects.create(
                    usuario=tecnico.usuario,
                    tipo='ORDEN_ASIGNADA',
                    titulo=f'🔧 Nueva Orden Asignada: {orden.numero_orden}',
                    mensaje=f'Se te ha asignado la orden {orden.numero_orden}\n'
                            f'Cliente: {orden.cliente.nombre_completo}\n'
                            f'Equipo: {orden.tipo_equipo} {orden.marca} {orden.modelo}\n'
                            f'Prioridad: {orden.get_prioridad_display()}',
                    url=f'/ordenes/{orden.pk}/',
                    icono='fas fa-wrench',
                    color='info',
                    prioridad='ALTA' if orden.prioridad in ['ALTA', 'URGENTE'] else 'MEDIA'
                )
        except Exception as e:
            print(f"Error creando notificación in-app para técnico: {e}")

        # Email al técnico
        try:
            if tecnico.email:
                contexto = {
                    'orden': orden,
                    'tecnico': tecnico,
                    'url_orden': f'{settings.SITE_URL}/ordenes/{orden.pk}/',
                }

                html_content = render_to_string('emails/orden_asignada_tecnico.html', contexto)
                text_content = strip_tags(html_content)

                subject = f'Nueva Orden Asignada - {orden.numero_orden}'
                if orden.prioridad == 'URGENTE':
                    subject = f'🚨 URGENTE - {subject}'

                email = EmailMultiAlternatives(
                    subject=subject,
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[tecnico.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

                return True
        except Exception as e:
            print(f"Error enviando email al técnico: {e}")
            return False

    @staticmethod
    def notificar_tecnico_a_admin(orden, tecnico, tipo, mensaje, nueva_fecha=None):
        """
        Notifica al administrador cuando el técnico reporta una demora o adelanto
        tipo: 'DEMORA', 'ADELANTO', 'INCIDENCIA', 'ACTUALIZACIÓN'
        """
        # Notificación in-app para administradores
        admins = User.objects.filter(is_staff=True, is_active=True)

        iconos_tipo = {
            'DEMORA': 'fas fa-exclamation-triangle',
            'ADELANTO': 'fas fa-check-circle',
            'INCIDENCIA': 'fas fa-tools',
            'ACTUALIZACIÓN': 'fas fa-info-circle'
        }

        colores_tipo = {
            'DEMORA': 'warning',
            'ADELANTO': 'success',
            'INCIDENCIA': 'danger',
            'ACTUALIZACIÓN': 'info'
        }

        for admin in admins:
            Notificacion.objects.create(
                usuario=admin,
                tipo=f'TECNICO_{tipo}',
                titulo=f'{tipo}: Orden {orden.numero_orden}',
                mensaje=f'Técnico: {tecnico.nombre_completo}\n'
                        f'{mensaje}',
                url=f'/ordenes/{orden.pk}/',
                icono=iconos_tipo.get(tipo, 'fas fa-bell'),
                color=colores_tipo.get(tipo, 'info'),
                prioridad='ALTA' if tipo in ['DEMORA', 'INCIDENCIA'] else 'MEDIA'
            )

        # Email al administrador principal
        try:
            admin_email = settings.ADMIN_EMAIL if hasattr(settings, 'ADMIN_EMAIL') else admins.first().email

            contexto = {
                'orden': orden,
                'tecnico': tecnico,
                'tipo': tipo,
                'mensaje': mensaje,
                'nueva_fecha': nueva_fecha,
                'url_orden': f'{settings.SITE_URL}/ordenes/{orden.pk}/',
            }

            html_content = render_to_string('emails/notificacion_tecnico_admin.html', contexto)
            text_content = strip_tags(html_content)

            subject_prefix = {
                'DEMORA': '⚠️ Demora Reportada',
                'ADELANTO': '✅ Adelanto Reportado',
                'INCIDENCIA': '🚨 Incidencia',
                'ACTUALIZACIÓN': '📝 Actualización'
            }

            email = EmailMultiAlternatives(
                subject=f'{subject_prefix.get(tipo, "Notificación")} - Orden {orden.numero_orden}',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[admin_email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return True
        except Exception as e:
            print(f"Error enviando email al admin: {e}")
            return False


class MonitorDemoras:
    """Monitorea y detecta demoras en las órdenes de servicio"""

    @staticmethod
    def detectar_demoras():
        """
        Revisa todas las órdenes activas y detecta las que están demoradas
        """
        from ordenes.models import OrdenServicio

        # Órdenes activas (no entregadas ni canceladas)
        ordenes_activas = OrdenServicio.objects.exclude(
            estado__in=['ENTREGADA', 'CANCELADA']
        )

        demoras_detectadas = []

        for orden in ordenes_activas:
            # Verificar si pasó la fecha de compromiso
            if orden.fecha_compromiso and timezone.now() > orden.fecha_compromiso:
                dias_demora = (timezone.now() - orden.fecha_compromiso).days

                if dias_demora > 0:
                    # Registrar demora
                    demoras_detectadas.append({
                        'orden': orden,
                        'dias_demora': dias_demora,
                        'fecha_compromiso': orden.fecha_compromiso,
                    })

                    # Notificar al administrador
                    ServicioNotificaciones.notificar_demora_detectada(orden, dias_demora)

        return demoras_detectadas

    @staticmethod
    def registrar_novedad(orden, tipo, descripcion, usuario=None):
        """
        Registra una novedad en la orden de servicio
        """
        from ordenes.models import SeguimientoOrden

        novedad = SeguimientoOrden.objects.create(
            orden=orden,
            estado_anterior=orden.estado,
            estado_nuevo=orden.estado,
            descripcion=f'[{tipo}] {descripcion}',
            usuario=usuario.username if usuario else 'Sistema'
        )

        # Notificar según el tipo de novedad
        if tipo in ['DEMORA', 'INCIDENCIA']:
            ServicioNotificaciones.notificar_demora_detectada(
                orden,
                (timezone.now() - orden.fecha_recepcion).days
            )

        return novedad

