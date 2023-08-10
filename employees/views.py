from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from .filters import EmployeeFilter, PostFilter
from .serializers import (
    EmployeeMeSerializer, EmployeeLoginSerializer,
    EmployeeUpdateSerializer, EmployeeListSerializer, EmployeeCreateSerializer, EmployeeDetailSerializer,
    PostUpdateSerializer, PostListSerializer, PostCreateSerializer, PostDetailSerializer,
)

from .models import Employee, Post


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_permissions(self):
        if self.action in ("me", ):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [pc() for pc in permission_classes]

    def get_serializer_class(self):
        match self.action:
            case "create":
                return EmployeeCreateSerializer
            case "list":
                return EmployeeListSerializer
            case "update":
                return EmployeeUpdateSerializer
            case "retrieve":
                return EmployeeDetailSerializer
            case "me":
                return EmployeeLoginSerializer
            case _:
                return EmployeeDetailSerializer

    def list(self, request, *args, **kwargs):
        queryset = EmployeeFilter(queryset=self.get_queryset(), data=request.GET)
        serializer = self.get_serializer_class()(queryset.qs, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def me(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.login()
        detail_serializer = EmployeeMeSerializer(employee)
        return Response(detail_serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        match self.action:
            case "create":
                return PostCreateSerializer
            case "list":
                return PostListSerializer
            case "update":
                return PostUpdateSerializer
            case "retrieve":
                return PostDetailSerializer
            case _:
                return PostDetailSerializer

    def list(self, request, *args, **kwargs):
        queryset = PostFilter(queryset=self.get_queryset(), data=request.GET)
        serializer = self.get_serializer_class()(queryset.qs, many=True)
        return Response(serializer.data)
