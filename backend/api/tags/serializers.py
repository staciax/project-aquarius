from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
        )
