from rest_framework import serializers

from core.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = ('from_currency', 'to_currency', 'rate', 'timestamp')
        extra_kwargs = {
            'from_currency': {'required': True},
            'to_currency': {'required': True},
            'rate': {'required': True},
        }