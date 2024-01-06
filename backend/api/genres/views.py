from rest_framework import viewsets

from .models import Genre
from .serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
