from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View


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

    def has_permission(self, request: Request, view: View) -> bool:
        return super().has_permission(request, view) and request.user.is_active  # type: ignore
