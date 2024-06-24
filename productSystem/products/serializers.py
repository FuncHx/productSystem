from rest_framework import serializers

from inventory.serializers import InventorySerializer
from suppliers.serializers import SupplierSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):   # 商品数据序列化器
    product_name = serializers.CharField(max_length=100, required=False)
    category = serializers.CharField(max_length=100, required=False)
    price = serializers.CharField(max_length=100, required=False)
    supplier_id = SupplierSerializer(many=False, read_only=True)
    inventory = InventorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
