from rest_framework import serializers

from .regions import RegionListSerializer
from ..models import City


class CityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("region", "name")


class CityListSerializer(serializers.ModelSerializer):
    country = RegionListSerializer(read_only=True)

    class Meta:
        model = City
        fields = "__all__"


class CityDetailSerializer(serializers.ModelSerializer):
    country = RegionListSerializer(read_only=True)

    class Meta:
        model = City
        fields = "__all__"


class CityUpdateSerializer(serializers.ModelSerializer):
    region = RegionListSerializer(read_only=True)

    class Meta:
        model = City
        fields = ("region", "name")
