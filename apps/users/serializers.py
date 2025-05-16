from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserGetMeSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "id",
            "telegram_id",
            "client_id",
            "name",
            "surname",
            "phone_number",
            "is_admin",
            "balance",
        ]
    
    def get_balance(self, obj):
        try:
            return obj.client_id.cashback.balance
        except AttributeError:
            return None

