from typing import Any

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product, ProductImage, ProductInventory
from .serializers import ProductImageSerializer, ProductInventorySerializer, ProductSerializer


class ProductImageList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

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


class ProductList(generics.ListCreateAPIView):  # type: ignore
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


# class ProductImageList(generics.ListCreateAPIView):  # type: ignore
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer


# class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'id'


class ProductInventoryList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer


class ProductInventoryDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
