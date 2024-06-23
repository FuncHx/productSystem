from django.contrib.auth import update_session_auth_hash
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import AdminUser, UserToken, UploadedFile
from .serializers import AdminUserSerializer, MyTokenObtainPairSerializer, UserUpdateSerializer, \
    PasswordChangeSerializer, UploadedFileSerializer


class UserCreate(generics.CreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    """
    用户登录视图
    """
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = AdminUser.objects.get(username=request.data['username'])
            refresh_token = response.data['refresh']
            UserToken.objects.update_or_create(user=user, defaults={'refresh_token': refresh_token})
            response.data.pop("refresh") # 删除refresh token，防止泄露
            response.data["code"] = 200
        return response


class LogoutView(APIView):
    """
    用户登出视图
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            user_token = UserToken.objects.get(user=user)
            refresh_token = user_token.refresh_token
            token = RefreshToken(refresh_token)
            token.blacklist()

            user_token.delete()  # 删除用户的刷新令牌记录

            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except UserToken.DoesNotExist:
            return Response({"error": "No token found for user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AdminUserViewSet(viewsets.ModelViewSet):
    """
    管理员用户视图集
    """
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path="editAvatar")
    def edit_avatar(self, request):
        user = self.request.user
        # 手动更新用户avatar内容
        try:
            user.avatar = request.data['avatar']
            user.save()
            return Response({"code": 200, "message": "头像更新成功"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"code": 200, "message": str(e)}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path="userInfo")
    def get_user_info(self, request):
        user = self.request.user
        serializer = AdminUserSerializer(user)
        return Response({"code": 200, "data": serializer.data})

    @action(detail=False, methods=['get'], url_path="logout")
    def logout(self, request):
        try:
            token = RefreshToken()
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(generics.UpdateAPIView):
    """
    用户信息更新视图
    """
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = UserUpdateSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "用户信息更新成功", "code": 200}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "code": 200}, status=status.HTTP_200_OK)


class PasswordChangeView(APIView):
    """
    用户密码修改视图
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"message": "旧密码输入错误", "code": 201}, status=status.HTTP_200_OK)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            update_session_auth_hash(request, user)  # 防止用户密码修改后被登出
            return Response({"message": "密码修改成功", "code": 200}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "code": 201}, status=status.HTTP_200_OK)


class FileUploadView(generics.CreateAPIView):
    """
    文件上传视图
    """
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 拼接文件返回链接，加上当前服务器地址
            file_url = request.build_absolute_uri(serializer.data["file"])
            data = serializer.data
            data["file"] = file_url
            # 处理文件上传后的逻辑, 获取上传后的文件链接等信息
            return Response({"message": "文件上传成功！", "code": 200, "data": data}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "code": 200}, status=status.HTTP_200_OK)