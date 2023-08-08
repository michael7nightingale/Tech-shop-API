from rest_framework import serializers

from .subcategory import SubcategoryCategorySerializer
from ..models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "id")


class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = SubcategoryCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("name", "id", "subcategories")
