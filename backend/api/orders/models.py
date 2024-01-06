from django.db import models


class OrderStatus(models.TextChoices):  # type: ignore
    PENDING = 'pending', 'pending'
    APPROVED = 'approved', 'approved'
    CANCELED = 'canceled', 'canceled'
    SHIPPED = 'shipped', 'shipped'
    COMPLETED = 'completed', 'completed'
    RETURNED = 'returned', 'returned'


class Order(models.Model):  # type: ignore
    customer = models.ForeignKey('api.Customer', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=32,
        choices=OrderStatus,
        default=OrderStatus.PENDING,
    )  # TODO: choices or table for order status
    tracking_number = models.CharField(max_length=32, null=True)
    approved_at = models.DateTimeField(null=True)
    shipped_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):  # type: ignore
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey('api.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_on_purchase = models.DecimalField(max_digits=10, decimal_places=2)  # คือ ราคาตอนซื้อ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_items'
