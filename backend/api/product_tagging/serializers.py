from rest_framework import serializers

from .models import ProductTagging


class ProductTaggingSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = ProductTagging
        fields = '__all__'
