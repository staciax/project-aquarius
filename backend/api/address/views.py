from typing import Any

from rest_framework import serializers, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Address
from .permissions import AddressPermission
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'

    permission_classes = (AddressPermission,)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if len(self.request.user.addresses.all()) >= 5:
            raise serializers.ValidationError('You can only have 5 addresses at most')
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer: AddressSerializer) -> None:
        serializer.save(user=self.request.user)


class AddressMeView(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        serializer = AddressSerializer(request.user.addresses, many=True)
        return Response(serializer.data)
