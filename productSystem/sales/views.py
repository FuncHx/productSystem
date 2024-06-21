from rest_framework import viewsets
from .models import SalesOrder, SalesDetail
from .serializers import SalesOrderSerializer, SalesDetailSerializer

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

class SalesDetailViewSet(viewsets.ModelViewSet):
    queryset = SalesDetail.objects.all()
    serializer_class = SalesDetailSerializer
