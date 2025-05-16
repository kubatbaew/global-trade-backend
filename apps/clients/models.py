from django.db import models


class Client(models.Model):
    client_code = models.CharField(
        max_length=8,
    )
    name = models.CharField(
        max_length=120,
    )
    surname = models.CharField(
        max_length=120,
    )
    phone_number = models.CharField(
        max_length=12,
    )
    phone_number_whatsapp = models.CharField(
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
    guanjou_address = models.CharField(
        max_length=1000,
    )

    def __str__(self):
        return self.client_code
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
