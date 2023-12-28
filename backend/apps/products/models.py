from typing import Any

from django.db import models

from apps.genres.models import Genre

# Create your models here.


class Product(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(
        Genre,
        through='product_genres.ProductGenre',
        related_name='products',
    )
    tags = models.ManyToManyField(
        'tags.Tag',
        through='product_tags.ProductTag',
        related_name='products',
    )

    def __str__(self) -> Any:
        return self.name

    @property
    def genre_id(self) -> Any:
        return self.genre.id


class ProductImage(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def product_id(self) -> Any:
        return self.product.id


class ProductInventory(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def product_id(self) -> Any:
        return self.product.id
