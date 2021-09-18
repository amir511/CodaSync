from django.db import models


class Shop(models.Model):
    '''
    A shop represents a physical shop that has many products (Stock readings).
    '''

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
