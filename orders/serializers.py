from rest_framework import serializers

from goods.serializers import GoodListSerializer
from .models import Order, Basket, BasketItem


class BasketItemCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BasketItem
        fields = ("good", "quantity", "user")

    def save(self, **kwargs):
        kwargs.update(self.validated_data)
        basket_item = BasketItem.objects.create(
            quantity=kwargs["quantity"],
            basket=kwargs['user'].basket,
            good=kwargs['good']
        )
        return basket_item


class BasketItemDetailSerializer(serializers.ModelSerializer):
    good = GoodListSerializer(read_only=True)

    class Meta:
        model = BasketItem
        fields = ("id", "good", "quantity", "total_price")


class BasketDetailSerializer(serializers.ModelSerializer):
    basket_items = BasketItemDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ("id", "basket_items", "total_price")


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = (
            "user",
            "city",
            "street",
            "home",
            "home_number",

        )

    def save(self, **kwargs):
        kwargs.update(basket=self.validated_data.get('user').basket)
        order = super().save(**kwargs)
        self.validated_data.get('user').add_new_basket()
        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    basket = BasketDetailSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            "basket",
            "city",
            "street",
            "home",
            "home_number",
            "paid",
            "time_created",
            "time_delivered",

        )


class OrderListSerializer(serializers.ModelSerializer):
    basket = BasketDetailSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            "basket",
            "paid",
            "time_created",
            "time_delivered",

        )
