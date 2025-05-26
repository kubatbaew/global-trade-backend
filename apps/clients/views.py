from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.clients.models import Client
from apps.clients.serializers import ClientListSerializer


class ClientListAPIViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
