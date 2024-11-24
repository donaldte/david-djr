from rest_framework import serializers
from .models import Commentaire


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        field = '__all__'