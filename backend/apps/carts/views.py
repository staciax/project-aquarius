from rest_framework import generics

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


class CartList(generics.ListCreateAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class CartDetailByCustomer(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'customer_id'
    lookup_url_kwarg = 'customer_id'


class CartItemList(generics.ListCreateAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
