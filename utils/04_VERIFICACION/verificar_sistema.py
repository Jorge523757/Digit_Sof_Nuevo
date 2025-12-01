from django.core.management.base import BaseCommand
import os
import sys


def verificar_archivos():
    """Verificar que todos los archivos necesarios existan"""
    print("🔍 Verificando archivos del sistema...")
    
    archivos_necesarios = [
        'static/js/cart.js',
        'static/js/header.js',
        'templates/main/auth/auth_base.html',
        'templates/main/auth/profile.html',
        'templates/main/auth/history.html',
        'templates/main/admin/admin_panel.html',
        'templates/main/includes/header.html'
    ]
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for archivo in archivos_necesarios:
        ruta_completa = os.path.join(base_dir, archivo)
        if os.path.exists(ruta_completa):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - NO ENCONTRADO")
    
    return True


def verificar_urls():
    """Verificar que las URLs estén configuradas"""
    print("\n🌐 Verificando configuración de URLs...")
    
    try:
        from main.urls import urlpatterns
        urls_necesarias = ['profile', 'admin_panel', 'history']
        
        urls_encontradas = []
        for pattern in urlpatterns:
            if hasattr(pattern, 'name') and pattern.name:
                urls_encontradas.append(pattern.name)
        
        for url in urls_necesarias:
            if url in urls_encontradas:
                print(f"✅ URL '{url}' configurada")
            else:
                print(f"❌ URL '{url}' - NO ENCONTRADA")
        
        print(f"\n📋 URLs disponibles: {', '.join(urls_encontradas)}")
        
    except Exception as e:
        print(f"❌ Error al verificar URLs: {e}")
    
    return True


def verificar_views():
    """Verificar que las vistas estén definidas"""
    print("\n🎯 Verificando vistas...")
    
    try:
        from main import views
        
        vistas_necesarias = ['profile_view', 'admin_panel_view', 'history_view']
        
        for vista in vistas_necesarias:
            if hasattr(views, vista):
                print(f"✅ Vista '{vista}' definida")
            else:
                print(f"❌ Vista '{vista}' - NO ENCONTRADA")
    
    except Exception as e:
        print(f"❌ Error al verificar vistas: {e}")
    
    return True


def main():
    """Función principal de verificación"""
    print("🚀 VERIFICADOR DEL SISTEMA DIGIT SOFT")
    print("=" * 50)
    
    # Cambiar al directorio del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    # Agregar el directorio al path para importar módulos
    sys.path.insert(0, project_dir)
    
    # Configurar Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
    
    try:
        import django
        django.setup()
        print("✅ Django configurado correctamente")
    except Exception as e:
        print(f"❌ Error al configurar Django: {e}")
        return False
    
    # Ejecutar verificaciones
    verificar_archivos()
    verificar_urls()
    verificar_views()
    
    print("\n" + "=" * 50)
    print("🎉 Verificación completada!")
    print("\n💡 Para probar el sistema:")
    print("1. Ejecuta: python manage.py runserver")
    print("2. Navega a: http://127.0.0.1:8000")
    print("3. Inicia sesión y prueba:")
    print("   - Mi Perfil (/auth/profile/)")
    print("   - Panel de Administración (/admin-panel/)")
    print("   - Historial (/auth/history/)")
    print("   - Carrito (hacer clic en el ícono del carrito)")
    
    return True


if __name__ == "__main__":
    main()