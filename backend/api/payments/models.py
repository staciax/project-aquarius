from django.db import models


class PaymentStatus(models.TextChoices):  # type: ignore
    PENDING = 'pending', 'pending'
    PAID = 'paid', 'paid'
    REFUNDED = 'refunded', 'refunded'


class Payment(models.Model):  # type: ignore
    order = models.OneToOneField('api.Order', on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=128)  # TODO: choices or table for payment methods
    status = models.CharField(
        max_length=32,
        default=PaymentStatus.PENDING,
        choices=PaymentStatus,
    )  # TODO: choices or table for payment status
    paid_at = models.DateTimeField(null=True, blank=True)
    receipt = models.ImageField(upload_to='receipts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'
