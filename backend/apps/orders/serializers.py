from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Order
        fields = '__all__'
