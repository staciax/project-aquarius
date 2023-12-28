from __future__ import annotations

from django.db import models


class Genre(models.Model):  # type: ignore
    # if TYPE_CHECKING:
    #     products: models.ManyToManyField[Product]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
