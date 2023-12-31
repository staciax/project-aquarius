from django.db import models

from apps.customers.models import Customer
from apps.payments.models import Payment
from apps.products.models import Product


class Order(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name='orders',
    )
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='order',
    )
    # status = models.CharField(max_length=128, default='created')  # created, preparing, delivering, delivered, cancelled, refunded
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preparing_at = models.DateTimeField(null=True, default=None)
    delivering_at = models.DateTimeField(null=True, default=None)
    delivered_at = models.DateTimeField(null=True, default=None)
    cancelled_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_items'


# TODO: order details
