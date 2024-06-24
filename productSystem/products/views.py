from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['post'], url_path='search')
    def filter_products(self, request):
        request.query_params._mutable = True
        request.query_params.update(request.data)
        request.query_params._mutable = False
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        data['code'] = 200
        return Response(data)

    def filter_queryset(self, queryset):
        filter_backends = self.filter_backends or ()
        print(filter_backends)
        for backend in filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
