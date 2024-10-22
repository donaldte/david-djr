from django.db import models

from django.db import models
from Hotels.models import Hotel
from accounts.models import CustomUser
from Rooms.models import Room

status = (('CONFIRMEE' , 'confirmee') , ('ANNULEE' , 'annulee'))
class Reservation(models.Model):
        hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
        room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
        start_date = models.DateField() 
        end_date = models.DateField()
        total_price = models.FloatField(blank=True, null=True)
        status = models.CharField(choices=status)

        def __str__(self):
            return self.hotel + "---" + self.total_price

