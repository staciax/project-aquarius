from typing import Any

from django.http import Http404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductImage, ProductInventory
from .serializers import ProductImageSerializer, ProductInventorySerializer, ProductSerializer


class ProductList(generics.ListCreateAPIView):  # type: ignore
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(APIView):  # type: ignore
    def get_product(self, id: int) -> Any:
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        product = self.get_product(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        product = self.get_product(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        product = self.get_product(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDetail(APIView):  # type: ignore
    def get_product_image(self, id: int) -> Any:
        try:
            return ProductImage.objects.get(id=id)
        except ProductImage.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        product_image = self.get_product_image(id)
        serializer = ProductImageSerializer(product_image)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        product_image = self.get_product_image(id)
        serializer = ProductImageSerializer(product_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        product_image = self.get_product_image(id)
        product_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductInventoryList(generics.ListCreateAPIView):  # type: ignore
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer


class ProductInventoryDetail(APIView):  # type: ignore
    def get_product_inventory(self, id: int) -> Any:
        try:
            return ProductInventory.objects.get(id=id)
        except ProductInventory.DoesNotExist:
            raise Http404

    def get(self, request: Request, id: int) -> Response:
        product_inventory = self.get_product_inventory(id)
        serializer = ProductInventorySerializer(product_inventory)
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        product_inventory = self.get_product_inventory(id)
        serializer = ProductInventorySerializer(product_inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        product_inventory = self.get_product_inventory(id)
        product_inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
