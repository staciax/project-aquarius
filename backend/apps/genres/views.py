from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre
from .serializers import GenreSerializer


class GenreList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
