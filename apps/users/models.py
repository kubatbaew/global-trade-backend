from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.clients.models import Client


class User(AbstractUser):
    telegram_id = models.CharField(
        max_length=120,
    )
    # client_id = models.OneToOneField(
    #     Client, on_delete=models.SET_NULL,
    #     blank=True, null=True
    # )
    client_code = models.CharField(
        max_length=8,
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(
        max_length=12,
        blank=True, null=True
    )
    is_admin = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
