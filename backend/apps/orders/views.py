from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderList(generics.ListCreateAPIView):  # type: ignore
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailByCustomer(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'customer_id'


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
