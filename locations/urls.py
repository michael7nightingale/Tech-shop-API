from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, RegionViewSet, CityViewSet


router = DefaultRouter()
router.register("countries", CountryViewSet, "countries")
router.register("regions", RegionViewSet, "regions")
router.register("cities", CityViewSet, "cities")


urlpatterns = [
    path("", include(router.urls)),

]
