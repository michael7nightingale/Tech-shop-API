from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import (
    CountryListSerializer, CountryDetailSerializer, CountryCreateSerializer, CountryUpdateSerializer,
    RegionListSerializer, RegionDetailSerializer, RegionCreateSerializer, RegionUpdateSerializer,
    CityListSerializer, CityDetailSerializer, CityCreateSerializer, CityUpdateSerializer,

)

from .models import Country, Region, City, Address


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Country.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return CountryCreateSerializer
            case "list":
                return CountryListSerializer
            case "update":
                return CountryUpdateSerializer
            case "retrieve":
                return CountryDetailSerializer
            case _:
                return CountryDetailSerializer


class RegionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Region.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return RegionCreateSerializer
            case "list":
                return RegionListSerializer
            case "update":
                return RegionUpdateSerializer
            case "retrieve":
                return RegionDetailSerializer
            case _:
                return RegionDetailSerializer


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = City.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return CityCreateSerializer
            case "list":
                return CityListSerializer
            case "update":
                return CityUpdateSerializer
            case "retrieve":
                return CityDetailSerializer
            case _:
                return CityDetailSerializer
