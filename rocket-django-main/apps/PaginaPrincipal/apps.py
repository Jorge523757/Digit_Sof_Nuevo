from django.apps import AppConfig


class PaginaPrincipalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.PaginaPrincipal"

    def ready(self):
        import apps.PaginaPrincipal.signals
