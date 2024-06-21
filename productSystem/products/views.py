from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['price', 'stock_quantity']

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        return Response({'message': 'This is a search endpoint'})
