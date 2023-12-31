from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):  # type: ignore
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'payment',
            'status',
            'created_at',
            'updated_at',
            'preparing_at',
            'delivering_at',
            'delivered_at',
            'cancelled_at',
            'items',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
