from http import HTTPStatus

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateSerializer


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    lookup_url_kwarg = "email"
    lookup_field = "email"

    # def get_permissions(self):
    #     if self.action in ("create", "retrieve"):
    #         pc = [AllowAny]
    #     else:
    #         pc = [IsAuthenticated]
    #     return [p() for p in pc]

    def get_serializer(self, *args, **kwargs):
        match self.action:
            case "create":
                s = UserCreateSerializer
            case _:
                s = UserCreateSerializer
        return s(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(serializer.validated_data, status=HTTPStatus.OK)
