"""
Vistas para el Sistema de Ayuda y Soporte
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import TicketAyuda, RespuestaTicket, FAQ, CategoriaAyuda
from .forms import CrearTicketForm, ResponderTicketForm, BuscarFAQForm


@login_required
def centro_ayuda(request):
    """Página principal del centro de ayuda"""
    # FAQs más populares
    faqs_populares = FAQ.objects.filter(activo=True).order_by('-vistas')[:5]

    # Tickets recientes del usuario
    tickets_usuario = TicketAyuda.objects.filter(usuario=request.user).order_by('-fecha_creacion')[:5]

    # Categorías disponibles
    categorias = CategoriaAyuda.objects.filter(activo=True)

    # Estadísticas del usuario
    total_tickets = TicketAyuda.objects.filter(usuario=request.user).count()
    tickets_abiertos = TicketAyuda.objects.filter(usuario=request.user, estado='abierto').count()
    tickets_resueltos = TicketAyuda.objects.filter(usuario=request.user, estado='resuelto').count()

    context = {
        'faqs_populares': faqs_populares,
        'tickets_usuario': tickets_usuario,
        'categorias': categorias,
        'total_tickets': total_tickets,
        'tickets_abiertos': tickets_abiertos,
        'tickets_resueltos': tickets_resueltos,
    }

    return render(request, 'ayuda/centro_ayuda.html', context)


@login_required
def crear_ticket(request):
    """Crear un nuevo ticket de ayuda"""
    if request.method == 'POST':
        form = CrearTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user

            # Capturar información adicional
            ticket.ip_usuario = get_client_ip(request)
            ticket.navegador = request.META.get('HTTP_USER_AGENT', '')[:200]

            ticket.save()

            messages.success(
                request,
                f'✅ Ticket #{ticket.pk} creado exitosamente. '
                f'Te responderemos pronto.'
            )
            return redirect('ayuda:ver_ticket', ticket_id=ticket.pk)
        else:
            messages.error(request, '❌ Error al crear el ticket. Verifica los datos.')
    else:
        form = CrearTicketForm()

    return render(request, 'ayuda/crear_ticket.html', {'form': form})


@login_required
def ver_ticket(request, ticket_id):
    """Ver detalles de un ticket y sus respuestas"""
    ticket = get_object_or_404(TicketAyuda, pk=ticket_id)

    # Verificar que el usuario sea el dueño o staff
    if ticket.usuario != request.user and not request.user.is_staff:
        messages.error(request, '❌ No tienes permiso para ver este ticket.')
        return redirect('ayuda:mis_tickets')

    # Responder al ticket
    if request.method == 'POST':
        form = ResponderTicketForm(request.POST, request.FILES)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.ticket = ticket
            respuesta.usuario = request.user
            respuesta.es_staff = request.user.is_staff
            respuesta.save()

            # Actualizar estado del ticket
            if ticket.estado == 'abierto':
                ticket.estado = 'en_proceso'
            elif respuesta.es_staff:
                ticket.estado = 'respondido'

            ticket.save()

            messages.success(request, '✅ Respuesta agregada correctamente.')
            return redirect('ayuda:ver_ticket', ticket_id=ticket.pk)
    else:
        form = ResponderTicketForm()

    # Obtener respuestas
    respuestas = ticket.respuestas.all().order_by('fecha_creacion')

    context = {
        'ticket': ticket,
        'respuestas': respuestas,
        'form': form
    }

    return render(request, 'ayuda/ver_ticket.html', context)


@login_required
def mis_tickets(request):
    """Lista de tickets del usuario"""
    # Filtros
    estado_filtro = request.GET.get('estado', '')

    tickets = TicketAyuda.objects.filter(usuario=request.user)

    if estado_filtro:
        tickets = tickets.filter(estado=estado_filtro)

    tickets = tickets.order_by('-fecha_creacion')

    # Paginación
    paginator = Paginator(tickets, 10)
    page = request.GET.get('page', 1)
    tickets_paginados = paginator.get_page(page)

    context = {
        'tickets': tickets_paginados,
        'estado_filtro': estado_filtro,
        'total_tickets': tickets.count()
    }

    return render(request, 'ayuda/mis_tickets.html', context)


@login_required
def cerrar_ticket(request, ticket_id):
    """Cerrar un ticket"""
    ticket = get_object_or_404(TicketAyuda, pk=ticket_id)

    # Verificar permisos
    if ticket.usuario != request.user and not request.user.is_staff:
        messages.error(request, '❌ No tienes permiso para cerrar este ticket.')
        return redirect('ayuda:mis_tickets')

    ticket.marcar_resuelto()
    ticket.estado = 'cerrado'
    ticket.save()

    messages.success(request, f'✅ Ticket #{ticket.pk} cerrado exitosamente.')
    return redirect('ayuda:ver_ticket', ticket_id=ticket.pk)


def faqs(request):
    """Página de preguntas frecuentes"""
    form = BuscarFAQForm(request.GET or None)

    faqs_lista = FAQ.objects.filter(activo=True)

    # Buscar
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        categoria = form.cleaned_data.get('categoria')

        if busqueda:
            faqs_lista = faqs_lista.filter(
                Q(pregunta__icontains=busqueda) |
                Q(respuesta__icontains=busqueda)
            )

        if categoria:
            faqs_lista = faqs_lista.filter(categoria_id=categoria)

    faqs_lista = faqs_lista.order_by('orden', '-fecha_creacion')

    # Categorías para el filtro
    categorias = CategoriaAyuda.objects.filter(activo=True)

    context = {
        'faqs': faqs_lista,
        'form': form,
        'categorias': categorias,
        'total_faqs': faqs_lista.count()
    }

    return render(request, 'ayuda/faqs.html', context)


def ver_faq(request, faq_id):
    """Ver una FAQ específica"""
    faq = get_object_or_404(FAQ, pk=faq_id, activo=True)

    # Incrementar contador de vistas
    faq.incrementar_vista()

    # FAQs relacionadas de la misma categoría
    faqs_relacionadas = FAQ.objects.filter(
        categoria=faq.categoria,
        activo=True
    ).exclude(pk=faq.pk)[:5]

    context = {
        'faq': faq,
        'faqs_relacionadas': faqs_relacionadas
    }

    return render(request, 'ayuda/ver_faq.html', context)


def get_client_ip(request):
    """Obtiene la IP del cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

