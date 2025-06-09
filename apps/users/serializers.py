from rest_framework import serializers

from django.contrib.auth import get_user_model

from apps.cashbacks.models import CashbackBalance
from apps.cashbacks.serializers import CashbackBalanceSerializer
from apps.clients.serializers import ClientListSerializer

from apps.clients.models import Client

User = get_user_model()


class UserGetMeSerializer(serializers.ModelSerializer):
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

    def validate_telegram_id(self, value):
        if User.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("User with telegramId already exists.")
        return value


class UserCreateSerializer(serializers.ModelSerializer):
    client_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "telegram_id",
            "client_code",
        ]

    def validate_telegram_id(self, value):
        if User.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("User with telegramId already exists.")
        return value

    def validate_client_code(self, value):
        try:
            client = Client.objects.get(client_code=value)
        except Client.DoesNotExist:
            raise serializers.ValidationError("Client with this code does not exist.")
        
        if User.objects.filter(client=client).exists():
            raise serializers.ValidationError("User with this client already exists.")
        
        return value


    def create(self, validated_data):
        client_code = validated_data.pop("client_code")
        client = Client.objects.get(client_code=client_code)
        user = User.objects.create(client=client, **validated_data)
        CashbackBalance.objects.create(user=user)
        return user


class UserTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'telegram_id',
        ]
