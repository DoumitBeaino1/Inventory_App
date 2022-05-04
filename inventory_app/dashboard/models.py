from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models


# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=100, null=True)
    GTIN = models.BigIntegerField()
    expiry_date = models.DateField()
    
    def __str__(self):
        return f'{"GTIN: "}{self.GTIN}'
