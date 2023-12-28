from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer


class PaymentList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):  # type: ignore
    def get_payment(self, id: int) -> Any:
        try:
            return Payment.objects.get(id=id)
        except Payment.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        payment = self.get_payment(id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        payment = self.get_payment(id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        payment = self.get_payment(id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
