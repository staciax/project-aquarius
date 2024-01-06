from django.db import models
from django.db.models.functions import Now


class Customer(models.Model):  # type: ignore
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=320)
    password_hash = models.CharField(max_length=64)
    salt = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=10, null=True, db_default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'customers'
