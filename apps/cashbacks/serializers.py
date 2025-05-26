from rest_framework import serializers

from apps.cashbacks.models import CashbackBalance, CashbackTransaction
from apps.clients.serializers import ClientListSerializer


class CashbackBalanceSerializer(serializers.ModelSerializer):
    client = ClientListSerializer(read_only=True)
    class Meta:
        model = CashbackBalance
        fields = [
            "id",
            "client",
            "total_earned",
            "total_used",
            "current_balance",
            "total_weight",
            "created_at",
            "updated_at",
        ]


class CashbackTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashbackTransaction
        fields = [
            "id",
            "client_id",
            "transaction_type",
            "cashback_amount",
            "amount",
            "weight",
            "balance_before",
            "balance_after",
            "description",
            "created_at",
        ]
