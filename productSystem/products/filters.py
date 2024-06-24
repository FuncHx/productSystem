# products/filters.py
from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    product_name = filters.CharFilter(lookup_expr='icontains', required=False)
    category = filters.CharFilter(lookup_expr='icontains', required=False)
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte', required=False)
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte', required=False)
    suppliers_id = filters.NumberFilter(field_name='suppliers_id', lookup_expr='exact', required=False)

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price_min', 'price_max', 'suppliers_id']
