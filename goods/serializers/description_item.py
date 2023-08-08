from rest_framework import serializers

from ..models import DescriptionItem


class DescriptionItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DescriptionItem
        fields = (
            "good",
            "key",
            "value",
            "tag",

        )


class DescriptionItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionItem
        fields = (
            "good",
            "key",
            "value",
            "tag",

        )
