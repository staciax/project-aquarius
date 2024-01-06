from typing import Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import utils
from .models import Customer

# from api.address.serializers import AddressSerializer
# from api.cart.serializers import CartReadSerializer


class CustomerReadSerializer(serializers.ModelSerializer):  # type: ignore
    # cart = CartReadSerializer(many=False, read_only=True)
    # address = AddressSerializer(many=False, read_only=True)

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password_hash',
            'salt',
            'phone_number',
            'address',
            'cart',
            'created_at',
            'updated_at',
        )
        # extra_kwargs = {
        #     'cart': {'read_only': True},
        # }


class CustomerCreateSerializer(serializers.ModelSerializer):  # type: ignore
    salt = serializers.CharField(required=False, write_only=False)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True, style={'input_type': 'password'})
    password_hash = serializers.CharField(max_length=64, required=False, write_only=False)

    def create(self, validated_data: dict[str, Any]) -> Any:
        salt, password_hash = utils.hash_password(validated_data.pop('password'))
        return Customer.objects.create(**validated_data, salt=salt, password_hash=password_hash)

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_hash',
            'salt',
            'phone_number',
            'address',
            'cart',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'salt',
            'password_hash',
            'address',
            'created_at',
            'updated_at',
            'cart',
        )


class CustomerUpdateSerializer(CustomerCreateSerializer):
    first_name = serializers.CharField(max_length=128, required=False)
    last_name = serializers.CharField(max_length=128, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(
        required=False,
        min_length=8,
        max_length=128,
        write_only=True,
        style={'input_type': 'password'},
    )
    password_old = serializers.CharField(
        required=False,
        min_length=8,
        max_length=128,
        write_only=True,
        style={'input_type': 'password'},
    )

    def update(self, instance: Customer, validated_data: dict[str, Any]) -> Any:
        if 'email' in validated_data:
            # if Customer.objects.filter(email=validated_data['email']).exists():
            #     raise ValidationError('Email already exists.')
            # TODO: in the future, we should send a verification email to the new email address
            raise ValidationError({'email': 'This field is read-only. If you want to change your email, please contact us.'})
        if 'password' in validated_data:
            if 'password_old' not in validated_data:
                raise ValidationError(
                    {
                        'password_old': 'This field is required. If you want to change your password, you must provide the old password.'
                    }
                )
            else:
                if not utils.check_password(validated_data.pop('password_old'), instance.salt, instance.password_hash):
                    raise ValidationError({'password_old': 'Old password is incorrect.'})

            if utils.check_password(validated_data['password'], instance.salt, instance.password_hash):
                raise ValidationError({'password': 'New password cannot be the same as the old password.'})

            salt, password_hash = utils.hash_password(validated_data.pop('password'))
            instance.salt = salt
            instance.password_hash = password_hash
        return super().update(instance, validated_data)

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_hash',
            'password_old',
            'salt',
            'phone_number',
            # 'address',
            'cart',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'email',
            'salt',
            'password_hash',
            'cart',
            'created_at',
            'updated_at',
        )


# 'blank': 'Email cannot be blank.',
# 'invalid': 'Email is invalid.',
# 'max_length': 'Email is too long.',
# 'min_length': 'Email is too short.',
# 'max_value': 'Email is too long.',
# 'min_value': 'Email is too short.',
