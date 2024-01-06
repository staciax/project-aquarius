from rest_framework import viewsets

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'id'
