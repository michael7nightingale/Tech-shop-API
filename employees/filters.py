import django_filters

from .models import Employee, Post


class EmployeeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")

    salary = django_filters.NumberFilter()
    salary__lt = django_filters.NumberFilter(field_name="salary", lookup_expr="lt")
    salary__gt = django_filters.NumberFilter(field_name="salary", lookup_expr="gt")

    shop = django_filters.Filter(field_name="shop")
    post = django_filters.Filter(field_name="post")

    class Meta:
        model = Employee
        fields = ("salary", "first_name", "last_name", "shop", "post")


class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    min_salary = django_filters.NumberFilter()
    min_salary__lt = django_filters.NumberFilter(field_name="min_salary", lookup_expr="lt")
    min_salary__gt = django_filters.NumberFilter(field_name="min_salary", lookup_expr="gt")

    max_salary = django_filters.NumberFilter()
    max_salary__lt = django_filters.NumberFilter(field_name="max_salary", lookup_expr="lt")
    max_salary__gt = django_filters.NumberFilter(field_name="max_salary", lookup_expr="gt")

    class Meta:
        model = Post
        fields = ("name", "min_salary", "max_salary")
