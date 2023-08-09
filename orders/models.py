from django.db import models


class Basket(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="baskets"
    )

    def clear(self) -> None:
        for basket_item in self.basket_items.all():
            basket_item.delete()

    @property
    def total_price(self) -> float:
        return sum(i.total_price for i in self.basket_items.all())


class BasketItem(models.Model):
    good = models.ForeignKey(
        "goods.Good",
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    basket = models.ForeignKey(
        "Basket",
        on_delete=models.CASCADE,
        related_name="basket_items"
    )

    def increment(self) -> None:
        self.quantity += 1
        self.save()

    def decrement(self) -> None:
        if self.quantity == 1:
            self.delete()
        else:
            self.quantity -= 1
            self.save()

    @property
    def total_price(self) -> float:
        return self.quantity * float(self.good.price)


class Order(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders"
    )
    basket = models.ForeignKey(
        "Basket",
        on_delete=models.CASCADE,
        related_name="orders"
    )
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    home = models.CharField(max_length=20)
    time_created = models.DateTimeField(auto_created=True, auto_now=True)
    time_delivered = models.DateTimeField(null=True)
    paid = models.BooleanField(default=False)

    def set_payed(self) -> None:
        self.paid = True
        self.save()
