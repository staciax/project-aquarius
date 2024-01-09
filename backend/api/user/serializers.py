from typing import Any

from rest_framework import serializers

from .models import User


class BaseUserCreateSerializer(serializers.ModelSerializer):  # type: ignore
    def create(self, validated_data: dict[str, Any]) -> User:
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user  # type: ignore


class UserSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_customer',
            'last_login',
            'created_at',
            'updated_at',
            'groups',
            'user_permissions',
        )
        read_only_fields = (
            'id',
            'last_login',
            'created_at',
            'updated_at',
            'is_customer',
        )


class UserReadByCustomerSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            # 'password',
            'cart',
            'created_at',
            'updated_at',
        )


class UserRegiserSerializer(BaseUserCreateSerializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate(self, attrs: Any) -> Any:
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)


# class UserLoginSerializer(serializers.Serializer):  # type: ignore
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField(min_length=8, max_length=128, write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'password',
#         )
