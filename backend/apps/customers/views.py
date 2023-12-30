from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import CustomerSerializer


class CustomerList(generics.ListCreateAPIView):  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(APIView):  # type: ignore
    def get_customer(self, id: int) -> Any:
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        customer = self.get_customer(id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        customer = self.get_customer(id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request: Request, id: int) -> Response:
        customer = self.get_customer(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
