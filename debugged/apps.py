from django.apps import AppConfig


class DebuggedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'debugged'
