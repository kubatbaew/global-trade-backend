from django.urls import path

from apps.clients.views import ClientListAPIView


urlpatterns = [
    path("clients/", ClientListAPIView.as_view(), name="client_list"),
]
