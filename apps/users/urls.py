from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import GetMeAPIView, UserCreateAPIView



urlpatterns = [
    path("get_me/", GetMeAPIView.as_view(), name="get_me"),
    path("create/", UserCreateAPIView.as_view(), name="create_user"),
    path('login/', TokenObtainPairView.as_view(), name='token_create_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
