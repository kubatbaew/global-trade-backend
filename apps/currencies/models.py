from django.db import models


class Currency(models.Model):
    exchange_rate = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return str(self.exchange_rate)
