from django.urls import path
from apps.users.views import GetMeAPIView, UserCreateAPIView, UserListAPIView, UserDestroyAPIView



urlpatterns = [
    path("", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/", UserDestroyAPIView.as_view(), name="users_delete"),
    path("<str:telegram_id>/", GetMeAPIView.as_view(), name="get_me"),
    path("create/", UserCreateAPIView.as_view(), name="create_user"),
]
