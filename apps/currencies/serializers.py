from rest_framework import serializers

from apps.currencies.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "id",
            "exchange_rate",
        ]
