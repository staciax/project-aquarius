from __future__ import annotations

from typing import TYPE_CHECKING

from api.permissions import IsCustomer

if TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.viewsets import GenericViewSet

    from .models import Cart


class CartPermission(IsCustomer):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        if not super().has_permission(request, view):
            return False

        if view.action in ('list', 'update', 'destroy') and not request.user.is_superuser:
            return False

        return True

    def has_object_permission(self, request: Request, view: GenericViewSet, obj: Cart) -> bool:
        if request.user.is_superuser:
            return True
        return bool(request.user == obj.user)
