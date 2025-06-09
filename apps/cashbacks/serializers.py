from rest_framework import serializers

from apps.cashbacks.models import CashbackBalance, CashbackTransaction


class CashbackBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashbackBalance
        fields = [
            "id",
            "user",
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
            "user",
            "transaction_type",
            "cashback_amount",
            "amount",
            "weight",
            "balance_before",
            "balance_after",
            "description",
            "created_at",
        ]
