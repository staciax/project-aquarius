from django.apps import AppConfig


class ApiConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
