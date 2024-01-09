from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404

from api.permissions import IsCustomer

from .models import Cart, CartItem
from .permissions import CartPermission
from .serializers import (
    CartItemCreateSerializer,
    CartItemReadSerializer,
    CartItemSerializer,
    CartItemUpdateSerializer,
    CartReadSerializer,
    CartSerializer,
)

if TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.response import Response


class CartViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'

    permission_classes = (CartPermission,)

    def get_serializer_class(self) -> Any:
        if self.action in ('list', 'retrieve'):
            return CartReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer: CartSerializer) -> None:
        serializer.save(user=self.request.user)


class CartItemListCreateView(generics.ListCreateAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'

    def get_serializer_class(self) -> Any:
        if self.request.method == 'POST':
            return CartItemCreateSerializer
        return super().get_serializer_class()

    def post(self, request: Request, cart_id: int) -> Response:
        # if not 'cart' in request.data:
        request.data['cart'] = cart_id
        # NOTE: replace 'cart' from request data because this endpoint is only for a specific cart
        return super().post(request)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = ('cart', 'product')

    def get_serializer_class(self) -> Any:
        if self.request.method == 'GET':
            return CartItemReadSerializer
        elif self.request.method == 'PUT':
            return CartItemUpdateSerializer
        return super().get_serializer_class()

    def get_object(self) -> Any:
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_field:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class CartMeView(generics.RetrieveAPIView):  # type: ignore
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self) -> Any:
        return self.request.user.cart

    permission_classes = (IsCustomer,)
