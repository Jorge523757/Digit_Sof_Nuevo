"""
Script de Prueba - API de Búsqueda Dinámica
Verifica que la API de búsqueda funcione correctamente
"""

import requests
import json
from colorama import init, Fore, Style

# Inicializar colorama para Windows
init()

BASE_URL = "http://localhost:8000/tienda/api/buscar/"

def print_header(text):
    print("\n" + "="*60)
    print(Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL)
    print("="*60)

def print_success(text):
    print(Fore.GREEN + "✓ " + text + Style.RESET_ALL)

def print_error(text):
    print(Fore.RED + "✗ " + text + Style.RESET_ALL)

def print_info(text):
    print(Fore.YELLOW + "→ " + text + Style.RESET_ALL)

def test_api_endpoint(url, test_name):
    """Prueba un endpoint de la API"""
    print_info(f"Probando: {test_name}")
    print_info(f"URL: {url}")

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            if data.get('success'):
                print_success(f"Status: 200 OK")
                print_success(f"Productos encontrados: {data.get('total', 0)}")

                if data.get('productos'):
                    print_info(f"Primer producto: {data['productos'][0]['nombre'][:50]}")

                return True
            else:
                print_error(f"API retornó success=False")
                return False
        else:
            print_error(f"Status: {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print_error("No se pudo conectar al servidor")
        print_info("¿Está el servidor corriendo en http://localhost:8000?")
        return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def main():
    print_header("🔍 PRUEBAS DE API - BÚSQUEDA DINÁMICA")

    tests = [
        {
            'url': BASE_URL,
            'name': 'Búsqueda sin parámetros (todos los productos)'
        },
        {
            'url': f"{BASE_URL}?q=laptop",
            'name': 'Búsqueda simple: "laptop"'
        },
        {
            'url': f"{BASE_URL}?q=hp",
            'name': 'Búsqueda por marca: "hp"'
        },
        {
            'url': f"{BASE_URL}?categoria=1",
            'name': 'Filtro por categoría: ID=1'
        },
        {
            'url': f"{BASE_URL}?orden=precio_asc",
            'name': 'Ordenamiento: Precio ascendente'
        },
        {
            'url': f"{BASE_URL}?q=laptop&orden=precio_desc",
            'name': 'Búsqueda + Orden: laptop por precio desc'
        },
        {
            'url': f"{BASE_URL}?q=core&categoria=1&orden=nombre",
            'name': 'Combinado: "core" + categoría + orden'
        },
    ]

    results = []

    for i, test in enumerate(tests, 1):
        print_header(f"PRUEBA {i}/{len(tests)}: {test['name']}")
        result = test_api_endpoint(test['url'], test['name'])
        results.append(result)
        print()

    # Resumen
    print_header("📊 RESUMEN DE PRUEBAS")
    passed = sum(results)
    total = len(results)

    print(f"\nTotal de pruebas: {total}")
    print_success(f"Exitosas: {passed}")

    if total - passed > 0:
        print_error(f"Fallidas: {total - passed}")

    if passed == total:
        print("\n" + Fore.GREEN + Style.BRIGHT + "✅ ¡TODAS LAS PRUEBAS PASARON!" + Style.RESET_ALL)
    else:
        print("\n" + Fore.YELLOW + "⚠️  Algunas pruebas fallaron. Revisa los errores arriba." + Style.RESET_ALL)

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "Pruebas canceladas por el usuario" + Style.RESET_ALL)
    except Exception as e:
        print_error(f"Error inesperado: {str(e)}")

