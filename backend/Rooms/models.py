from django.db import models
from Hotels.models import Hotel
from accounts.models import CustomUser



status = (('CONFIRMEE' , 'confirmee') , ('ANNULEE' , 'annulee'))
room_choices_type = (('SIMPLE' , 'simple') , ('DOUBLE' , 'double') , ('VIP' , 'vip'))
class Room(models.Model):
        hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
        room_number = models.CharField()
        price= models.FloatField(blank=True, null=True) 
        capacity = models.IntegerField()
        total_price = models.FloatField(blank=True, null=True)
        is_available = models.BooleanField()
        room_type = models.CharField(choices=room_choices_type)

        def __str__(self):
            return self.hotel + "---" + self.room_number
