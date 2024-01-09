from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from api.user.models import User
from app.permissions import BaseAPIPermission


class IsSuperUser(permissions.IsAuthenticated):  # type: ignore
    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(request.user and request.user.is_superuser)


class IsSuperUserOrReadOnly(IsSuperUser):  # type: ignore
    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(request.method in permissions.SAFE_METHODS or super().has_permission(request, view))


class IsCustomer(BaseAPIPermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        assert isinstance(request.user, User)
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            return False
        return super().has_permission(request, view) and request.user.is_customer
