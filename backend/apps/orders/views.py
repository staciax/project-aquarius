from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
