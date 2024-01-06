from django.db import models
from django.db.models.functions import Now


class Genre(models.Model):  # type: ignore
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'genres'
