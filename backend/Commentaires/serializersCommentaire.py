from rest_framework import serializers
from .models import Commentaire
from Rooms import SerializerRooms
from Hotels import serializerHotels


class CommentaireSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    room = SerializerRooms()
    hotel = serializerHotels()
    class Meta:
        model = Commentaire
        field = '__all__'