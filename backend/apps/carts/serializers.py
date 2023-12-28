from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Cart
        fields = '__all__'
