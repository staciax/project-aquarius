from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsSuperUser

from .models import User
from .serializers import UserRegiserSerializer, UserSerializer
from .tokens import get_tokens_for_user


class UserRegisterView(APIView):  # type: ignore
    serializer_class = UserRegiserSerializer

    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_customer=True)
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

        # serializer = UserSerializer(user)

        tokens = get_tokens_for_user(user)

        return Response({'message': 'User logged in successfully', 'tokens': tokens})


class UserViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    permission_classes = [IsSuperUser]
