import math

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=120, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class CountryChoices(models.TextChoices):
    Russia = "RUSSIA", "Russia"
    China = "CHINA", "China"
    Korea = "KOREA", "Korea"


class Good(models.Model):
    subcategory = models.ForeignKey(
        "Subcategory",
        on_delete=models.CASCADE,
        related_name="goods"
    )
    name = models.CharField(max_length=120, db_index=True)
    model = models.CharField(max_length=130, db_index=True)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    description = models.TextField()
    images = models.ManyToManyField(to="self", through="GoodImage")
    made_in_country = models.CharField(max_length=100, choices=CountryChoices.choices)
    amount = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)

    @property
    def available(self):
        return bool(self.amount)

    class Meta:
        unique_together = (("name", "model", "brand"), )


class Brand(models.Model):
    name = models.CharField(max_length=120, db_index=True, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100, choices=CountryChoices.choices)

    def __str__(self):
        return self.name


class GoodImage(models.Model):
    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE
    )
    image = models.ImageField()


class DescriptionItem(models.Model):

    class DescriptionItemTagChoices(models.TextChoices):
        size = "SIZE", "Size"
        accumulator = "ACCUMUlATOR", "Accumulator"
        processor = "PROCESSOR", "processor"

    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE,
        related_name="description_items"
    )
    key = models.CharField(max_length=70)
    value = models.CharField(max_length=100)
    tag = models.CharField(choices=DescriptionItemTagChoices.choices, max_length=100)

    def __str__(self):
        return f"{self.key}: {self.value} ({self.tag})"
