from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Address
from .serializers import AddressSerializer

# Create your views here.


class AddressList(APIView):  # type: ignore
    def get(self, request: HttpRequest) -> JsonResponse:
        ...

    def post(self, request: HttpRequest) -> JsonResponse:
        ...

    def put(self, request: HttpRequest) -> JsonResponse:
        ...

    def delete(self, request: HttpRequest) -> JsonResponse:
        ...


def root(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Welcome to the address app!'}, status=200)


@api_view(['GET'])  # type: ignore
def get_address(request: HttpRequest) -> JsonResponse:
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return JsonResponse(serializer.data, safe=False)
