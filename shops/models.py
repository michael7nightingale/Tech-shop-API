from django.db import models


class Shop(models.Model):
    address = models.OneToOneField(
        "locations.Address",
        on_delete=models.CASCADE,
        related_name="shop",
        unique=True,
        db_index=True
    )


class ShopGood(models.Model):
    good = models.ForeignKey("goods.Good", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Quantity")
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ("good", "shop"),

        )
