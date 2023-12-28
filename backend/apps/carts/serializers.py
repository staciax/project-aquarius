from __future__ import annotations

from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):  # type: ignore
    # product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = (
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
        fields = (
            'id',
            'customer',
            'created_at',
            'updated_at',
            'items',
        )
