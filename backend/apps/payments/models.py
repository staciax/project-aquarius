from __future__ import annotations

from typing import Any

from django.db import models


class Payment(models.Model):  # type: ignore
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    provider = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def order_id(self) -> Any:
        return self.order.id
