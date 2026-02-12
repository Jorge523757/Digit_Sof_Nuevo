"""
Validadores personalizados para DIGIT SOFT
"""

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re


# Validador de teléfono colombiano
def validar_telefono_colombiano(value):
    """Valida que el teléfono sea un número colombiano válido"""
    # Eliminar espacios y caracteres especiales
    telefono = re.sub(r'[^\d]', '', str(value))

    # Verificar longitud (7 o 10 dígitos)
    if len(telefono) not in [7, 10]:
        raise ValidationError(
            '📱 El teléfono debe tener 7 dígitos (fijo) o 10 dígitos (celular)',
            code='telefono_invalido'
        )

    # Si es celular, debe empezar con 3
    if len(telefono) == 10 and not telefono.startswith('3'):
        raise ValidationError(
            '📱 Los números celulares en Colombia deben empezar con 3',
            code='celular_invalido'
        )


# Validador de NIT colombiano
def validar_nit(value):
    """Valida que el NIT sea válido"""
    nit = re.sub(r'[^\d]', '', str(value))

    if len(nit) < 8 or len(nit) > 10:
        raise ValidationError(
            '🏢 El NIT debe tener entre 8 y 10 dígitos',
            code='nit_invalido'
        )


# Validador de cédula colombiana
def validar_cedula(value):
    """Valida que la cédula sea válida"""
    cedula = re.sub(r'[^\d]', '', str(value))

    if len(cedula) < 6 or len(cedula) > 10:
        raise ValidationError(
            '🪪 La cédula debe tener entre 6 y 10 dígitos',
            code='cedula_invalida'
        )


# Validador de dirección
def validar_direccion(value):
    """Valida que la dirección tenga un formato mínimo válido"""
    if len(value.strip()) < 5:
        raise ValidationError(
            '📍 La dirección debe tener al menos 5 caracteres',
            code='direccion_corta'
        )

    if not any(char.isdigit() for char in value):
        raise ValidationError(
            '📍 La dirección debe incluir números (ej: Calle 123 #45-67)',
            code='direccion_sin_numero'
        )


# Validador de nombre
def validar_nombre(value):
    """Valida que el nombre sea válido"""
    if len(value.strip()) < 2:
        raise ValidationError(
            '👤 El nombre debe tener al menos 2 caracteres',
            code='nombre_corto'
        )

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
        raise ValidationError(
            '👤 El nombre solo puede contener letras y espacios',
            code='nombre_caracteres_invalidos'
        )


# Validador de precio
def validar_precio_positivo(value):
    """Valida que el precio sea positivo"""
    if value <= 0:
        raise ValidationError(
            '💰 El precio debe ser mayor a cero',
            code='precio_invalido'
        )

    if value > 999999999:
        raise ValidationError(
            '💰 El precio no puede ser mayor a $999,999,999',
            code='precio_muy_alto'
        )


# Validador de stock
def validar_stock(value):
    """Valida que el stock sea válido"""
    if value < 0:
        raise ValidationError(
            '📦 El stock no puede ser negativo',
            code='stock_negativo'
        )

    if value > 999999:
        raise ValidationError(
            '📦 El stock no puede ser mayor a 999,999 unidades',
            code='stock_muy_alto'
        )


# Validador de email profesional
def validar_email_profesional(value):
    """Valida email con mensajes más amigables"""
    validator = EmailValidator(message='📧 Ingrese un email válido (ejemplo: usuario@empresa.com)')
    validator(value)

    # Validar que no sea un email temporal
    dominios_temporales = ['tempmail.com', 'guerrillamail.com', '10minutemail.com']
    dominio = value.split('@')[1].lower()

    if dominio in dominios_temporales:
        raise ValidationError(
            '📧 No se permiten correos temporales',
            code='email_temporal'
        )


# Validador de contraseña segura
def validar_contraseña_segura(value):
    """Valida que la contraseña sea segura"""
    if len(value) < 8:
        raise ValidationError(
            '🔐 La contraseña debe tener al menos 8 caracteres',
            code='contraseña_corta'
        )

    if not re.search(r'[A-Z]', value):
        raise ValidationError(
            '🔐 La contraseña debe contener al menos una letra mayúscula',
            code='sin_mayuscula'
        )

    if not re.search(r'[a-z]', value):
        raise ValidationError(
            '🔐 La contraseña debe contener al menos una letra minúscula',
            code='sin_minuscula'
        )

    if not re.search(r'[0-9]', value):
        raise ValidationError(
            '🔐 La contraseña debe contener al menos un número',
            code='sin_numero'
        )


# Validador de fecha futura
def validar_fecha_futura(value):
    """Valida que la fecha no sea en el futuro"""
    from datetime import date

    if value > date.today():
        raise ValidationError(
            '📅 La fecha no puede ser en el futuro',
            code='fecha_futura'
        )


# Validador de rango de fechas
def validar_rango_fechas(fecha_inicio, fecha_fin):
    """Valida que el rango de fechas sea válido"""
    if fecha_fin < fecha_inicio:
        raise ValidationError(
            '📅 La fecha de fin no puede ser anterior a la fecha de inicio',
            code='rango_invalido'
        )


# Validador de archivo
def validar_tamaño_archivo(value):
    """Valida que el archivo no sea muy grande"""
    limite = 5 * 1024 * 1024  # 5 MB

    if value.size > limite:
        raise ValidationError(
            '📎 El archivo no puede ser mayor a 5 MB',
            code='archivo_muy_grande'
        )


# Validador de extensión de archivo
def validar_extension_imagen(value):
    """Valida que el archivo sea una imagen"""
    extensiones_permitidas = ['jpg', 'jpeg', 'png', 'gif', 'webp']
    extension = value.name.split('.')[-1].lower()

    if extension not in extensiones_permitidas:
        raise ValidationError(
            f'🖼️ Solo se permiten archivos: {", ".join(extensiones_permitidas)}',
            code='extension_invalida'
        )


# Validador de cantidad
def validar_cantidad_positiva(value):
    """Valida que la cantidad sea positiva"""
    if value <= 0:
        raise ValidationError(
            '🔢 La cantidad debe ser mayor a cero',
            code='cantidad_invalida'
        )

    if value > 10000:
        raise ValidationError(
            '🔢 La cantidad no puede ser mayor a 10,000',
            code='cantidad_muy_alta'
        )

