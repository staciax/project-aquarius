from rest_framework import serializers

from .models import Customer

# from api.user.serializers import UserSerializer
# from api.address.serializers import AddressSerializer
# from api.cart.serializers import CartReadSerializer


class CustomerReadSerializer(serializers.ModelSerializer):  # type: ignore
    # cart = CartReadSerializer(many=False, read_only=True)
    # address = AddressSerializer(many=False, read_only=True)
    # user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Customer
        # depth = 1
        fields = (
            'id',
            'user',
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
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'phone_number',
            'address',
            'cart',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'address',
            'created_at',
            'updated_at',
            'cart',
        )


class CustomerUpdateSerializer(CustomerCreateSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'phone_number',
            'cart',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'cart',
            'created_at',
            'updated_at',
        )
