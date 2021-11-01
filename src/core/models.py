from django.db import models
from django.utils import timezone


class ExchangeRate(models.Model):

    from_currency = models.CharField(max_length=10)

    to_currency = models.CharField(max_length=10)

    rate = models.FloatField()

    timestamp = models.DateTimeField(default=timezone.now)