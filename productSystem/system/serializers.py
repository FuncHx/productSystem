from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from system.models import AdminUser, UploadedFile


class AdminUserSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'email', 'nick_name', 'phone',
                  'update_time', 'avatar', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = AdminUser.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    自定义token序列化
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token



class UserUpdateSerializer(serializers.ModelSerializer):
    """
    用户更新序列化
    """
    class Meta:
        model = AdminUser
        fields = ['email', 'nick_name', 'phone']


class PasswordChangeSerializer(serializers.Serializer):
    """
    密码修改序列化
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['file', 'uploaded_at']
