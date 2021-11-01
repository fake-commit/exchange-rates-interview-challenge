from datetime import datetime

import requests
from celery import shared_task
from django.conf import settings

from core.models import ExchangeRate


@shared_task
def get_current_exchange_rate(from_currency, to_currency):

     ploads = {
          'function': 'CURRENCY_EXCHANGE_RATE',
          'from_currency': from_currency,
          'to_currency': to_currency,
          'apikey': settings.ALPHAVANTAGE_API_KEY
     }

     data = requests.get(settings.ALPHAVANTAGE_API_URL, params=ploads)

     exchange_rate_dict = data.json().get('Realtime Currency Exchange Rate', {})

     exchange_rate = ExchangeRate(
          from_currency=exchange_rate_dict.get('1. From_Currency Code', ''),
          to_currency=exchange_rate_dict.get('3. To_Currency Code', ''),
          rate=exchange_rate_dict.get('5. Exchange Rate', ''),
          timestamp=datetime.strptime(exchange_rate_dict.get('6. Last Refreshed', ''), '%Y-%m-%d %H:%M:%S')
     )

     exchange_rate.save()

     return exchange_rate