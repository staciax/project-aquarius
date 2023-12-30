from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer


class CustomerList(generics.ListCreateAPIView):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'
