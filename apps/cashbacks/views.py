from rest_framework import mixins, viewsets

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.cashbacks.models import CashbackBalance, CashbackTransaction
from apps.cashbacks.serializers import CashbackBalanceSerializer, CashbackTransactionSerializer


class GetCashBackBalance(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = CashbackBalance.objects.all()
    serializer_class = CashbackBalanceSerializer


class CashbackTransactionListAPIViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CashbackTransactionSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'client_id',
                openapi.IN_QUERY,
                description="ID client for filter transaction",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        client_id = self.request.query_params.get("client_id")
        return CashbackTransaction.objects.filter(client_id=client_id).order_by('-created_at')
