"""
Script para limpiar conflictos de perfiles duplicados
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import UserProfile
from usuarios.models import PerfilUsuario


class Command(BaseCommand):
    help = 'Limpia perfiles duplicados y migra datos de UserProfile a PerfilUsuario'

    def handle(self, *args, **kwargs):
        self.stdout.write('🔧 Iniciando limpieza de perfiles...')

        # 1. Eliminar UserProfile huérfanos (sin usuario correspondiente)
        huerfanos = UserProfile.objects.filter(user__isnull=True)
        count_huerfanos = huerfanos.count()
        if count_huerfanos > 0:
            huerfanos.delete()
            self.stdout.write(self.style.SUCCESS(f'✅ Eliminados {count_huerfanos} UserProfile huérfanos'))

        # 2. Para cada usuario, asegurarse de que tenga solo PerfilUsuario
        usuarios = User.objects.all()
        migrados = 0
        eliminados = 0

        for user in usuarios:
            # Verificar si tiene UserProfile
            try:
                old_profile = UserProfile.objects.get(user=user)

                # Verificar si ya tiene PerfilUsuario
                try:
                    new_profile = PerfilUsuario.objects.get(user=user)
                    # Ya tiene el nuevo perfil, eliminar el viejo
                    old_profile.delete()
                    eliminados += 1
                    self.stdout.write(f'🗑️  Eliminado UserProfile duplicado para {user.username}')
                except PerfilUsuario.DoesNotExist:
                    # No tiene PerfilUsuario, migrar datos
                    new_profile = PerfilUsuario.objects.create(
                        user=user,
                        tipo_usuario='CLIENTE' if old_profile.role == 'cliente' else 'ADMIN',
                        telefono=old_profile.phone or '',
                        documento=old_profile.documento or '',
                        activo=True
                    )
                    old_profile.delete()
                    migrados += 1
                    self.stdout.write(f'✅ Migrado perfil de {user.username}')

            except UserProfile.DoesNotExist:
                # No tiene UserProfile viejo, verificar que tenga el nuevo
                try:
                    PerfilUsuario.objects.get(user=user)
                except PerfilUsuario.DoesNotExist:
                    # No tiene ningún perfil, crear uno nuevo
                    PerfilUsuario.objects.create(user=user)
                    self.stdout.write(f'✨ Creado nuevo perfil para {user.username}')

        self.stdout.write(self.style.SUCCESS(f'\n📊 Resumen:'))
        self.stdout.write(self.style.SUCCESS(f'   - Perfiles migrados: {migrados}'))
        self.stdout.write(self.style.SUCCESS(f'   - Perfiles duplicados eliminados: {eliminados}'))
        self.stdout.write(self.style.SUCCESS(f'   - Total usuarios: {usuarios.count()}'))
        self.stdout.write(self.style.SUCCESS(f'\n✅ Limpieza completada!'))

