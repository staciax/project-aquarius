from pathlib import Path
from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product, ProductImage
from .serializers import (
    ProductCreateSerializer,
    ProductImageSerializer,
    ProductReadSerializer,
    ProductSerializer,
    ProductUpdateSerializer,
)

# from rest_framework.decorators import action


class ProductImageList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'product'

    def get(self, request: Request, product: int) -> Response:
        queryset = self.get_queryset()
        images = queryset.filter(product_id=product)
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Any:
        request.data['product'] = kwargs['product']
        return super().create(request, *args, **kwargs)


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = ('product', 'id')

    def get_object(self) -> Any:
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_field:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()

        # delete image file
        fp = Path(instance.image.path).resolve()
        if fp.exists():
            fp.unlink()

        # delete in database
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Product.objects.all()  # database model
    serializer_class = ProductSerializer  # serializer แปลงข้อมูลจาก database model ให้เป็น json
    lookup_field = 'id'

    # filters
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('is_available', 'genre', 'tags')
    ordering_fields = ('id', 'title', 'price', 'created_at')
    search_fields = ('title', 'description', 'author')

    def get_serializer_class(self) -> Any:
        if self.action in ('list', 'retrieve'):
            return ProductReadSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        elif self.action == 'update':
            return ProductUpdateSerializer
        return super().get_serializer_class()

    # /products/<id>/images/
    # @action(detail=True)  # type: ignore
    # def images(self, request: Any, id=None) -> Any:
    #     return Response()

    # @images.mapping.post  # type: ignore
    # def add_image(self, request: Any, id=None) -> Any:
    #     return Response()


# class ProductImageViewSet(viewsets.ModelViewSet):  # type: ignore
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer
#     lookup_field = 'id'
