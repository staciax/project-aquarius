from rest_framework import serializers

from .models import Cart, CartItem

# from api.products.serializers import ProductReadSerializer


class CartItemSerializer(serializers.ModelSerializer):  # type: ignore
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, instance: CartItem) -> float:
        return instance.product.price * instance.quantity  # type: ignore

    class Meta:
        model = CartItem
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
            'total_price',
            'created_at',
            'updated_at',
        )


class CartItemReadSerializer(CartItemSerializer):
    # product = ProductReadSerializer()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
            'total_price',
            'created_at',
            'updated_at',
        )
        # depth = 1


class CartItemCreateSerializer(CartItemSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
            'total_price',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'cart': {'required': False},
        }


class CartItemUpdateSerializer(CartItemSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
            'total_price',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'cart': {'required': False},
        }


class CartSerializer(serializers.ModelSerializer):  # type: ignore
    # derived fields
    total_price = serializers.SerializerMethodField()
    item_count = serializers.SerializerMethodField()

    def get_total_price(self, instance: Cart) -> float:
        return sum([item.product.price * item.quantity for item in instance.items.all()])  # type: ignore

    def get_item_count(self, instance: Cart) -> int:
        return instance.items.count()  # type: ignore

    class Meta:
        model = Cart
        fields = (
            'id',
            'customer',
            'items',
            'total_price',
            'item_count',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'items',
            'total_price',
            'item_count',
        )


class CartReadSerializer(CartSerializer):
    # items = CartItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'customer',
            'items',
            'total_price',
            'item_count',
            'created_at',
            'updated_at',
        )
        # depth = 1
