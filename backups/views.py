"""
DIGIT SOFT - Módulo de Backups
Views
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from django.core.paginator import Paginator
from core.decorators import admin_required
from .models import Backup, ConfiguracionBackup
from .services import BackupService
import os


@login_required
@admin_required
def lista_backups(request):
    """Lista de backups disponibles"""
    backups_list = Backup.objects.all().order_by('-fecha_creacion')

    # Paginación
    paginator = Paginator(backups_list, 10)
    page = request.GET.get('page', 1)
    backups = paginator.get_page(page)

    # Obtener configuración
    config, created = ConfiguracionBackup.objects.get_or_create(defaults={
        'activo': False,
        'frecuencia_horas': 24,
        'max_backups': 10
    })

    context = {
        'backups': backups,
        'config': config,
        'total_backups': backups_list.count(),
    }

    return render(request, 'backups/lista.html', context)


@login_required
@admin_required
def crear_backup(request):
    """Crear un nuevo backup"""
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion', '')

        service = BackupService()
        resultado = service.crear_backup(
            usuario=request.user,
            tipo='MANUAL',
            descripcion=descripcion
        )

        if resultado['success']:
            messages.success(request, f'✅ {resultado["mensaje"]}')
        else:
            messages.error(request, f'❌ {resultado["mensaje"]}')

        return redirect('backups:lista')

    return render(request, 'backups/crear.html')


@login_required
@admin_required
def restaurar_backup(request, backup_id):
    """Restaurar un backup"""
    backup = get_object_or_404(Backup, pk=backup_id)

    if request.method == 'POST':
        confirmacion = request.POST.get('confirmacion', '')

        if confirmacion == 'CONFIRMAR':
            service = BackupService()
            resultado = service.restaurar_backup(backup_id, request.user)

            if resultado['success']:
                messages.success(request, f'✅ {resultado["mensaje"]}')
                messages.warning(request, '⚠️ Por favor reinicie el servidor para aplicar los cambios')
            else:
                messages.error(request, f'❌ {resultado["mensaje"]}')

            return redirect('backups:lista')
        else:
            messages.error(request, '❌ Debe escribir CONFIRMAR para restaurar el backup')

    context = {
        'backup': backup
    }

    return render(request, 'backups/restaurar.html', context)


@login_required
@admin_required
def descargar_backup(request, backup_id):
    """Descargar un backup"""
    backup = get_object_or_404(Backup, pk=backup_id)

    service = BackupService()
    archivo = service.descargar_backup(backup_id)

    if archivo and os.path.exists(archivo):
        response = FileResponse(open(archivo, 'rb'))
        response['Content-Type'] = 'application/zip'
        response['Content-Disposition'] = f'attachment; filename="{backup.nombre}.zip"'
        return response
    else:
        messages.error(request, '❌ Archivo de backup no encontrado')
        return redirect('backups:lista')


@login_required
@admin_required
def eliminar_backup(request, backup_id):
    """Eliminar un backup"""
    if request.method == 'POST':
        service = BackupService()
        resultado = service.eliminar_backup(backup_id)

        if resultado['success']:
            messages.success(request, f'✅ {resultado["mensaje"]}')
        else:
            messages.error(request, f'❌ {resultado["mensaje"]}')

    return redirect('backups:lista')


@login_required
@admin_required
def configuracion_backups(request):
    """Configuración de backups automáticos"""
    config, created = ConfiguracionBackup.objects.get_or_create(defaults={
        'activo': False,
        'frecuencia_horas': 24,
        'max_backups': 10
    })

    if request.method == 'POST':
        config.activo = request.POST.get('activo') == 'on'
        config.frecuencia_horas = int(request.POST.get('frecuencia_horas', 24))
        config.max_backups = int(request.POST.get('max_backups', 10))
        config.incluir_media = request.POST.get('incluir_media') == 'on'
        config.notificar_admin = request.POST.get('notificar_admin') == 'on'
        config.save()

        messages.success(request, '✅ Configuración guardada exitosamente')
        return redirect('backups:configuracion')

    context = {
        'config': config
    }

    return render(request, 'backups/configuracion.html', context)

