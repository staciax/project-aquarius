from rest_framework import generics

from .models import Product, ProductImage, ProductInventory
from .serializers import ProductImageSerializer, ProductInventorySerializer, ProductSerializer


class ProductList(generics.ListCreateAPIView):  # type: ignore
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProductImageList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProductInventoryList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer


class ProductInventoryDetail(generics.RetrieveUpdateDestroyAPIView):  # type: ignore
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
