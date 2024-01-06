from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'product',
            'quantity',
            'price_per_unit',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'order': {'read_only': True},
        }


class OrderSerializer(serializers.ModelSerializer):  # type: ignore
    items = OrderItemSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'status',
            'tracking_number',
            'approved_at',
            'shipped_at',
            'canceled_at',
            'completed_at',
            'created_at',
            'updated_at',
            'items',
        )
