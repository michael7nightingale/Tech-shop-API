from rest_framework import serializers

from .description_item import DescriptionItemListSerializer, DescriptionItemCreateSerializer
from .brand import BrandListSerializer
from ..models import Good


class GoodCreateSerializer(serializers.ModelSerializer):
    description_items = DescriptionItemCreateSerializer(many=True, required=False)

    class Meta:
        model = Good
        fields = (
            "subcategory",
            "name",
            "brand",
            "model",
            "price",
            "amount",
            "made_in_country",
            "description",
            "description_items",

        )


class GoodListSerializer(serializers.ModelSerializer):
    brand = BrandListSerializer()

    class Meta:
        model = Good
        fields = (
            "id",
            "name",
            "model",
            "brand",
            "price",
            "available",

        )


class GoodDetailSerializer(serializers.ModelSerializer):
    description_items = DescriptionItemListSerializer(many=True)
    brand = BrandListSerializer()

    class Meta:
        model = Good
        fields = (
            "id",
            "name",
            "model",
            "brand",
            "price",
            "amount",
            "description",
            "available",
            "description_items",

        )
