from rest_framework import serializers

from .cities import CityListSerializer
from ..models import Address


class AddressCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("city", "street", "home")


class AddressListSerializer(serializers.ModelSerializer):
    city = CityListSerializer(read_only=True)

    class Meta:
        model = Address
        fields = "__all__"


class AddressDetailSerializer(serializers.ModelSerializer):
    city = CityListSerializer(read_only=True)

    class Meta:
        model = Address
        fields = "__all__"


class AddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("city", "street", "home")
