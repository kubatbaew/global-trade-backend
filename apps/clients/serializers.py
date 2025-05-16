from rest_framework import serializers

from apps.clients.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "client_code",
            "name",
            "surname",
            "phone_number",
            "phone_number_whatsapp",
            "city",
            "address",
            "ref_link",
            "guanjou_address",
        ]
