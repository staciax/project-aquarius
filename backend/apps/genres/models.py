from django.db import models

# Create your models here.


class Genre(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
