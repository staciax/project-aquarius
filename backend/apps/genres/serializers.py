from rest_framework import serializers

from .models import Genre


class GenreSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Genre
        # depth = 1
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'products',
        )
