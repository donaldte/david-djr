from django.db import models
from Hotels.models import Hotel
from accounts.models import CustomUser
from Reservations.models import Reservation
from Rooms.models import Room


class Commentaire(models.Model):
        hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
        notation = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Notation de 1 à 5
        commentaire = models.TextField()
        create_date = models.DateTimeField()
        room = models.ForeignKey(Room , on_delete=models.CASCADE, null=True, blank=True)

        def __str__(self):
            return self.commentaire 


