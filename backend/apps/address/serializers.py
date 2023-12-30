from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):  # type: ignore
    first_name = serializers.CharField(required=False, max_length=255)
    last_name = serializers.CharField(required=False, max_length=255)
    street_address = serializers.CharField(required=False, max_length=512)
    province = serializers.CharField(required=False, max_length=128)
    district = serializers.CharField(required=False, max_length=128)
    postal_code = serializers.CharField(required=False, max_length=5)
    phone_number = serializers.CharField(required=False, max_length=10)

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
