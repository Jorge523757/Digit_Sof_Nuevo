"""
Filtros personalizados para formatear monedas en pesos colombianos
"""
from django import template

register = template.Library()


@register.filter(name='peso_colombiano')
def peso_colombiano(valor):
    """
    Formatea un número como peso colombiano sin decimales
    Ejemplo: 50000 -> $50.000
    """
    try:
        # Convertir a float primero para manejar strings y Decimals
        numero = float(valor) if valor else 0
        # Redondear para eliminar decimales
        numero = int(round(numero))
        # Formatear con separador de miles
        formato = f"{numero:,}".replace(',', '.')
        return f"${formato}"
    except (ValueError, TypeError):
        return "$0"


@register.filter(name='peso_colombiano_decimal')
def peso_colombiano_decimal(valor, decimales=2):
    """
    Formatea un número como peso colombiano con decimales opcionales
    Ejemplo: 50000.50 -> $50.000,50
    """
    try:
        numero = float(valor) if valor else 0
        # Separar parte entera y decimal
        parte_entera = int(numero)
        parte_decimal = numero - parte_entera

        # Formatear parte entera con separador de miles
        formato_entero = f"{parte_entera:,}".replace(',', '.')

        # Formatear parte decimal si es necesario
        if decimales > 0 and parte_decimal > 0:
            formato_decimal = f"{parte_decimal:.{decimales}f}"[2:]  # Eliminar '0.'
            return f"${formato_entero},{formato_decimal}"
        else:
            return f"${formato_entero}"
    except (ValueError, TypeError):
        return "$0"

