from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.clients.models import Client
from apps.clients.serializers import ClientListSerializer

from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr


class ClientListAPIViewSet(ModelViewSet):
    queryset = (
        Client.objects
        .annotate(
            code_num=Cast(Substr('client_code', 4), IntegerField())
        )
        .order_by('code_num')
    )
    serializer_class = ClientListSerializer
