from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BasketViewSet, BasketItemViewSet, OrderViewSet


router = DefaultRouter()
router.register("basket", BasketViewSet, "basket")
router.register("basket_items", BasketItemViewSet, "basket_items")
router.register("orders", OrderViewSet, "orders")


urlpatterns = [
    path("", include(router.urls)),

]
