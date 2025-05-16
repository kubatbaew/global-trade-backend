from django.urls import path

from apps.users.views import GetMeAPIView


urlpatterns = [
    path("get_me/", GetMeAPIView.as_view(), name="get_me"),
]
