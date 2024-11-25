

from rest_framework import serializers
from Reservations import serializerReservation
from models import Payements


class PaymentSerializer(serializers.ModelSerializer):
    reservation = serializerReservation()
    class Meta:
        model = Payements
        fields = '__all__'