from typing import Any

from rest_framework import serializers

from . import utils
from .models import Customer

# TODO: read only model serializer


class CustomerSerializer(serializers.ModelSerializer):  # type: ignore
    password = serializers.CharField(max_length=1024, write_only=True)
    password_hash = serializers.CharField(max_length=512, required=False, write_only=False)
    salt = serializers.CharField(max_length=128, required=False, write_only=False)

    class Meta:
        depth = 1
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'salt',
            'password',
            'password_hash',
            'phone_number',
            'created_at',
            'updated_at',
            'address',
        )

        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'address': {'required': False, 'read_only': True},
        }

        # extra_kwargs = {
        #     'password_hash': {'write_only': True, 'required': False},
        #     'salt': {'write_only': True, 'required': False},
        # }
        # NOTE: https://stackoverflow.com/questions/74391152/adding-permissions-to-user-on-the-serializer

    def create(self, validated_data: dict[str, Any]) -> Any:
        salt, password_hash = utils.hash_password(validated_data['password'])
        return Customer.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            salt=salt,
            password_hash=password_hash,
            phone_number=validated_data['phone_number'],
        )
