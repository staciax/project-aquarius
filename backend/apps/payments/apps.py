from django.apps import AppConfig


class PaymentsConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'
