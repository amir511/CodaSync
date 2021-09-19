from django.db import transaction
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from sync.apps.shop.models import Shop, StockReading
from sync.apps.shop.serializers import ShopSerializer, StockReadingSerializer


class ShopViewSet(ModelViewSet):
    '''
    CRUD endpoints for Shop model.
    '''

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class StockReadingViewSet(ModelViewSet):
    '''
    CRUD endpoints for Stock reading model.
    '''

    queryset = StockReading.objects.all()
    serializer_class = StockReadingSerializer

    def update(self, request, *args, **kwargs):
        '''
        Override of update method to achieve:
        1- atomic transaction
        2- DB row locking while update
        '''
        partial = kwargs.pop('partial', False)

        with transaction.atomic():
            # Lock row using select_for update, but actually use the instance from get_object
            StockReading.objects.select_for_update().get(pk=kwargs['pk'])
            instance = self.get_object()
            # Make sure expiry_date is modified ONLY if it is more recent than the original date
            try:
                new_expiry_date = parse_date(request.data.get('expiry_date'))
            except ValueError:
                new_expiry_date = None

            if new_expiry_date and instance.expiry_date <= new_expiry_date:
                request.data['expiry_date'] = instance.expiry_date

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
