from django.apps import AppConfig


class ProyectoaptConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProyectoAPT'

    def ready(self):
        import ProyectoAPT.signals  # Carga las señales al iniciar la aplicación
