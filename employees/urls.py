from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, PostViewSet


router = DefaultRouter()
router.register("employees", EmployeeViewSet, "employees")
router.register("posts", PostViewSet, "posts")


urlpatterns = [
    path("", include(router.urls)),

]
