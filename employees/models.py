from django.db import models

from .service.secret_key import generate_secret_key


class Post(models.Model):
    name = models.CharField("Post name", unique=True, db_index=True, max_length=255)
    min_salary = models.DecimalField("Minimal salary", decimal_places=2, max_digits=10)
    max_salary = models.DecimalField("Maximum salary", max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name    # type: ignore


class Employee(models.Model):
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    secret_key = models.CharField(
        "Secret key",
        max_length=255,
        unique=True,
        db_index=True,
        default=generate_secret_key
    )
    shop = models.ForeignKey("shops.Shop", on_delete=models.CASCADE)
    salary = models.DecimalField("Salary", decimal_places=2, max_digits=10)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
