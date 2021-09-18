from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from sync.apps.shop.models import Shop


class ShopSerializer(ModelSerializer):
    '''
    Shop serializer.
    '''

    class Meta:
        model = Shop
        fields = '__all__'
