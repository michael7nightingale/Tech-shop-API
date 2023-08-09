from django.db import models


class Country(models.Model):
    name = models.CharField("Country name", db_index=True, max_length=120)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField("Region name", db_index=True, max_length=120)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField("City name", db_index=True, max_length=100)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True, related_name="cities")

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    street = models.CharField("Street", max_length=255)
    home = models.CharField("Home", max_length=20)
