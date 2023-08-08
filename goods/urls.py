from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GoodViewSet, CategoryViewSet, BrandViewSet


router = DefaultRouter()
router.register("goods", GoodViewSet, "goods")
router.register("categories", CategoryViewSet, "categories")
router.register("brands", BrandViewSet, "brands")


urlpatterns = [
    path('', include(router.urls)),

]
