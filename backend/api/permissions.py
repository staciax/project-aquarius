from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):  # type: ignore
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request: Request, view: str, obj: str) -> bool:
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user  # type: ignore
