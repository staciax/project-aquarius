from django.db import models

from apps.products.models import Product
from apps.tags.models import Tag


class ProductTag(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tags'
        unique_together = ('product', 'tag')
