from rest_framework import serializers

from django.contrib.auth import get_user_model

from apps.cashbacks.models import CashbackBalance, CashbackTransaction
from apps.clients.serializers import ClientListSerializer

User = get_user_model()


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


class UserTransactionSerializer(serializers.ModelSerializer):
    client = ClientListSerializer(read_only=True)
    balance = CashbackBalanceSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "telegram_id",
            "client",
            "balance",
            # "is_admin",
        ]
        read_only_fields = [
            # "is_admin",
            "id",
        ]


class CashbackTransactionSerializer(serializers.ModelSerializer):
    user = UserTransactionSerializer(read_only=True)
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
