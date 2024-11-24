from rest_framework import serializers
from .models import Room


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        field = '__all__'
