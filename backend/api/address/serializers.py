from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Address
        fields = '__all__'
