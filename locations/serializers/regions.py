from rest_framework import serializers

from .countries import CountryListSerializer
from ..models import Region


class RegionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("country", "name")


class RegionListSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(read_only=True)

    class Meta:
        model = Region
        fields = "__all__"


class RegionDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(read_only=True)

    class Meta:
        model = Region
        fields = "__all__"


class RegionUpdateSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(read_only=True)

    class Meta:
        model = Region
        fields = ("country", "name")
