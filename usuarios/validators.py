"""
DIGITSOFT - Validadores personalizados en español
"""

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator
)


class ValidadorLongitudMinima(MinimumLengthValidator):
    """Validador de longitud mínima con mensaje en español"""

    def __init__(self, min_length=8):
        super().__init__(min_length=min_length)

    def get_help_text(self):
        return f'Tu contraseña debe contener al menos {self.min_length} caracteres.'

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                f'Esta contraseña es demasiado corta. Debe contener al menos {self.min_length} caracteres.',
                code='password_too_short',
                params={'min_length': self.min_length},
            )


class ValidadorContrasenaComun(CommonPasswordValidator):
    """Validador de contraseñas comunes con mensaje en español"""

    def get_help_text(self):
        return 'Tu contraseña no puede ser una contraseña de uso común.'

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                'Esta contraseña es demasiado común. Por favor, elige una contraseña más segura.',
                code='password_too_common',
            )


class ValidadorContrasenaNumerica(NumericPasswordValidator):
    """Validador de contraseñas completamente numéricas con mensaje en español"""

    def get_help_text(self):
        return 'Tu contraseña no puede ser completamente numérica.'

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                'Esta contraseña es completamente numérica. Debe contener letras y otros caracteres.',
                code='password_entirely_numeric',
            )


class ValidadorSimilitudAtributos(UserAttributeSimilarityValidator):
    """Validador de similitud con atributos del usuario con mensaje en español"""

    def get_help_text(self):
        return 'Tu contraseña no puede ser muy similar a tu información personal.'

    def validate(self, password, user=None):
        if not user:
            return

        # Usar el método validate del padre que ya tiene _are_similar implementado
        try:
            super().validate(password, user)
        except ValidationError:
            # Capturar el error y lanzar uno con mensaje en español
            for attribute_name in self.user_attributes:
                value = getattr(user, attribute_name, None)
                if not value or not isinstance(value, str):
                    continue

                # Usar el método heredado de la clase padre
                from difflib import SequenceMatcher
                similarity = SequenceMatcher(None, password.lower(), value.lower()).ratio()

                if similarity > self.max_similarity:
                    verbose_name = self._get_verbose_name(attribute_name)
                    raise ValidationError(
                        f'Tu contraseña es muy similar a tu {verbose_name}. Por favor, elige una contraseña diferente.',
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )

    def _get_verbose_name(self, attribute_name):
        """Traduce los nombres de atributos al español"""
        translations = {
            'username': 'nombre de usuario',
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
        }
        return translations.get(attribute_name, attribute_name)

