from rest_framework import serializers
from .models import MallUser

class MallUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MallUser
        fields = '__all__'
