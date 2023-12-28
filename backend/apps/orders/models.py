from typing import Any

from apps.payments.models import Payment
from apps.products.models import Product
from django.db import models

# Create your models here.


class Order(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    status = models.CharField(max_length=128)
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='order',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preparing_at = models.DateTimeField(null=True, default=None)
    delivering_at = models.DateTimeField(null=True, default=None)
    delivered_at = models.DateTimeField(null=True, default=None)
    cancelled_at = models.DateTimeField(null=True, default=None)


class OrderItem(models.Model):  # type: ignore
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def product_id(self) -> Any:
        return self.product.id
