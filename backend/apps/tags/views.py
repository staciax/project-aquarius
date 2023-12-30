from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag
from .serializers import TagSerializer


class TagList(generics.ListCreateAPIView):  # type: ignore
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(APIView):  # type: ignore
    def get_tag(self, id: int) -> Any:
        try:
            return Tag.objects.get(id=id)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        tag = self.get_tag(id)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        tag = self.get_tag(id)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        tag = self.get_tag(id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
