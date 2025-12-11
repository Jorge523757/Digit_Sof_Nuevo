"""
Script para crear la tabla de notificaciones manualmente
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

def crear_tabla_notificaciones():
    """Crea la tabla de notificaciones en la base de datos"""
    with connection.cursor() as cursor:
        # Crear tabla de notificaciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios_notificacion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                titulo VARCHAR(200) NOT NULL,
                mensaje TEXT NOT NULL,
                tipo VARCHAR(10) NOT NULL DEFAULT 'INFO',
                leida BOOLEAN NOT NULL DEFAULT 0,
                fecha_creacion DATETIME NOT NULL,
                fecha_lectura DATETIME NULL,
                url VARCHAR(500),
                icono VARCHAR(50),
                color VARCHAR(20),
                FOREIGN KEY(usuario_id) REFERENCES auth_user(id) ON DELETE CASCADE
            )
        ''')

        # Crear índices
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_notif_usuario_leida 
            ON usuarios_notificacion(usuario_id, leida)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_notif_fecha 
            ON usuarios_notificacion(fecha_creacion DESC)
        ''')

        print("✅ Tabla 'usuarios_notificacion' creada exitosamente")
        print("✅ Índices creados exitosamente")

if __name__ == '__main__':
    try:
        crear_tabla_notificaciones()
        print("\n🎉 ¡Migración completada!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

