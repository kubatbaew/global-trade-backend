from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserGetMeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "telegram_id",
            "client_code",
            "full_name",
            "phone_number",
            "is_admin",
        ]

