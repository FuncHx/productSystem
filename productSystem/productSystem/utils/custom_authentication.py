from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from rest_framework.response import Response


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise AuthenticationFailed(detail={'code': 401, 'message': '未登录'}, code=200)
        return super().authenticate(request)





