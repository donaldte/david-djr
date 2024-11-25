from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name
    
    
    def get_product_name(self):
        return self.name
    
    def get_product_description(self):
        return self.description
    
    def get_product_price(self):
        return self.price
    
    def get_product_owner(self):
        return self.owner