from django.core.cache import cache
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from http import HTTPStatus
import datetime

from .models import User
from .serializers import UserCreateSerializer, ActivationSerializer
from .service.email import send_email


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    lookup_url_kwarg = "email"
    lookup_field = "email"

    def get_permissions(self):
        if self.action in ("create", ):
            pc = [AllowAny]
        else:
            pc = [IsAuthenticated]
        return [p() for p in pc]

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
        try:
            user = User.objects.get(email=serializer.validated_data.get('email'))
        except User.DoesNotExist:
            pass
        else:
            return Response({"detail": "Data is invalid."}, status=HTTPStatus.BAD_REQUEST)
        send_email(serializer.validated_data)
        return Response(serializer.validated_data, status=HTTPStatus.OK)


class ActivationAPIView(generics.CreateAPIView):
    serializer_class = ActivationSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        data = cache.get(code)
        time_now = datetime.datetime.now()
        if time_now >= data['exp']:
            cache.delete(code)
            return Response({"detail": "Code is expired."}, status=400)
        user = User.objects.create_user(**data['user'])
        user.is_active = True
        user.save()
        cache.delete(code)
        return Response({"detail": "User is created successfully."})
