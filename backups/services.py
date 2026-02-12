"""
DIGIT SOFT - Módulo de Backups
Servicios para gestión de copias de seguridad
"""

import os
import subprocess
import shutil
import zipfile
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from .models import Backup, ConfiguracionBackup


class BackupService:
    """Servicio para crear y gestionar backups de la base de datos"""

    def __init__(self):
        self.backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        self.ensure_backup_directory()

    def ensure_backup_directory(self):
        """Asegurar que existe el directorio de backups"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def crear_backup(self, usuario=None, tipo='MANUAL', descripcion=''):
        """Crear un backup de la base de datos"""
        try:
            # Generar nombre único
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre = f'backup_{timestamp}'

            # Crear registro en BD
            backup = Backup.objects.create(
                nombre=nombre,
                tipo=tipo,
                estado='EN_PROCESO',
                usuario=usuario,
                descripcion=descripcion
            )

            # Determinar tipo de base de datos
            db_config = settings.DATABASES['default']
            db_engine = db_config['ENGINE']

            archivo_backup = None

            if 'sqlite' in db_engine:
                archivo_backup = self._backup_sqlite(nombre, db_config)
            elif 'mysql' in db_engine:
                archivo_backup = self._backup_mysql(nombre, db_config)
            elif 'postgresql' in db_engine:
                archivo_backup = self._backup_postgresql(nombre, db_config)
            else:
                raise Exception(f'Base de datos no soportada: {db_engine}')

            # Actualizar registro
            if archivo_backup and os.path.exists(archivo_backup):
                backup.archivo = archivo_backup
                backup.tamaño = os.path.getsize(archivo_backup)
                backup.estado = 'EXITOSO'
                backup.save()

                # Limpiar backups antiguos
                self.limpiar_backups_antiguos()

                return {'success': True, 'backup': backup, 'mensaje': 'Backup creado exitosamente'}
            else:
                backup.estado = 'FALLIDO'
                backup.error_mensaje = 'Archivo de backup no creado'
                backup.save()
                return {'success': False, 'mensaje': 'Error al crear el archivo de backup'}

        except Exception as e:
            if 'backup' in locals():
                backup.estado = 'FALLIDO'
                backup.error_mensaje = str(e)
                backup.save()
            return {'success': False, 'mensaje': f'Error: {str(e)}'}

    def _backup_sqlite(self, nombre, db_config):
        """Crear backup de SQLite"""
        db_path = db_config['NAME']
        backup_file = os.path.join(self.backup_dir, f'{nombre}.db')

        # Copiar archivo de base de datos
        shutil.copy2(db_path, backup_file)

        # Comprimir
        zip_file = f'{backup_file}.zip'
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(backup_file, os.path.basename(backup_file))

        # Eliminar archivo sin comprimir
        os.remove(backup_file)

        return zip_file

    def _backup_mysql(self, nombre, db_config):
        """Crear backup de MySQL"""
        backup_file = os.path.join(self.backup_dir, f'{nombre}.sql')

        cmd = [
            'mysqldump',
            f"--user={db_config.get('USER', '')}",
            f"--password={db_config.get('PASSWORD', '')}",
            f"--host={db_config.get('HOST', 'localhost')}",
            f"--port={db_config.get('PORT', 3306)}",
            db_config.get('NAME', ''),
            f'--result-file={backup_file}'
        ]

        subprocess.run(cmd, check=True)

        # Comprimir
        zip_file = f'{backup_file}.zip'
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(backup_file, os.path.basename(backup_file))

        os.remove(backup_file)

        return zip_file

    def _backup_postgresql(self, nombre, db_config):
        """Crear backup de PostgreSQL"""
        backup_file = os.path.join(self.backup_dir, f'{nombre}.sql')

        env = os.environ.copy()
        env['PGPASSWORD'] = db_config.get('PASSWORD', '')

        cmd = [
            'pg_dump',
            f"--host={db_config.get('HOST', 'localhost')}",
            f"--port={db_config.get('PORT', 5432)}",
            f"--username={db_config.get('USER', '')}",
            f"--dbname={db_config.get('NAME', '')}",
            f'--file={backup_file}'
        ]

        subprocess.run(cmd, env=env, check=True)

        # Comprimir
        zip_file = f'{backup_file}.zip'
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(backup_file, os.path.basename(backup_file))

        os.remove(backup_file)

        return zip_file

    def restaurar_backup(self, backup_id, usuario=None):
        """Restaurar un backup"""
        try:
            backup = Backup.objects.get(pk=backup_id)

            if not os.path.exists(backup.archivo):
                return {'success': False, 'mensaje': 'Archivo de backup no encontrado'}

            # Determinar tipo de BD
            db_config = settings.DATABASES['default']
            db_engine = db_config['ENGINE']

            # Extraer archivo comprimido
            extract_dir = os.path.join(self.backup_dir, 'temp')
            os.makedirs(extract_dir, exist_ok=True)

            with zipfile.ZipFile(backup.archivo, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            # Obtener archivo extraído
            extracted_files = os.listdir(extract_dir)
            if not extracted_files:
                return {'success': False, 'mensaje': 'No se pudo extraer el backup'}

            extracted_file = os.path.join(extract_dir, extracted_files[0])

            # Restaurar según tipo de BD
            if 'sqlite' in db_engine:
                resultado = self._restaurar_sqlite(extracted_file, db_config)
            elif 'mysql' in db_engine:
                resultado = self._restaurar_mysql(extracted_file, db_config)
            elif 'postgresql' in db_engine:
                resultado = self._restaurar_postgresql(extracted_file, db_config)
            else:
                resultado = {'success': False, 'mensaje': 'BD no soportada'}

            # Limpiar archivos temporales
            shutil.rmtree(extract_dir)

            return resultado

        except Backup.DoesNotExist:
            return {'success': False, 'mensaje': 'Backup no encontrado'}
        except Exception as e:
            return {'success': False, 'mensaje': f'Error: {str(e)}'}

    def _restaurar_sqlite(self, backup_file, db_config):
        """Restaurar SQLite"""
        db_path = db_config['NAME']

        # Crear backup de la BD actual antes de restaurar
        backup_actual = f'{db_path}.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        shutil.copy2(db_path, backup_actual)

        try:
            # Reemplazar BD actual
            shutil.copy2(backup_file, db_path)
            return {'success': True, 'mensaje': 'Base de datos restaurada exitosamente'}
        except Exception as e:
            # Restaurar backup si falla
            shutil.copy2(backup_actual, db_path)
            return {'success': False, 'mensaje': f'Error al restaurar: {str(e)}'}

    def _restaurar_mysql(self, backup_file, db_config):
        """Restaurar MySQL"""
        try:
            with open(backup_file, 'r') as f:
                cmd = [
                    'mysql',
                    f"--user={db_config.get('USER', '')}",
                    f"--password={db_config.get('PASSWORD', '')}",
                    f"--host={db_config.get('HOST', 'localhost')}",
                    f"--port={db_config.get('PORT', 3306)}",
                    db_config.get('NAME', '')
                ]
                subprocess.run(cmd, stdin=f, check=True)

            return {'success': True, 'mensaje': 'Base de datos restaurada exitosamente'}
        except Exception as e:
            return {'success': False, 'mensaje': f'Error: {str(e)}'}

    def _restaurar_postgresql(self, backup_file, db_config):
        """Restaurar PostgreSQL"""
        try:
            env = os.environ.copy()
            env['PGPASSWORD'] = db_config.get('PASSWORD', '')

            cmd = [
                'psql',
                f"--host={db_config.get('HOST', 'localhost')}",
                f"--port={db_config.get('PORT', 5432)}",
                f"--username={db_config.get('USER', '')}",
                f"--dbname={db_config.get('NAME', '')}",
                f'--file={backup_file}'
            ]

            subprocess.run(cmd, env=env, check=True)

            return {'success': True, 'mensaje': 'Base de datos restaurada exitosamente'}
        except Exception as e:
            return {'success': False, 'mensaje': f'Error: {str(e)}'}

    def limpiar_backups_antiguos(self):
        """Eliminar backups antiguos según configuración"""
        try:
            config = ConfiguracionBackup.objects.first()
            if not config:
                return

            # Obtener backups ordenados por fecha
            backups = Backup.objects.filter(estado='EXITOSO').order_by('-fecha_creacion')

            # Mantener solo los últimos N backups
            backups_a_eliminar = backups[config.max_backups:]

            for backup in backups_a_eliminar:
                # Eliminar archivo físico
                if os.path.exists(backup.archivo):
                    os.remove(backup.archivo)
                # Eliminar registro
                backup.delete()

        except Exception as e:
            print(f'Error al limpiar backups antiguos: {str(e)}')

    def eliminar_backup(self, backup_id):
        """Eliminar un backup específico"""
        try:
            backup = Backup.objects.get(pk=backup_id)

            # Eliminar archivo físico
            if os.path.exists(backup.archivo):
                os.remove(backup.archivo)

            # Eliminar registro
            backup.delete()

            return {'success': True, 'mensaje': 'Backup eliminado exitosamente'}

        except Backup.DoesNotExist:
            return {'success': False, 'mensaje': 'Backup no encontrado'}
        except Exception as e:
            return {'success': False, 'mensaje': f'Error: {str(e)}'}

    def descargar_backup(self, backup_id):
        """Preparar backup para descarga"""
        try:
            backup = Backup.objects.get(pk=backup_id)

            if not os.path.exists(backup.archivo):
                return None

            return backup.archivo

        except Backup.DoesNotExist:
            return None

