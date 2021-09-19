from rest_framework.serializers import ModelSerializer

from sync.apps.shop.models import Shop, StockReading


class ShopSerializer(ModelSerializer):
    '''
    Shop serializer.
    '''

    class Meta:
        model = Shop
        fields = '__all__'


class StockReadingSerializer(ModelSerializer):
    '''
    StockReading serializer.
    '''

    class Meta:
        model = StockReading
        fields = '__all__'
