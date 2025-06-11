from rest_framework import viewsets, mixins
from apps.currencies.models import Currency
from .serializers import CurrencySerializer

class CurrencyViewSet(mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
