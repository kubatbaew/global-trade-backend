from django.db import models

from django.contrib.auth.hashers import make_password, identify_hasher
from django.core.exceptions import ImproperlyConfigured

from django.contrib.auth.models import AbstractUser

from apps.clients.models import Client


class User(AbstractUser):
    telegram_id = models.CharField(
        max_length=120,
    )
    client = models.OneToOneField(
        Client, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    is_admin = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except (ValueError, ImproperlyConfigured):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

# new users
# - id, telegram_id, client, balance - total