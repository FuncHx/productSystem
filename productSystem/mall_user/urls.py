from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MallUserViewSet

router = DefaultRouter()
router.register(r'mallUser', MallUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
