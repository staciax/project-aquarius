from django.apps import AppConfig


class OrdersConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
