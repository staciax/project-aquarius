from django.apps import AppConfig


class ProductsConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
