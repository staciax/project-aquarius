from typing import Any

from django.db import models

from apps.customers.models import Customer


class Cart(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Cart of {self.customer}'

    @property
    def customer_id(self) -> Any:
        return self.customer.id


class CartItem(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(
        Cart,
        # primary_key=True,
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.IntegerField()
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cart_id(self) -> Any:
        return self.cart.id

    @property
    def product_id(self) -> Any:
        return self.product.id

    # def get_total(self) -> float:
    #     return self.product.price * self.quantity

    class Meta:
        unique_together = ('cart', 'product')
