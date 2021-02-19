from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase

from auth.serializers import TokenObtainPairSerializer, TokenVerifySerializer


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenVerifyView(TokenViewBase):
    serializer_class = TokenVerifySerializer
