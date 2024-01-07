from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from api.user.models import User
from app.permissions import BaseAPIPermission


class IsSuperUser(permissions.BasePermission):  # type: ignore
    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(request.user and request.user.is_superuser)


class IsCustomer(BaseAPIPermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if not isinstance(request.user, User):
            return False
        return super().has_permission(request, view) and request.user.is_customer
