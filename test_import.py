import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from usuarios import views

print("Funciones en views:")
funcs = [x for x in dir(views) if not x.startswith('_') and callable(getattr(views, x))]
for func in sorted(funcs):
    print(f"  - {func}")

print(f"\n¿Existe registro_cliente? {hasattr(views, 'registro_cliente')}")
print(f"¿Existe registro_tecnico? {hasattr(views, 'registro_tecnico')}")
print(f"¿Existe login_view? {hasattr(views, 'login_view')}")

if hasattr(views, 'registro_tecnico'):
    print("\n✅ ¡La función registro_tecnico SÍ existe!")
else:
    print("\n❌ La función registro_tecnico NO existe")

