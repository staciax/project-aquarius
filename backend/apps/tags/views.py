from typing import Any

from django.http import Http404
from rest_framework import generics

from .models import Tag
from .serializers import TagSerializer


class TagList(generics.ListCreateAPIView):  # type: ignore
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
