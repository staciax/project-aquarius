from rest_framework import generics

from .models import Payment
from .serializers import PaymentSerializer


class PaymentList(generics.ListCreateAPIView):  # type: ignore
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
