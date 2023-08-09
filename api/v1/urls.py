from django.urls import path, include

urlpatterns = [
    path("", include("goods.urls")),
    path("", include("users.urls")),
    path("", include("orders.urls")),
    path("", include("locations.urls")),

]
