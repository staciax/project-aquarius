from typing import Any

from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerCreateSerializer, CustomerReadSerializer, CustomerUpdateSerializer


class CustomerViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerReadSerializer
    lookup_field = 'id'

    def get_serializer_class(self) -> Any:
        if self.action in ('list', 'retrieve'):
            return CustomerReadSerializer
        elif self.action == 'create':
            return CustomerCreateSerializer
        elif self.action in ('update', 'partial_update'):
            return CustomerUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer: Any) -> None:
        serializer.save(user=self.request.user)
