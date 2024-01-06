from rest_framework import viewsets

from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'
