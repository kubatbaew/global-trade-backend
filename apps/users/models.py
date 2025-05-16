from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.clients.models import Client


class User(AbstractUser):
    first_name = None
    last_name = None

    telegram_id = models.CharField(
        max_length=120,
    )
    client_id = models.OneToOneField(
        Client, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    name = models.CharField(
        max_length=120,
        blank=True, null=True
    )
    surname = models.CharField(
        max_length=120,
        blank=True, null=True
    )
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
