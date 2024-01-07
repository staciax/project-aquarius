from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = User
        fields = '__all__'
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
        )
