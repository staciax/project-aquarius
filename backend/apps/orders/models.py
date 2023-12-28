from typing import Any

from django.db import models

from apps.customers.models import Customer
from apps.payments.models import Payment
from apps.products.models import Product


class Order(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True, related_name='orders')
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='order',
    )
    status = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preparing_at = models.DateTimeField(null=True, default=None)
    delivering_at = models.DateTimeField(null=True, default=None)
    delivered_at = models.DateTimeField(null=True, default=None)
    cancelled_at = models.DateTimeField(null=True, default=None)

    @property
    def customer_id(self) -> Any:
        return self.customer.id

    @property
    def payment_id(self) -> Any:
        return self.payment.id


class OrderItem(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def order_id(self) -> Any:
        return self.order.id

    @property
    def product_id(self) -> Any:
        return self.product.id
