from django.db import models


class Genre(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # product = models.OneToOneField(
    #     'products.Product',
    #     on_delete=models.CASCADE,
    #     related_name='genre',
    # )

    class Meta:
        db_table = 'genres'
        ordering = ['name']
