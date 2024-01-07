from django.db import models
from django.db.models.functions import Now

from api.user.models import User


class Customer(models.Model):  # type: ignore
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.CharField(max_length=10, null=True, db_default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    updated_at = models.DateTimeField(auto_now=True, db_default=Now())

    class Meta:
        db_table = 'customers'
