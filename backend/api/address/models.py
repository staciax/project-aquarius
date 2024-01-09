from django.db import models
from django.db.models.functions import Now


class Address(models.Model):  # type: ignore
    first_name = models.CharField(max_length=128, null=True, default=None)
    last_name = models.CharField(max_length=128, null=True, default=None)
    phone_number = models.CharField(max_length=10, null=True, default=None)
    street_address = models.CharField(max_length=256, null=True, default=None)
    province = models.CharField(max_length=128, null=True, default=None)
    district = models.CharField(max_length=128, null=True, default=None)
    postal_code = models.CharField(max_length=5, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())
    user = models.ForeignKey(
        'api.User',
        on_delete=models.CASCADE,  # หมายถึงถ้าลูกค้าถูกลบ ที่อยู่ของลูกค้าจะถูกลบไปด้วย
        related_name='addresses',
        null=True,
        default=None,
    )

    class Meta:
        db_table = 'addresses'
