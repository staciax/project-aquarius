from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductImage, ProductInventory
from .serializers import ProductImageSerializer, ProductInventorySerializer, ProductSerializer


class ProductList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ProductImageList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        product_image = ProductImage.objects.all()
        serializer = ProductImageSerializer(product_image, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ProductInventoryList(APIView):  # type: ignore
    def get(self, request: Request) -> Response:
        product_inventory = ProductInventory.objects.all()
        serializer = ProductInventorySerializer(product_inventory, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ProductInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
