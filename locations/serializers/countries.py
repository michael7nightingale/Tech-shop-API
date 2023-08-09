from rest_framework import serializers

from ..models import Country


class CountryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ("name", )


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", )
