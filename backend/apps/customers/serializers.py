from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Customer
        fields = '__all__'
