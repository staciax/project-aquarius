from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Payment
        fields = '__all__'
