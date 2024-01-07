from rest_framework import viewsets

from api.permissions import IsSuperUser

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    permission_classes = [IsSuperUser]
