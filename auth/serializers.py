from rest_framework_simplejwt import serializers as simplejwt_serializers
from rest_framework_simplejwt.tokens import UntypedToken

from users.models import User


class TokenObtainPairSerializer(simplejwt_serializers.TokenObtainPairSerializer):
    def validate(self, data):
        data = super().validate(data)
        data['user_type'] = self.user.user_type
        return data


class TokenVerifySerializer(simplejwt_serializers.TokenVerifySerializer):
    def validate(self, attrs):
        token_obj = UntypedToken(attrs['token'])
        user = User.objects.get(pk=token_obj.payload['user_id'])
        return {'user_type': user.user_type, 'username': user.username}
