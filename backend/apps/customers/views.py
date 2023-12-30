from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Customer, CustomerAddress
from .serializers import CustomerAddressSerializer, CustomerSerializer


class CustomerList(generics.ListCreateAPIView):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'


# class AddressList(generics.ListCreateAPIView):  # type: ignore
#     queryset = CustomerAddress.objects.all()
#     serializer_class = CustomerAddressSerializer


# class AddressDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
#     queryset = CustomerAddress.objects.all()
#     serializer_class = CustomerAddressSerializer
#     lookup_field = 'id'


class CustomerAddressListDetail(
    mixins.CreateModelMixin,  # type: ignore
    generics.RetrieveUpdateDestroyAPIView,  # type: ignore
    GenericAPIView,  # type: ignore
):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    lookup_field = 'customer'

    def get(self, request: Request, customer: int) -> Response:
        return super().retrieve(request, customer)

    def post(self, request: Request, customer: int) -> Response:
        request.data['customer'] = customer  # NOTE: bypass serializer validation
        return super().create(request)

    def put(self, request: Request, customer: int) -> Response:
        request.data['customer'] = customer  # NOTE: bypass serializer validation
        return super().update(request)

    def delete(self, request: Request, customer: int) -> Response:
        return super().destroy(request, customer)
