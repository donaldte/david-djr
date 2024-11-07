from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        field = '__all__'

