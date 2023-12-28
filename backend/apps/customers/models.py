from typing import Any

from django.db import models


class Customer(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=256)
    salt = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='customer')

    # orders
    # cart

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def address_id(self) -> Any:
        return self.address.id

    # class Meta:
    #     private_fields = ('salt',)
