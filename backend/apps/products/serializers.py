from rest_framework import serializers

from .models import Product, ProductImage, ProductInventory


class ProductImageSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'product',
            'image',
            'created_at',
            'updated_at',
        )


class ProductInventorySerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = ProductInventory
        fields = (
            'id',
            'product',
            'quantity',
            'created_at',
            'updated_at',
        )


class ProductSerializer(serializers.ModelSerializer):  # type: ignore
    images = ProductImageSerializer(many=True, read_only=True)
    inventory = ProductInventorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'isbn',
            'created_at',
            'updated_at',
        )
