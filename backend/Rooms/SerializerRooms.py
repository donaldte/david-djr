from rest_framework import serializers
from .models import Room
from Hotels import serializerHotels


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
