from rest_framework import generics

from .models import Address
from .serializers import AddressSerializer


class AddressList(generics.ListCreateAPIView):  # type: ignore
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
