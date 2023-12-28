from typing import Any

from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductImage, ProductInventory
from .serializers import ProductImageSerializer, ProductInventorySerializer, ProductSerializer
