from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from productSystem import settings
from system.views import UserCreate, AdminUserViewSet, LogoutView, MyTokenObtainPairView, UserUpdateView, \
    PasswordChangeView, FileUploadView

router = DefaultRouter()
router.register(r'adminUser', AdminUserViewSet, basename="admin_user")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suppliers.urls')),
    path('', include('products.urls')),
    path('', include('inventory.urls')),
    path('', include('sales.urls')),
    path('', include('mall_user.urls')),
    path('system/', include('system.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls), name="admin-user"),
    path('updateUserInfo/', UserUpdateView.as_view(), name="update-user-info"),
    path('editPassword/', PasswordChangeView.as_view(), name="edit-password"),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('uploadFile/', FileUploadView.as_view(), name='upload-file'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



