from typing import Any

from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import serializers

from .models import Product, ProductImage

PRODUCT_IMAGE_CHUNK_SIZE = 1024 * 1024 * 5  # 5MB


class ProductImageSerializer(serializers.ModelSerializer):  # type: ignore
    url = serializers.ImageField(required=True)

    def validate_image(self, value: TemporaryUploadedFile) -> TemporaryUploadedFile:
        if value.size > PRODUCT_IMAGE_CHUNK_SIZE:
            raise serializers.ValidationError('Image size too large')
        return value

    def create(self, validated_data: dict[str, Any]) -> Any:
        if product := validated_data.get('product'):
            if product.images.count() >= 10:
                raise serializers.ValidationError('Product can only have 10 images')
        return super().create(validated_data)

    class Meta:
        model = ProductImage
        fields = '__all__'
        extra_kwargs = {
            'product': {'required': False, 'write_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'price': {
                'min_value': 0,
            },
        }


class ProductReadSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'author',
            'published_at',
            'price',
            'isbn',
            'quantity',
            'is_available',
            'images',
            'genre',
            'tags',
            'created_at',
            'updated_at',
        )
        depth = 1


class ProductUpdateSerializer(serializers.ModelSerializer):  # type: ignore
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    published_at = serializers.DateTimeField(required=False)
    isbn = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2, min_value=0)
    quantity = serializers.IntegerField(required=False, min_value=0)
    is_available = serializers.BooleanField(required=False)

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
