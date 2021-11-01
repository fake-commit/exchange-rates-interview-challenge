from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import ExchangeRate
from core.serializers import ExchangeRateSerializer
from core.tasks import get_current_exchange_rate


class ExchangeRateViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = ExchangeRate.objects.all()
        serializer = ExchangeRateSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        exchange_rate = get_current_exchange_rate(
            from_currency=request.data.get('from_currency', 'BTC'),
            to_currency=request.data.get('to_currency', 'USD'),
        )
        serializer = ExchangeRateSerializer(exchange_rate)
        return Response(serializer.data)