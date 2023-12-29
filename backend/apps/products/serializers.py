from typing import Any

from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import serializers

from apps.genres.serializers import GenreSerializer
from apps.tags.models import Tag
from apps.tags.serializers import TagSerializer

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
    images = ProductImageSerializer(many=True, required=False)
    inventory = ProductInventorySerializer(read_only=True)
    genres = GenreSerializer(many=True, required=False, read_only=True)
    tags = TagSerializer(many=True, required=False, read_only=True)

    genre_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
    )
    tag_ids = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False,
    )

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
            'genre_ids',
            'tag_ids',
        )

    def create(self, validated_data: dict[str, Any]) -> Any:
        genre_ids = validated_data.pop('genre_ids', [])
        tag_ids = validated_data.pop('tag_ids', [])
        product = Product.objects.create(**validated_data)

        product.inventory = ProductInventory.objects.create(product=product)

        for genre_id in genre_ids:
            product.genres.add(genre_id)

        for tag_id in tag_ids:
            tag, _ = Tag.objects.get_or_create(name=tag_id)
            product.tags.add(tag)
        return product

    def update(self, instance: Any, validated_data: dict[str, Any]) -> Any:
        return super().update(instance, validated_data)
