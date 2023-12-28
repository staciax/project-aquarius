from django.db import models

# Create your models here.


class Address(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=512)
    province = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
