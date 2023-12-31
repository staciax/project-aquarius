from __future__ import annotations

from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):  # type: ignore
    quantity = serializers.IntegerField(min_value=0, max_value=10)  # TODO: makesure min value should be 1 or 0

    class Meta:
        model = CartItem
        # depth = 1
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
            'created_at',
            'updated_at',
        )


class CartItemReadSerializer(CartItemSerializer):  # type: ignore
    product = ProductSerializer()


class CartSerializer(serializers.ModelSerializer):  # type: ignore
    # items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        # depth = 1
        fields = (
            'id',
            'customer',
            'created_at',
            'updated_at',
            'items',
        )
        extra_kwargs = {
            'items': {'required': False},
        }
