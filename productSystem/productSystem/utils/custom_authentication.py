from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from django.utils.translation import gettext_lazy as _


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        if not validated_token:
            raise AuthenticationFailed(_('Invalid token.'))

        return self.get_user(validated_token), validated_token




