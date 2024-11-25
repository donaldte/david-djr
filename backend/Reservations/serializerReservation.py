from rest_framework import serializers
from .models import Reservation
from Rooms import SerializerRooms


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        field = '__all__'






