from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import (
    ShopListSerializer, ShopDetailSerializer, ShopCreateSerializer, ShopUpdateSerializer,
    ShopGoodListSerializer, ShopGoodCreateSerializer, ShopGoodDetailSerializer, ShopGoodUpdateSerializer

)

from .models import Shop, ShopGood


class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Shop.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return ShopCreateSerializer
            case "list":
                return ShopListSerializer
            case "update":
                return ShopUpdateSerializer
            case "retrieve":
                return ShopDetailSerializer
            case "goods":
                return ShopGoodListSerializer
            case _:
                return ShopDetailSerializer

    @action(methods=['GET'], detail=True)
    def goods(self, request, pk):
        shop = self.get_object()
        shop_goods = ShopGood.objects.filter(shop=shop)
        serializer = self.get_serializer_class()(shop_goods, many=True)
        return Response(serializer.data)


class ShopGoodViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ShopGood.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return ShopGoodCreateSerializer
            case "list":
                return ShopGoodListSerializer
            case "update":
                return ShopGoodUpdateSerializer
            case "retrieve":
                return ShopGoodDetailSerializer
            case _:
                return ShopGoodDetailSerializer
