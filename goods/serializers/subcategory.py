from rest_framework import serializers

from ..models import Subcategory


class SubcategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ("name", "category")


class SubcategoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ("name", "id")
