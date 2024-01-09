from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View


class BaseAPIPermission(permissions.IsAuthenticated):  # type: ignore
    # perms_map = {
    #     'GET': ['%(app_label)s.view_%(model_name)s'],
    #     'OPTIONS': [],
    #     'HEAD': [],
    #     'POST': ['%(app_label)s.add_%(model_name)s'],
    #     'PUT': ['%(app_label)s.change_%(model_name)s'],
    #     'PATCH': ['%(app_label)s.change_%(model_name)s'],
    #     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    # }

    def has_permission(self, request: Request, view: View) -> bool:
        if not super().has_permission(request, view):
            return False

        if request.user.is_superuser:
            return True

        return request.user.is_active  # type: ignore

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        if request.user.is_superuser:
            return True
        return True

    # TODO: object permission
