from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Basket, Order, BasketItem
from .serializers import (
    BasketDetailSerializer, BasketItemDetailSerializer,
    OrderDetailSerializer, OrderListSerializer, OrderCreateSerializer,

)


class BasketViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Basket.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        basket = request.user.basket
        serializer = BasketDetailSerializer(basket)
        return Response(serializer.data)


class BasketItemViewSet(mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = BasketItemDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BasketItem.objects.filter(basket=self.request.user.basket)

    def get_object(self) -> BasketItem:
        return super().get_object()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response("Item deleted.")

    @action(methods=['PATCH'], url_name="increment", detail=True)
    def increment(self, request, pk):
        item = self.get_object()
        item.increment()
        return Response("Item incremented")

    @action(methods=['PATCH'], url_name="decrement", detail=True)
    def decrement(self, request, pk):
        item = self.get_object()
        item.decrement()
        return Response("Item decremented")


class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {
            "request": self.request,

        }

    def get_object(self) -> Order:
        return self.get_object()

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        detail_serializer = OrderDetailSerializer(order)
        return Response(detail_serializer.data, status=201)
