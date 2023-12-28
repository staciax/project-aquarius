from typing import Any

from django.db import models

from apps.address.models import Address


class Customer(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=4096)
    salt = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='customer')

    # orders
    # cart

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def address_id(self) -> Any:
        return self.address.id
