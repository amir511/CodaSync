from django.urls import path
from rest_framework.routers import DefaultRouter

from sync.apps.shop.views import ShopViewSet, StockReadingViewSet

router = DefaultRouter()

router.register(r'shops', ShopViewSet, basename='shops')
router.register(r'stock-readings', StockReadingViewSet, basename='stock_readings')


urlpatterns = router.urls
