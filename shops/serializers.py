from rest_framework import serializers

from locations.serializers import AddressCreateSerializer, AddressDetailSerializer
from .models import Shop, ShopGood


class ShopCreateSerializer(serializers.ModelSerializer):
    address = AddressCreateSerializer()

    class Meta:
        model = Shop()
        fields = ("address", )


class ShopListSerializer(serializers.ModelSerializer):
    address = AddressDetailSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"


class ShopDetailSerializer(serializers.ModelSerializer):
    address = AddressDetailSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"


class ShopUpdateSerializer(serializers.ModelSerializer):
    address = AddressCreateSerializer(read_only=True, partial=True)

    class Meta:
        model = Shop
        fields = ("address", )


class ShopGoodCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopGood
        fields = ("shop", "good", "quantity")


class ShopGoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopGood
        fields = "__all__"


class ShopGoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopGood
        fields = "__all__"


class ShopGoodUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopGood
        fields = ("quantity", )
