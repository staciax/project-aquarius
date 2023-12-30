from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


class CartList(generics.ListCreateAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


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


class CartDetailByCustomer(APIView):  # type: ignore
    def get_cart(self, customer_id: int) -> Any:
        try:
            return Cart.objects.get(customer_id=customer_id)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request: Request, customer_id: int) -> Response:
        cart = self.get_cart(customer_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request: Request, customer_id: int) -> Response:
        cart = self.get_cart(customer_id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request: Request, customer_id: int) -> Response:
        cart = self.get_cart(customer_id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemList(generics.ListCreateAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetail(APIView):  # type: ignore
    def get_cart_item(self, id: int) -> Any:
        try:
            return CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        cart_item = self.get_cart_item(id)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        cart_item = self.get_cart_item(id)
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request: Request, id: int) -> Response:
        cart_item = self.get_cart_item(id)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
