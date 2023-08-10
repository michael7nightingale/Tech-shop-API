from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# from rest_framework.exceptions import NotFound

from orders.models import Basket


class UserManager(UserManager):
    def create_user(
            self,
            email: str,
            password: str,
            first_name: str,
            last_name: str
    ):
        user = self.model(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=False
        )
        user.password = make_password(password)
        user.save(using=self._db)
        basket = Basket.objects.create(user=user)
        return user

    def create_superuser(
            self,
            email: str,
            password: str,
            first_name: str,
            last_name: str
    ):
        user = self.model(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_superuser=True,
            is_staff=True,
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    # def get(self, *args, **kwargs):
    #     try:
    #         return super().get(*args, **kwargs)
    #     except self.model.DoesNotExist:
    #         raise NotFound

    def are_you_blocked(self, you, other) -> bool:
        return other.black_list.filter(id=you.id).exists()

    def is_blocked_by_you(self, you, other) -> bool:
        return you.black_list.filter(id=other.id).exists()

    # def filter(self, **kwargs):
    #     return (
    #         super()
    #         .prefetch_related("chats")
    #         .filter(**kwargs)
    #     )
    #
    # def all(self):
    #     return (
    #         super()
    #         .prefetch_related("chats")
    #         .all()
    #     )


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    @property
    def basket(self) -> Basket:
        return Basket.objects.filter(user=self).last()

    def add_new_basket(self) -> Basket:
        basket = Basket.objects.create(user=self)
        return basket

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
