from django.db import models, transaction


class Shop(models.Model):
    '''
    A shop represents a physical shop that has many products (Stocks).
    '''

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class StockReading(models.Model):
    '''
    StockReading represents a record for the shortest expiry date of a specific stock (product).
    In a real life scenario, there should be another table for the stocks (products)
    And it should be linked to this table through a foreign key.
    But for simplicity, we are treating both tables as one.
    '''

    name = models.CharField(max_length=255)
    GTIN = models.CharField(max_length=14, unique=True)
    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='stock_readings')
    expiry_date = models.DateField()

    def __str__(self):
        return f'{self.name} (GTIN:{self.GTIN})'
