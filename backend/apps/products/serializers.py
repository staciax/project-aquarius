from typing import Any

from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import serializers

from apps.tags.models import Tag

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
        extra_kwargs = {
            'product': {'required': False, 'write_only': True},
        }


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

    genre_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
        max_length=5,
    )
    tag_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False,
        max_length=5,
    )

    class Meta:
        model = Product
        depth = 1
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
            'tag_names',
        )

    def create(self, validated_data: dict[str, Any]) -> Any:
        product = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            isbn=validated_data['isbn'],
        )

        # set default inventory
        product.inventory = ProductInventory.objects.create(product=product)

        # add genre to product
        genre_ids = validated_data.get('genre_ids', [])
        for genre_id in genre_ids:
            product.genres.add(genre_id)

        # add tag to product
        tag_names = validated_data.get('tag_names', [])
        for tname in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tname)
            product.tags.add(tag)

        return product

    def update(self, instance: Product, validated_data: dict[str, Any]) -> Any:
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.isbn = validated_data.get('isbn', instance.isbn)

        # genres

        genre_ids = validated_data.get('genre_ids', [])

        # remove genres that are not in the genre_ids
        for genre in instance.genres.all():
            if genre.id not in genre_ids:
                instance.genres.remove(genre)
            else:
                genre_ids.remove(genre.id)

        # add genres that are in the genre_ids
        for genre_id in genre_ids:
            instance.genres.add(genre_id)

        # tags

        tag_names = validated_data.get('tag_names', [])

        for tag in instance.tags.all():
            if tag.name not in tag_names:
                instance.tags.remove(tag)
            else:
                tag_names.remove(tag.name)

        for tname in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tname)
            instance.tags.add(tag)

        instance.save()

        return instance
