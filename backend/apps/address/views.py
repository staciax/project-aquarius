from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Address
from .serializers import AddressSerializer


class AddressList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetail(APIView):  # type: ignore
    def get_address(self, id: int) -> Any:
        try:
            return Address.objects.get(id=id)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        address = self.get_address(id)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        address = self.get_address(id)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        address = self.get_address(id)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
