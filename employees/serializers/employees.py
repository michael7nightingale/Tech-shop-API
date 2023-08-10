from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shops.serializers import ShopListSerializer
from employees.models import Post, Employee


class EmployeeCreateSerializer(serializers.ModelSerializer):

    def validate_salary(self, salary: int):
        data = self.get_initial()
        post = get_object_or_404(Post, id=data.get("post"))
        if not (post.min_salary <= salary <= post.max_salary):
            raise ValidationError(f"Salary for post {post} must be in range [{post.min_salary}; {post.max_salary}]")
        return salary

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "shop", "salary", "post")


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "shop", "salary", "post")


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "shop", "salary", "post")


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "shop", "salary", "post", "secret_key")


class EmployeeLoginSerializer(serializers.ModelSerializer):

    def login(self):
        employee = get_object_or_404(Employee, **self.validated_data)
        return employee

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "secret_key")


class EmployeeMeSerializer(serializers.ModelSerializer):
    shop = ShopListSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "shop", "salary", "post", "secret_key")
