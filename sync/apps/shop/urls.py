from django.urls import path
from rest_framework.routers import DefaultRouter

from sync.apps.shop.views import ShopViewSet

router = DefaultRouter()

router.register(r'shops', ShopViewSet, basename='shops')

urlpatterns = router.urls
