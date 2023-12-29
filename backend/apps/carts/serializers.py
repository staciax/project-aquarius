from __future__ import annotations

from rest_framework import serializers

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):  # type: ignore
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


class CartSerializer(serializers.ModelSerializer):  # type: ignore
    items = CartItemSerializer(many=True, read_only=True)

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
