from typing import Type

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from orders.serializers import BasketItemCreateSerializer
from .models import Good, Category, Brand
from .serializers import (
    GoodCreateSerializer, GoodDetailSerializer, GoodListSerializer,
    CategoryListSerializer, CategoryCreateSerializer, CategoryDetailSerializer,
    SubcategoryCreateSerializer,
    BrandListSerializer, BrandCreateSerializer, BrandDetailSerializer,

)


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()

    serializer_classes = {
        "create": GoodCreateSerializer,
        "list": GoodListSerializer,
        "retrieve": GoodDetailSerializer,
        "add_to_basket": BasketItemCreateSerializer,

    }

    def get_serializer_context(self):
        return {
            "request": self.request,

        }

    def get_permissions(self):
        if self.action in ("add_to_basket", ):
            permission_classes = [IsAuthenticated]
        elif self.action in ("retrieve", "create"):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [pc() for pc in permission_classes]

    def get_serializer_class(self) -> Type[ModelSerializer]:
        if self.action not in self.serializer_classes:
            return GoodDetailSerializer
            # raise AssertionError(f"Define serializer for action {self.action}!")
        return self.serializer_classes[self.action]

    @action(methods=['POST'], detail=True, url_name="add_to_basket", url_path="add-to-basket")
    def add_to_basket(self, request, pk):
        good = self.get_object()
        serializer = self.get_serializer_class()(data={**request.data, "good": pk}, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        basket_item = serializer.save()
        return Response(serializer.data, status=201)


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Category.objects.all()

    serializer_classes = {
        "create": CategoryCreateSerializer,
        "list": CategoryListSerializer,
        "retrieve": CategoryDetailSerializer,
        "subcategory_create": SubcategoryCreateSerializer,

    }

    def get_permissions(self):
        if self.action in ("retrieve", "create"):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [pc() for pc in permission_classes]

    def get_serializer_class(self):
        if self.action not in self.serializer_classes:
            raise AssertionError(f"Define serializer for action {self.action}!")
        return self.serializer_classes[self.action]

    @action(methods=['post'], detail=False, serializer_class=SubcategoryCreateSerializer)
    def subcategory_create(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Brand.objects.all()

    serializer_classes = {
        "create": BrandCreateSerializer,
        "list": BrandListSerializer,
        "retrieve": BrandDetailSerializer,

    }

    def get_serializer_class(self):
        if self.action not in self.serializer_classes:
            raise AssertionError(f"Define serializer for action {self.action}!")
        return self.serializer_classes[self.action]
