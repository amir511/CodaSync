from rest_framework.viewsets import ModelViewSet

from sync.apps.shop.models import Shop
from sync.apps.shop.serializers import ShopSerializer


class ShopViewSet(ModelViewSet):
    '''
    CRUD endpoints for Shop model.
    '''

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
