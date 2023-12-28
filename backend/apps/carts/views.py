from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart
from .serializers import CartSerializer


class CartList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetail(APIView):  # type: ignore
    def get_cart(self, id: int) -> Any:
        try:
            return Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        cart = self.get_cart(id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        cart = self.get_cart(id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        cart = self.get_cart(id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
