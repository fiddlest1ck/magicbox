from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsSuperuser
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated & IsSuperuser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
