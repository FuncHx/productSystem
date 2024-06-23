from rest_framework import viewsets
from .models import MallUser
from .serializers import MallUserSerializer

class MallUserViewSet(viewsets.ModelViewSet):
    queryset = MallUser.objects.all()
    serializer_class = MallUserSerializer
