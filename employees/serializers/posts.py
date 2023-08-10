from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Post


class PostCreateSerializer(serializers.ModelSerializer):

    def validated_min_salary(self, min_salary: float):
        data = self.get_initial()
        if data.get('max_salary') < min_salary:
            raise ValidationError("Minimal salary must be less than maximum salary")
        return min_salary

    class Meta:
        model = Post
        fields = ('name', "min_salary", "max_salary")


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostUpdateSerializer(serializers.ModelSerializer):

    def validated_min_salary(self, min_salary: float):
        data = self.get_initial()
        if data.get('max_salary') < min_salary:
            raise ValidationError("Minimal salary must be less than maximum salary")
        return min_salary

    class Meta:
        model = Post
        fields = ('name', "min_salary", "max_salary")
