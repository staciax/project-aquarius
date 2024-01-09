from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from api.user.models import User


class IsSuperUserOrIsOwner(permissions.IsAuthenticated):  # type: ignore
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        if not super().has_permission(request, view):
            return False

        if request.user.is_superuser:
            return True

        if view.action in ('list', 'create', 'destroy'):
            return False

        return True

    def has_object_permission(self, request: Request, view: APIView, obj: User) -> bool:
        return bool(request.user and request.user.is_superuser) or obj == request.user
