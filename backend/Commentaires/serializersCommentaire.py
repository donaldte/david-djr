from rest_framework import serializers
from .models import Commentaire
from Rooms import SerializerRooms
from Hotels import serializerHotels


class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        field = '__all__'


    def validate_commentaire(value , self):
        if len(value) > 500:
            raise serializers.ValidationError("Le commentaire ne peut pas depasser 500 caracteres")
        return value