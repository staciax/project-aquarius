from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre
from .serializers import GenreSerializer


class GenreList(generics.ListCreateAPIView):  # type: ignore
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(APIView):  # type: ignore
    def get_genre(self, id: int) -> Any:
        try:
            return Genre.objects.get(id=id)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        genre = self.get_genre(id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        genre = self.get_genre(id)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        genre = self.get_genre(id)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
