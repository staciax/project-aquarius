from typing import Any

from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import IsSuperUserOrIsOwner
from .serializers import UserReadByCustomerSerializer, UserRegiserSerializer, UserSerializer
from .tokens import get_tokens_for_user


class UserRegisterView(APIView):  # type: ignore
    serializer_class = UserRegiserSerializer

    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):  # type: ignore
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            return Response(
                {
                    'error': 'Email or password is incorrect',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # serializer = UserLoginSerializer(user)

        tokens = get_tokens_for_user(user)

        return Response({'message': 'User logged in successfully', 'tokens': tokens})


class UserViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    permission_classes = [IsSuperUserOrIsOwner]

    def get_serializer_class(self) -> Any:
        if not self.request.user.is_superuser:
            return UserReadByCustomerSerializer
        return super().get_serializer_class()
