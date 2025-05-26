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
            "first_name",
            "last_name",
            "phone_number",
            "is_admin",
        ]
        read_only_fields = [
            "is_admin",
            "id",
        ]
    
    def validate_client_code(self, value):
        if User.objects.filter(client_code=value).exists():
            raise serializers.ValidationError("User with client_code already exists.")
        return value
