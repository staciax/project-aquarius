from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderList(generics.ListCreateAPIView):  # type: ignore
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(APIView):  # type: ignore
    def get_order(self, id: int) -> Any:
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        order = self.get_order(id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        order = self.get_order(id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        order = self.get_order(id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
