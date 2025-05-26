from rest_framework import serializers

from apps.clients.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "client_code",
            "first_name",
            "last_name",
            "phone_number",
            "whatsapp_number",
            "city",
            "address",
            "ref_link",
            "china_warehouse_address",
            "created_at",
        ]
