from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from api.user.models import User


class IsSuperUser(permissions.BasePermission):  # type: ignore
    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(request.user and request.user.is_superuser)


class BaseAPIPermission(permissions.DjangoModelPermissions):  # type: ignore
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request: Request, view: APIView) -> bool:
        return super().has_permission(request, view) and request.user.is_active  # type: ignore


class IsCustomer(BaseAPIPermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if not isinstance(request.user, User):
            return False
        return super().has_permission(request, view) and request.user.is_customer
