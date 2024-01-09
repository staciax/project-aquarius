from __future__ import annotations

from django.db import models
from django.db.models.functions import Now

from api.utils import get_media_filename


def get_product_image_path(instance: ProductImage, filename: str) -> str:
    filename = get_media_filename(filename, prefix=instance.product.id)
    return f'product/{filename}'


class Product(models.Model):  # type: ignore
    title = models.CharField(max_length=256)
    description = models.TextField(default='', blank=True)
    author = models.CharField(max_length=128)
    published_at = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    genre = models.ForeignKey('api.Genre', on_delete=models.SET_NULL, null=True, default=None)
    tags = models.ManyToManyField('api.Tag', through='api.ProductTagging')

    class Meta:
        db_table = 'products'


class ProductImage(models.Model):  # type: ignore
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    url = models.ImageField(upload_to=get_product_image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'product_images'
