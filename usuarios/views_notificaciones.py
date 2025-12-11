# ==================== NOTIFICACIONES ====================

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Notificacion


@login_required
def listar_notificaciones(request):
    """Vista para listar todas las notificaciones del usuario"""
    notificaciones = request.user.notificaciones.all()[:50]  # Últimas 50
    
    # Contar no leídas
    no_leidas = request.user.notificaciones.filter(leida=False).count()
    
    context = {
        'notificaciones': notificaciones,
        'no_leidas': no_leidas
    }
    return render(request, 'usuarios/notificaciones.html', context)


@login_required
def notificaciones_json(request):
    """Vista AJAX para obtener notificaciones en JSON"""
    notificaciones = request.user.notificaciones.filter(leida=False)[:10]
    
    data = {
        'count': notificaciones.count(),
        'notificaciones': [
            {
                'id': n.id,
                'titulo': n.titulo,
                'mensaje': n.mensaje[:100] + '...' if len(n.mensaje) > 100 else n.mensaje,
                'tipo': n.tipo,
                'icono': n.get_icono(),
                'color': n.get_color(),
                'url': n.url,
                'tiempo': n.tiempo_transcurrido
            }
            for n in notificaciones
        ]
    }
    
    return JsonResponse(data)


@login_required
@require_http_methods(["POST"])
def marcar_notificacion_leida(request, notificacion_id):
    """Marca una notificación como leída"""
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notificacion.marcar_como_leida()
    
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def marcar_todas_leidas(request):
    """Marca todas las notificaciones como leídas"""
    request.user.notificaciones.filter(leida=False).update(leida=True)
    messages.success(request, 'Todas las notificaciones marcadas como leídas.')
    
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def eliminar_notificacion(request, notificacion_id):
    """Elimina una notificación"""
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notificacion.delete()
    
    return JsonResponse({'success': True})


def debug_notificaciones(request):
    """Página de debug para notificaciones"""
    return render(request, 'debug_notificaciones.html')



