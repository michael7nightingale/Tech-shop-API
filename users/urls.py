from django.urls import path, include, re_path

from .views import UserViewSet, ActivationAPIView


urlpatterns = [
    path("users/create/", UserViewSet.as_view({"post": "create"}), name="users"),
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path("auth/activate/", ActivationAPIView.as_view(), name='user_activate'),

]
