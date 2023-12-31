from django.db import models

from apps.customers.models import Customer
from apps.products.models import Product


class Cart(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',  # TODO: remove this or not?
        # null=True,
    )
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        # related_name='cart_items',  # TODO: remove this or not?
        # null=True,
    )
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
