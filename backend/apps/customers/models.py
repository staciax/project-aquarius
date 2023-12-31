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

    class Meta:
        db_table = 'customers'


class CustomerAddress(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=512)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.OneToOneField(
        'customers.Customer',
        on_delete=models.CASCADE,
        related_name='address',
    )

    class Meta:
        db_table = 'customer_addresses'
