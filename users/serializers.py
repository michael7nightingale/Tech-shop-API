from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            "email",
            "first_name",
            "last_name",
            "password"
        )
        model = User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",

        )


class ActivationSerializer(serializers.Serializer):
    # user_id = serializers.CharField()
    code = serializers.CharField(min_length=6, max_length=6)
