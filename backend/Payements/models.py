from django.db import models
from Hotels.models import Hotel
from accounts.models import CustomUser
from Reservations.models import Reservation



room_choices_type = (('PAYPAL' , 'paypal') , ('CARTE_CREDIT' , 'carte_credit') , ('ORANGE_MONEY' , 'orange_money') ,  ('MTN_MONEY' , 'mtn_money'))
status_payement = (('REUSSIR' , 'reussir') , ('ECHOUE' , 'echoue'))
class Payements(models.Model):
        reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
        price= models.FloatField(blank=True, null=True) 
        date_payement = models.DateTimeField()
        total_price = models.FloatField(blank=True, null=True)
        payement_method = models.CharField(choices=room_choices_type)
        status_payement = models.CharField(choices=status_payement)

        def __str__(self):
            return self.payement_method + "---" + self.status_payement

