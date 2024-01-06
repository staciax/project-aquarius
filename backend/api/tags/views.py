from rest_framework import viewsets

from .models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
