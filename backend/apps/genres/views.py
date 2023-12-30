from rest_framework import generics

from .models import Genre
from .serializers import GenreSerializer


class GenreList(generics.ListCreateAPIView):  # type: ignore
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'
