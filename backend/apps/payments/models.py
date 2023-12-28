from django.db import models


class Payment(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
