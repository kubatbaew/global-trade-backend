from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class CashbackBalance(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="balance",
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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="transactions",
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
