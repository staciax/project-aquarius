from typing import Any

from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import serializers

from apps.genres.serializers import GenreSerializer

from .models import Product, ProductImage, ProductInventory

PRODUCT_IMAGE_CHUNK_SIZE = 1024 * 1024 * 5  # 5MB


class ProductImageSerializer(serializers.ModelSerializer):  # type: ignore
    image = serializers.ImageField(required=True)

    def validate_image(self, value: TemporaryUploadedFile) -> TemporaryUploadedFile:
        if value.size > PRODUCT_IMAGE_CHUNK_SIZE:
            raise serializers.ValidationError('Image size too large')
        return value

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
        read_only_fields = (
            'product',
            'created_at',
            'updated_at',
        )


class ProductSerializer(serializers.ModelSerializer):  # type: ignore
    # genre_id = serializers.IntegerField(required=False)
    images = ProductImageSerializer(many=True, required=False)
    inventory = ProductInventorySerializer(read_only=True)
    genres = GenreSerializer(many=True, required=False)

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
            'images',
            'inventory',
            'genres',
            'tags',
        )

    def create(self, validated_data: dict[str, Any]) -> Any:
        # genres = validated_data.pop('genres')
        # print(genres)
        # genre = Genre.objects.get(id=genre_id)
        # print(genre)
        product = Product.objects.create(**validated_data)
        product.genres.add(1)
        product.genres.add(2)
        # product.genres.add(3)
        return product
        # return Product.objects.create(**validated_data)

    def update(self, instance: Any, validated_data: dict[str, Any]) -> Any:
        return super().update(instance, validated_data)
