from rest_framework import serializers

from ..models import Brand


class BrandCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("name", "country")


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "country")


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "country", "description")
