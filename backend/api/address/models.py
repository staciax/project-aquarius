from django.db import models
from django.db.models.functions import Now


class Address(models.Model):  # type: ignore
    first_name = models.CharField(max_length=128, null=True, db_default=None)
    last_name = models.CharField(max_length=128, null=True, db_default=None)
    phone_number = models.CharField(max_length=10, null=True, db_default=None)
    street_address = models.CharField(max_length=256, null=True, db_default=None)
    province = models.CharField(max_length=128, null=True, db_default=None)
    district = models.CharField(max_length=128, null=True, db_default=None)
    postal_code = models.CharField(max_length=5, null=True, db_default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())
    customer = models.OneToOneField(
        'api.Customer',
        on_delete=models.CASCADE,  # หมายถึงถ้าลูกค้าถูกลบ ที่อยู่ของลูกค้าจะถูกลบไปด้วย
        null=True,
        db_default=None,
        related_name='address',
    )

    class Meta:
        db_table = 'address'
