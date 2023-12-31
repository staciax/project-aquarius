from typing import Any

from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartItemReadSerializer, CartItemSerializer, CartSerializer


class CartList(generics.ListCreateAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'


class CartDetailByCustomer(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'customer_id'


class CartItemList(generics.ListCreateAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'


class CartItemCreateDetail(
    mixins.CreateModelMixin,  # type: ignore
    mixins.ListModelMixin,  # type: ignore
    generics.RetrieveUpdateDestroyAPIView,  # type: ignore
    GenericAPIView,  # type: ignore
):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'cart'

    def post(self, request: Request, cart: int) -> Response:
        request.data['cart'] = cart  # NOTE: bypass serializer validation
        return super().create(request)

    def get(self, request: Request, cart: int) -> Response:
        return self.list(request, cart=cart)

    def get_serializer_class(self) -> Any:
        if self.request.method == 'GET':
            return CartItemReadSerializer
        return super().get_serializer_class()


class CartItemUpdateDelete(
    mixins.UpdateModelMixin,  # type: ignore
    mixins.DestroyModelMixin,  # type: ignore
    GenericAPIView,  # type: ignore
):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = ('cart', 'product')

    def get_object(self) -> Any:
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_field:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        request.data['product'] = kwargs['product']  # NOTE: bypass serializer validation
        request.data['cart'] = kwargs['cart']
        return super().update(request)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        request.data['product'] = kwargs['product']  # NOTE: bypass serializer validation
        request.data['cart'] = kwargs['cart']
        return self.destroy(request)
