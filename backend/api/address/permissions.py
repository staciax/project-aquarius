from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsCustomer

from .models import Address


class AddressPermission(IsCustomer):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        if not super().has_permission(request, view):
            return False

        if view.action in ('list') and not request.user.is_superuser:
            return False

        return True

    def has_object_permission(self, request: Request, view: GenericViewSet, obj: Address) -> bool:
        if request.user.is_superuser:
            return True
        return bool(request.user == obj.user)
