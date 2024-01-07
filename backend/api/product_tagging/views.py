from rest_framework import viewsets

from api.permissions import IsSuperUser

from .models import ProductTagging
from .serializers import ProductTaggingSerializer


class ProductTagViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = ProductTagging.objects.all()
    serializer_class = ProductTaggingSerializer
    lookup_field = 'id'

    permission_classes = [IsSuperUser]
