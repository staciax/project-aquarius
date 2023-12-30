from django.db import models

from apps.genres.models import Genre


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


class ProductImage(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductInventory(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
