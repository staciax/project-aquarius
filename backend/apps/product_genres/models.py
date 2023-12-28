from django.db import models

from apps.genres.models import Genre
from apps.products.models import Product


class ProductGenre(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
