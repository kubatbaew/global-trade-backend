from django.db import models

from apps.clients.models import Client

class CashBack(models.Model):
    client_id = models.OneToOneField(
        Client, on_delete=models.CASCADE,
        related_name="cashback"
    )
    balance = models.DecimalField(
        max_digits=7, decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.client_id.client_code
    
    class Meta:
        verbose_name = "CashBack"
        verbose_name_plural = "CashBacks"
