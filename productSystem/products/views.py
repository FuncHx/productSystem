from rest_framework import viewsets, filters

from productSystem.utils.PaginationUtil import PaginationUtil
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    pagination_class = PaginationUtil
    ordering_fields = ['price', 'stock_quantity']
