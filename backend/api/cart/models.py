from django.db import models
from django.db.models.functions import Now


class Cart(models.Model):  # type: ignore
    customer = models.OneToOneField('api.Customer', on_delete=models.CASCADE, related_name='cart')

    # NOTE: in my db design 'created_at' and 'updated_at' are not required
    #      but I'm adding them here for consistency
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'cart'


class CartItem(models.Model):  # type: ignore
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',  # TODO: remove this or not?
    )
    product = models.OneToOneField('api.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart_items'
