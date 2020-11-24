from django.urls import path
from rest_framework_simplejwt.views import token_refresh

from auth.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', token_refresh, name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify')
]
