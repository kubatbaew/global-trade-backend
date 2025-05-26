from django.db import models

from apps.clients.models import Client


class CashbackBalance(models.Model):
    client = models.OneToOneField(
        Client, on_delete=models.CASCADE,
        related_name="cashback_balance",
    )
    total_earned = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0,
        verbose_name="всего сколько начислено кешбэков"
    )
    total_used = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0, verbose_name="всего сколько потрачено кешбэков",
    )
    current_balance = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0, verbose_name="актуальный баланс кешбэка",
    )
    total_weight = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0, verbose_name="всего сколько веса было",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class CashbackTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('EARNED', 'Earned'),
        ('USED', 'Used'),
    ]

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        related_name="cashback_transactions",
    )
    transaction_type = models.CharField(
        max_length=6,
        choices=TRANSACTION_TYPES
    )
    cashback_amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name="сумма начислямого кэшбека",
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        verbose_name="сумма оплаты пользователя"
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        verbose_name="вес",
    )
    balance_before = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    balance_after = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    description = models.TextField(
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
