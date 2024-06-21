from rest_framework import serializers
from .models import SalesOrder, SalesDetail

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'

class SalesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetail
        fields = '__all__'
