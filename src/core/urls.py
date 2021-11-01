from rest_framework.routers import DefaultRouter

from core.views import ExchangeRateViewSet

router = DefaultRouter()
router.register('quotes', ExchangeRateViewSet, basename='quotes')
urlpatterns = router.urls