from typing import Any

import bcrypt
from rest_framework import serializers

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
        salt = bcrypt.gensalt()
        password: str = validated_data.pop('password')
        hashed = bcrypt.hashpw(password.encode(), salt)
        password_hash = hashed.replace(salt, b"")
        validated_data['salt'] = salt.decode()
        validated_data['password_hash'] = password_hash.decode()
        return Customer.objects.create(**validated_data)
