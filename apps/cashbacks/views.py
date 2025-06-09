from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from decimal import Decimal

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth import get_user_model

from apps.cashbacks.models import CashbackBalance, CashbackTransaction
from apps.cashbacks.serializers import CashbackBalanceSerializer, CashbackTransactionSerializer


User = get_user_model()

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
                'user_id',
                openapi.IN_QUERY,
                description="ID user for filter transaction",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return CashbackTransaction.objects.filter(user=user_id).order_by('-created_at')


class CashbackTransactionViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'cashback_amount'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'cashback_amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal'),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal'),
                'weight': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal'),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: CashbackTransactionSerializer}
    )
    @action(detail=False, methods=['post'], url_path='earn')
    def earn_cashback(self, request):
        data = request.data
        user_id = data.get("user_id")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not defined"})
        
        cashback_amount = Decimal(data.get("cashback_amount", 0))
        amount = data.get("amount")
        weight = data.get("weight")
        description = data.get("description", "")

        try:
            balance = CashbackBalance.objects.get(user=user)
        except CashbackBalance.DoesNotExist:
            return Response({"detail": "Баланс не найден"}, status=status.HTTP_404_NOT_FOUND)

        balance_before = balance.current_balance
        balance.current_balance += cashback_amount
        balance.total_earned += cashback_amount
        if weight:
            balance.total_weight += Decimal(weight)
        balance.save()

        transaction = CashbackTransaction.objects.create(
            user=user,
            transaction_type='EARNED',
            cashback_amount=cashback_amount,
            amount=amount,
            weight=weight,
            balance_before=balance_before,
            balance_after=balance.current_balance,
            description=description
        )
        return Response(CashbackTransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'cashback_amount'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'cashback_amount': openapi.Schema(type=openapi.TYPE_NUMBER, format='decimal'),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: CashbackTransactionSerializer}
    )
    @action(detail=False, methods=['post'], url_path='use')
    def use_cashback(self, request):
        data = request.data
        user_id = data.get("user_id")


        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not defined"})

        cashback_amount = Decimal(data.get("cashback_amount", 0))
        description = data.get("description", "")

        try:
            balance = CashbackBalance.objects.get(user=user)
        except CashbackBalance.DoesNotExist:
            return Response({"detail": "Баланс не найден"}, status=status.HTTP_404_NOT_FOUND)

        if balance.current_balance < cashback_amount:
            return Response({"detail": "Недостаточно средств на кешбэк-балансе"}, status=status.HTTP_400_BAD_REQUEST)

        balance_before = balance.current_balance
        balance.current_balance -= cashback_amount
        balance.total_used += cashback_amount
        balance.save()

        transaction = CashbackTransaction.objects.create(
            user=user,
            transaction_type='USED',
            cashback_amount=cashback_amount,
            balance_before=balance_before,
            balance_after=balance.current_balance,
            description=description
        )
        return Response(CashbackTransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)