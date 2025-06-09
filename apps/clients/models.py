from django.db import models


class Client(models.Model):
    client_code = models.CharField(
        max_length=8,
        unique=True,
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(
        max_length=12,
    )
    whatsapp_number = models.CharField(
        max_length=12,
    )
    city = models.CharField(
        max_length=120,
    )
    address = models.CharField(
        max_length=120,
        blank=True, null=True
    )
    ref_link = models.CharField(
        max_length=120,
        blank=True, null=True,
    )
    china_warehouse_address = models.CharField(
        max_length=1000,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.client_code
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
