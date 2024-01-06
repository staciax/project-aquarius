from __future__ import annotations

from django.db import models
from django.db.models.functions import Now


def upload_to(instance: ProductImage, filename: str) -> str:
    filename = (instance.product.title.lower() + '-' + filename.lower()).replace(' ', '_').replace('-', '_')
    return 'media/{0}'.format(filename)


class Product(models.Model):  # type: ignore
    title = models.CharField(max_length=256)
    description = models.TextField()
    author = models.CharField(max_length=128)
    published_at = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_default=0)
    isbn = models.CharField(max_length=13)
    quantity = models.PositiveIntegerField(db_default=0)
    is_available = models.BooleanField(db_default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    genre = models.ForeignKey('api.Genre', on_delete=models.CASCADE)
    tags = models.ManyToManyField('api.Tag', through='api.ProductTagging')

    class Meta:
        db_table = 'products'


class ProductImage(models.Model):  # type: ignore
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    url = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'product_images'
