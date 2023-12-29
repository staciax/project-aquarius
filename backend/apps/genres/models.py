from __future__ import annotations

from django.db import models


class Genre(models.Model):  # type: ignore
    # if TYPE_CHECKING:
    #     products: models.ManyToManyField[Product]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['name']
