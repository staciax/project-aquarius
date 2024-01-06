from django.db import models


class ProductTagging(models.Model):  # type: ignore
    product = models.ForeignKey('api.Product', on_delete=models.CASCADE)
    tag = models.ForeignKey('api.Tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tagging'
        unique_together = ('product', 'tag')
