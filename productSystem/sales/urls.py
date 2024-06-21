from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesOrderViewSet, SalesDetailViewSet

router = DefaultRouter()
router.register(r'sales-orders', SalesOrderViewSet)
router.register(r'sales-details', SalesDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
