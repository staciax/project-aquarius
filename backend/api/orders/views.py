from datetime import datetime

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Order, OrderItem, OrderStatus
from .serializers import OrderItemSerializer, OrderSerializer


def order_change_status(order_id: int, status: OrderStatus) -> Response:
    order: Order = get_object_or_404(Order, id=order_id)
    order.status = status

    tz_now = datetime.now(timezone.get_default_timezone())
    if status == OrderStatus.APPROVED:
        order.approved_at = tz_now
    elif status == OrderStatus.SHIPPED:
        order.shipped_at = tz_now
    elif status == OrderStatus.CANCELED:
        order.canceled_at = tz_now
    elif status == OrderStatus.COMPLETED:
        order.completed_at = tz_now

    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['POST'])  # type: ignore
def approve_order(request: Request, order_id: int) -> Response:
    return order_change_status(order_id, OrderStatus.APPROVED)  # type: ignore


@api_view(['POST'])  # type: ignore
def ship_order(request: Request, order_id: int) -> Response:
    return order_change_status(order_id, OrderStatus.SHIPPED)  # type: ignore


@api_view(['POST'])  # type: ignore
def cancel_order(request: Request, order_id: int) -> Response:
    return order_change_status(order_id, OrderStatus.CANCELED)  # type: ignore


@api_view(['POST'])  # type: ignore
def complete_order(request: Request, order_id: int) -> Response:
    return order_change_status(order_id, OrderStatus.COMPLETED)  # type: ignore


class OrderViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    # filters
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('customer', 'status')


class OrderItemListCreateView(generics.ListCreateAPIView):  # type: ignore
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'

    # def get_serializer_class(self) -> Any:
    #     if self.request.method == 'POST':
    #         return CartItemCreateSerializer
    #     return super().get_serializer_class()

    # def post(self, request: Request, cart_id: int) -> Response:
    #     # if not 'cart' in request.data:
    #     request.data['cart'] = cart_id
    #     # NOTE: replace 'cart' from request data because this endpoint is only for a specific cart
    #     return super().post(request)


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = ('order', 'product')

    # def get_serializer_class(self) -> Any:
    #     if self.request.method == 'GET':
    #         return CartItemReadSerializer
    #     elif self.request.method == 'PUT':
    #         return CartItemUpdateSerializer
    #     return super().get_serializer_class()

    # def get_object(self) -> Any:
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.lookup_field:
    #         filter[field] = self.kwargs[field]

    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
