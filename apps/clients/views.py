from rest_framework.generics import ListAPIView

from apps.clients.models import Client
from apps.clients.serializers import ClientListSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
